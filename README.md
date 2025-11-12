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
git clone https://github.com/chillhackr/mynewbot.git
cd mynewbot
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
OR

run your scripts like I do:
```bash
# (choose one)
# Windows:
.\venv\Scripts\[pip|python]
# macOS/Linux:
./venv/bin/[pip|python]
```

### 3️⃣ Install dependencies
Run your scripts without an environment activated:
```bash
# (choose one)
# Windows:
.\venv\Scripts\pip.exe install -r requirements.txt
# macOS/Linux:
./venv/bin/pip install -r requirements.txt
```

or use the activated environment

```bash
pip install -r requirements.txt
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
or if not using the activated environment:
```bash
# (choose one)
# Windows:
.\venv\Scripts\python.exe main.py
# macOS/Linux:
./venv/bin/python main.py
```

You should see:
```
Bot running... Press Ctrl+C to stop.
```
Feel free to edit the logic.

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
or alternatively:

```bash
./venv/bin/pip install -r requirements.txt
```
```bash
.\venv\Scripts\pip.exe install -r requirements.txt
```

---

## 🧹 Maintenance

- Stop the bot: `CTRL + C`  
- Deactivate the virtual environment: `deactivate` if not running from ./venv/[bin|Scripts]
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
