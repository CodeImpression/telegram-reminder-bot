from telegram import Bot
import random
from datetime import datetime
import pytz
import os

BOT_TOKEN = os.getenv("BOT_TOKEN") or 'your_bot_token_here'
CHAT_ID = os.getenv("CHAT_ID") or 'your_chat_id_here'

bot = Bot(token=BOT_TOKEN)

def send_reminder():
    tz = pytz.timezone('Europe/London')
    now = datetime.now(tz)
    hour = now.hour
    print(f"[DEBUG] send_reminder called at UK hour: {hour}")

    message = None  # Initialize message

    if 7 <= hour < 16:
        messages = [
            "🚫 Don't eat 🛑 Drink water 💧",
            "🥶 Step away from the snacks — hydrate instead 💧",
            "💪 Hunger isn’t the boss. Water is 💧",
            "🤖 Override craving: initiated. Water protocol engaged 💧",
            "🚨 Avoid empty calories - DRINK WATER 💧"
        ]
        message = random.choice(messages)
    elif 16 <= hour < 21:
        messages = [
            "🍷 Don't drink alcohol- you do not need it️",
            "❌ No alcohol tonight — be the boss of your brain 🧠",
            "🚱 Skipping the booze = levelling up ⬆",
            "🧃 Sip something else. You're rewiring your life",
            "🍸 Tempted? Nah. You’re on mission mode. 🎯"
        ]
        message = random.choice(messages)
    elif hour == 21:
        message = "⭐ You made it through the day"
    else:
        print("[DEBUG] Outside message hours; no message sent.")
        return

    if message:
        try:
            bot.send_message(chat_id=CHAT_ID, text=message)
            print(f"[DEBUG] Sent message: {message}")
        except Exception as e:
            print(f"[ERROR] Failed to send message: {e}")