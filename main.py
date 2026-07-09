from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import logging


TOKEN = "8900192006:AAHiAMcv4scRw45R-je3txY1yLstcvVhStY"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Gold Sniper Bot Started Successfully!\n\n"
        "Available Commands:\n"
        "/signal - Get Gold Signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signals = [
        {
            "type": "🟢 BUY",
            "entry": "3345.20",
            "sl": "3342.20",
            "tp": "3351.20"
        },
        {
            "type": "🔴 SELL",
            "entry": "3348.80",
            "sl": "3352.00",
            "tp": "3342.80"
        }
    ]

    s = random.choice(signals)

    msg = f"""
{s['type']} XAUUSD

📍 Entry : {s['entry']}
🛑 Stop Loss : {s['sl']}
🎯 Take Profit : {s['tp']}

⚠️ Risk only 1-2% per trade.
"""

    await update.message.reply_text(msg)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("✅ Gold Sniper Bot Running...")

    app.run_polling(
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES
    )

if __name__ == "__main__":
    main()
