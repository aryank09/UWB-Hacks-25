import json
import os
from typing import Any
# /opt/homebrew/bin/python3.11
# james@Jamess-MacBook-Air-197 agentchat fastapi % python -m venv .venv
# james@Jamess-MacBook-Air-197 agentchat fastapi % source .venv/bin/activate
import aiofiles
import yaml
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_core.models import ChatCompletionClient
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from email_sender import send_email
from generate_phishing_email import generate_phishing_email

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# mount the `static` folder at the URL path `/static`
BASE_DIR = os.path.dirname(__file__)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static",
)


@app.get("/")
async def root():
    """Serve the chat interface HTML file."""
    # return FileResponse("app_agent.html")
    return FileResponse("index.html")

model_config_path = "model_config.yaml"
state_path = "agent_state.json"
history_path = "agent_history.json"

@app.on_event("startup")
async def clear_history_file():
    if os.path.exists(history_path):
        os.remove(history_path)


async def get_agent() -> AssistantAgent:
    """Get the assistant agent, load state from file."""
    # Get model client from config.
    async with aiofiles.open(model_config_path, "r") as file:
        model_config = yaml.safe_load(await file.read())
    model_client = ChatCompletionClient.load_component(model_config)

    # Load system prompt context from file
    async with aiofiles.open("system_prompt.txt", "r") as prompt_file:
        llm_prompt_context = await prompt_file.read()

    # Create the assistant agent.
    agent = AssistantAgent(
        name="assistant",
        model_client=model_client,
        system_message=llm_prompt_context,
    )

    # Load state from file.
    if not os.path.exists(state_path):
        return agent  # Return agent without loading state.
    async with aiofiles.open(state_path, "r") as file:
        state = json.loads(await file.read())
    await agent.load_state(state)
    return agent



async def get_history() -> list[dict[str, Any]]:
    """Get chat history from file."""
    if not os.path.exists(history_path):
        return []
    async with aiofiles.open(history_path, "r") as file:
        return json.loads(await file.read())


@app.get("/history")
async def history() -> list[dict[str, Any]]:
    try:
        return await get_history()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@app.post("/chat", response_model=TextMessage)
async def chat(request: TextMessage) -> TextMessage:
    try:
        # Get the agent and respond to the message.
        agent = await get_agent()
        response = await agent.on_messages(messages=[request], cancellation_token=CancellationToken())

        # Save agent state to file.
        state = await agent.save_state()
        async with aiofiles.open(state_path, "w") as file:
            await file.write(json.dumps(state))

        # # Save chat history to file.
        # history = await get_history()
        # history.append(request.model_dump())
        # history.append(response.chat_message.model_dump())
        # async with aiofiles.open(history_path, "w") as file:
        #     await file.write(json.dumps(history))

        assert isinstance(response.chat_message, TextMessage)
        return response.chat_message
    except Exception as e:
        error_message = {
            "type": "error",
            "content": f"Error: {str(e)}",
            "source": "system"
        }
        raise HTTPException(status_code=500, detail=error_message) from e


@app.post("/send-email/")
def trigger_email(subject: str, body: str, to_email: str, from_email: str, from_password: str, smtp_server: str, smtp_port: int):
    # send_email(subject, body, to_email, from_email, from_password, smtp_server, smtp_port)
    send_email()
    return {"message": "Email sent successfully"}
#  send_email("","", "", "", "", "", "")
#    send_email(subject, body, to_email, from_email, from_password, smtp_server, smtp_port)


@app.post("/generate-phishing-email")
async def generate_email_endpoint():
    return await generate_phishing_email()

# Example usage
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
