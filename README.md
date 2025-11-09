# mynewbot
learning bots on telegram

# 📨 Telegram Bot — Forwarded Message Inspector

A Telegram bot that **analyzes forwarded messages** and shows their metadata in structured JSON format.  
It also saves forwarded message info to a local log file (`forwarded.json`) and provides a command to reprint the most recent entry.

---

## 🚀 Features

- Detects and inspects **forwarded messages**
- Displays detailed metadata (original sender, chat, date, content, etc.)
- Saves message data to `forwarded.json`
- `/test` command to view the **last forwarded message**
- Automatically registers bot commands in Telegram

---

## ⚙️ Available Commands

| Command | Description |
|----------|--------------|
| `/start` | Starts the bot and sends a short welcome message |
| `/test` | Prints details of the last forwarded message |
| *(no command)* | Simply forward any message to the bot — it will analyze and return structured info |

---

## 📦 Requirements

- Python **3.10+**
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- Git (optional, for cloning the repo)

---

## 🧰 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/forwarded-message-inspector.git
cd forwarded-message-inspector
```

### 2️⃣ Create and activate a virtual environment
```bash
# Create
python -m venv venv

# Activate (choose one)
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```txt
# Telegram bot framework
python-telegram-bot

# Environment variable loader
python-dotenv
```

---

## ⚙️ Configuration

Create a `.env` file in the project directory:
```bash
BOT_TOKEN=your_telegram_bot_token_here
```

---

## ▶️ Running the Bot

Start your bot by running:
```bash
python bot.py
```

You should see:
```
Bot running... Press Ctrl+C to stop.
```

Then open your Telegram app and:

1. Forward any message to your bot → it replies with structured JSON info.  
2. Use `/test` to show the last forwarded message again.

---

## 📁 Data Logging

All analyzed forwarded messages are saved in:
```
forwarded.json
```

Each entry includes fields such as:
```json
{
  "message_id": 1234,
  "date": "2025-11-07T17:23:10",
  "chat": {...},
  "forward_from": {...},
  "text": "Example message",
  "photo": [],
  "video": null
}
```

If the log file becomes corrupted, it will automatically reset.

---

## 🔄 Updating from GitHub

If you’ve cloned from GitHub:
```bash
git pull origin main
```

Then reinstall dependencies if needed:
```bash
pip install -r requirements.txt
```

---

## 🧹 Maintenance

- Stop the bot: `CTRL + C`  
- Deactivate the virtual environment: `deactivate`  
- Delete logs (if needed): `rm forwarded.json`

---

## 🧪 Example Use

**Forward a message to the bot:**
```
📨 Forwarded Message Info:
{
  "message_id": 88,
  "chat_id": 123456789,
  "forward_from_chat": { "title": "Example Channel" },
  "forward_date": "2025-11-07T12:00:00",
  "text": "Hello from another chat!"
}
```

**Then run:**
```
/test
```
→ returns the same info again.

** work in progress **
