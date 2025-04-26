# source .venv/bin/activate
from typing import Union
from fastapi import FastAPI

from email_sender import send_email

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/send-email/")
def trigger_email(subject: str, body: str, to_email: str, from_email: str, from_password: str, smtp_server: str, smtp_port: int):
    # send_email(subject, body, to_email, from_email, from_password, smtp_server, smtp_port)
    send_email("", "", "", "", "", "", "")
    return {"message": "Email sent successfully"}
#  send_email("","", "", "", "", "", "")
#    send_email(subject, body, to_email, from_email, from_password, smtp_server, smtp_port)
