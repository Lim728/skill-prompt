# Skill Prompt

> Turn your plain-language requirements into high-purity AI Agent skill prompts.

**[中文文档](./README.zh.md)**

---

## Features

- **One-click generation** — Describe what you want in plain language, get a structured Skill system prompt
- **Multi-model support** — DeepSeek-R1, GPT-4o, GPT-4o-mini, or any custom OpenAI-compatible API
- **Bilingual UI** — Full Chinese / English interface switch
- **Dark / Light / System theme** — With custom background image support
- **Typing animation** — 10 rotating example prompts as input hints
- **Stop generation** — Cancel long-running requests at any time
- **Docker ready** — One-command deployment

---

## Quick Start

### Prerequisites

- Python 3.11+
- Docker (optional)

### Local Run

```bash
# Install dependencies
pip install -r backend/requirements.txt

# Start server
cd backend
python main.py
```

Open `http://localhost:8000` in your browser.

### Docker Deploy

```bash
docker compose up -d --build
```

Open `http://your-server-ip:7619` in your browser.

---

## Project Structure

```
mimo-skill-factory/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── README.md
├── README.zh.md
├── backend/
│   ├── main.py
│   └── requirements.txt
└── frontend/
    ├── index.html
    └── assets/
        └── favicon.png
```

---

## How It Works

1. You describe a Skill requirement in plain language
2. The app sends it to your chosen AI model with a structured meta-prompt
3. The model returns a rigidly structured Skill system prompt
4. Copy the result and use it in your local AI agent

---

## Configuration

All settings are saved in the browser's `localStorage`:

| Setting | Description |
|---|---|
| API Key | Your AI model API key (never uploaded) |
| Base URL | API endpoint |
| Model Name | Model identifier |
| Theme | Dark / Light / System |
| Language | Chinese / English |
| Background | Custom image URL or upload |

---

## API Endpoint

```
POST /api/generate-prompt
Content-Type: application/json

{
  "requirement": "your skill description",
  "config": {
    "provider": "deepseek-r1",
    "api_key": "sk-xxx",
    "base_url": "https://api.deepseek.com",
    "model_name": "deepseek-reasoner"
  },
  "lang": "en"
}
```

Response:

```json
{
  "success": true,
  "prompt": "# Role & Objective\n..."
}
```

---

## Tech Stack

- **Backend**: Python, FastAPI, OpenAI SDK
- **Frontend**: Vanilla HTML / CSS / JS
- **Deploy**: Docker

---

## License

MIT
