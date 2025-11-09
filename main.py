"""
Telegram Bot — Forwarded Message Inspector with a dashboard to view them. 
------------------------------------------
This bot:
*  listens for forwarded messages, prints metadata
* new features coming soon!
"""

from telegram import Update,BotCommand
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import json, os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
LOG_FILE = "forwarded.json"

#last forwarded message info
last_forwarded_info = None

########################################################################################
########################################################################################

def tg_to_dict(obj):
    if obj is None:
        return None
    try:
        return obj.to_dict()
    except Exception:
        return str(obj)


def load_forwarded_log():
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Warning: forwarded.json is corrupt, starting new file.")
            return []
    return []


def save_forwarded_log(data):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def append_to_forwarded_log(entry):
    logs = load_forwarded_log()
    logs.append(entry)
    save_forwarded_log(logs)

#############################
# command handler functions
#############################

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! Forward a message to me to inspect it.")

async def handle_forwarded(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_forwarded_info

    msg = update.message
    info = {}
    tochat = {}

    # Basic message info
    info["message_id"] = msg.message_id
    tochat["message_id"] = msg.message_id
    info["date"] = msg.date.isoformat()
    tochat["date"] = msg.date.isoformat()
    info["chat"] = tg_to_dict(msg.chat)
    tochat["chat"] = tg_to_dict(msg.chat)
    info["chat_id"] = msg.chat.id
    tochat["chat_id"] = msg.chat.id
    info["from_user"] = tg_to_dict(msg.from_user)

    # Forwarded source info
    try:
        info["forward_from"] = tg_to_dict(msg.forward_from)  # user it was forwarded from
        tochat["forward_from"] = tg_to_dict(msg.forward_from)
    except Exception as e:
        info["forward_from_error"] = 'NotFound'
        tochat["forward_from_error"] = 'NotFound'
    try:
        info["forward_from_chat"] = tg_to_dict(msg.forward_from_chat)  # group/channel source
        tochat["forward_from_chat"] = tg_to_dict(msg.forward_from_chat)
    except Exception:
        info["forward_from_chat_error"] = 'NotFound'
        tochat["forward_from_chat_error"] = 'NotFound'
    try:
        info["forward_from_message_id"] = msg.forward_from_message_id
        tochat["forward_from_message_id"] = msg.forward_from_message_id
    except Exception:
        info["forward_from_message_id_error"] = 'NotFound'
        tochat["forward_from_message_id_error"] = 'NotFound'
    try:
        info["forward_signature"] = msg.forward_signature
        tochat["forward_signature"] = msg.forward_signature
    except Exception:
        info["forward_signature_error"] = 'NotFound'
        tochat["forward_signature_error"] = 'NotFound'
    try:
        info["forward_sender_name"] = msg.forward_sender_name
        tochat["forward_sender_name"] = msg.forward_sender_name
    except Exception:
        info["forward_sender_name_error"] = 'NotFound'
        tochat["forward_sender_name_error"] = 'NotFound'
    try:
        info["forward_date"] = (
            msg.forward_date.isoformat() if msg.forward_date else None
        )
        tochat["forward_date"] = (
            msg.forward_date.isoformat() if msg.forward_date else None
        )
    except Exception:
        info["forward_date_error"] = 'NotFound'
        tochat["forward_date_error"] = 'NotFound'

    # Text content
    info["text"] = msg.text or msg.caption
    tochat["text"] = msg.text or msg.caption

    # Entities (mentions, links, etc.)
    info["entities"] = [tg_to_dict(e) for e in (msg.entities or [])]
    info["caption_entities"] = [tg_to_dict(e) for e in (msg.caption_entities or [])]

    # Media (photo, video, etc.)
    info["photo"] = [tg_to_dict(p) for p in (msg.photo or [])]
    info["video"] = tg_to_dict(msg.video)
    info["document"] = tg_to_dict(msg.document)
    info["sticker"] = tg_to_dict(msg.sticker)
    info["animation"] = tg_to_dict(msg.animation)
    info["voice"] = tg_to_dict(msg.voice)
    info["audio"] = tg_to_dict(msg.audio)

    # Miscellaneous
    info["reply_to_message"] = tg_to_dict(msg.reply_to_message)
    info["via_bot"] = tg_to_dict(msg.via_bot)
    info["has_protected_content"] = msg.has_protected_content

    # Store last message in info
    last_forwarded_info = info
    append_to_forwarded_log(info)
    #send tochat in reply
    formatted = json.dumps(tochat, indent=2, ensure_ascii=False)
    await msg.reply_text(f"📨 Forwarded Message Info:\n```\n{formatted}\n```", parse_mode="MarkdownV2")


async def test_last(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reprints the last forwarded message info"""
    global last_forwarded_info
    if not last_forwarded_info:
        await update.message.reply_text("No forwarded message logged yet.")
        return

    formatted = json.dumps(last_forwarded_info, indent=2, ensure_ascii=False)
    await update.message.reply_text(
        f"🧪 Last Forwarded Message:\n```\n{formatted}\n```",
        parse_mode="MarkdownV2",
    )

########################################################################################
########################################################################################
#https://docs.python-telegram-bot.org/en/v22.1/telegram.botcommand.html
async def set_commands(app):
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("help", "get help")

    ]
    await app.bot.set_my_commands(commands)  # everyone

##################################################
# App setup
##################################################
# use next line to disable wake_up or post_init entirely
#app = ApplicationBuilder().token(BOT_TOKEN).build()
app = (ApplicationBuilder().token(BOT_TOKEN).post_init(set_commands).build())

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("test", test_last))
app.add_handler(MessageHandler(filters.FORWARDED, handle_forwarded))

print("Bot running... Press Ctrl+C to stop.")
app.run_polling()
