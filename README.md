# 🛡️ Phish Guard

> An AI-powered educational platform that teaches cybersecurity awareness through controlled phishing simulations.

![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=flat&logo=github)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-009688?style=flat&logo=fastapi)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=flat&logo=openai)


Phish Guard simulates a real phishing attack by sending a realistic fake email with a link. When clicked, the link leads to a "**You Got Scammed — but not really!**" landing page. Users can then chat with our **AI security coach**, which explains phishing tactics and teaches easy ways to stay safe. As a bonus, users can test their new skills by facing our **AI Red Team Squad**, where they identify fake versus real messages.

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API key
- SMTP server access (for email functionality) (sendgrid API key) for .env file

### Installation

1. Clone the repository:
```bash
git clone https://github.com/aryank09/UWB-Hacks-25.git
cd UWB-Hacks-25
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn aiofiles pyyaml autogen-agentchat autogen-core openai
```

4. Configure your API key:
   - Open `model_config.yaml`
   - Replace `REPLACE_WITH_YOUR_API_KEY` with your OpenAI API key

5. Run the server:
```bash
python app_agent.py
```

6. Open your browser and navigate to `http://localhost:8001`

## 🛠️ How we built it

### Tech Stack

- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Backend**: FastAPI (Python)
- **AI**: OpenAI GPT-4, AutoGen Agent Framework
- **Email**: SMTP integration
- **Styling**: Custom CSS with Tailwind utilities

### Architecture

The system consists of:
- A FastAPI backend server handling chat messages and email generation
- A responsive web interface with a sleek dark theme
- AI-powered chat agent using AutoGen framework
- Email sender integration for phishing simulation
- Static file serving for assets

### Key Components

#### Backend (`app.py`)
- FastAPI application with CORS middleware
- Chat endpoint for AI conversations
- Email generation and sending endpoints
- State persistence for conversation history

#### Frontend (`index.html`)
- Landing page with educational content
- Real-time chat interface
- Friend testing functionality
- Responsive design with custom styling

#### Configuration
- `model_config.yaml`: AI model settings
- `system_prompt.txt`: AI assistant instructions
- `agent_state.json`: Conversation state storage
- `agent_history.json`: Chat history persistence

# From Devpost:
## Challenges 

1. Creating realistic yet non-malicious AI-generated phishing examples
2. Parsing Markdown formatting cleanly in chat display
3. Time management while balancing features and AI integration
4. Keeping chatbot responses friendly and understandable for non-technical users
   
## Accomplishments 

- Built a full end-to-end phishing simulation and education platform in under 12 hours
- Seamlessly integrated AI for content generation and user education
- Created an eye-opening yet non-threatening user experience
- Developed an educational tool that removes shame from learning about cybersecurity
  
# 📦 Project Structure

```
phish-guard/
├── app.py                  # FastAPI backend server
├── index.html              # Main web interface
├── model_config.yaml       # AI model configuration
├── system_prompt.txt       # AI assistant instructions
├── email_sender.py         # Email sending functionality
├── generate_phishing_email.py # Phishing email generator
├── static/                 # Static assets
│   ├── company_logo_red.png
│   ├── company_logo_inverted.png
│   └── chatbot_icon.png
├── agent_state.json        # Conversation state (generated)
├── agent_history.json      # Chat history (generated)
└── README.md              # Project documentation
```

## 👥 Team

Built with ❤️ at UWB Hacks by our dedicated team of developers.

---

<p align="center">Made with 🛡️ for safer digital communities</p>
