from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import asyncio

TOKEN = "8900192006:AAHiAMcv4scRw45R-je3txY1yLstcvVhStY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Gold Sniper Bot Active!\n\n"
        "Command:\n"
        "/signal - Gold Signal"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    signals = [
        "🟢 BUY XAUUSD\n\nEntry: 3345.20\nSL: 3342.20\nTP: 3351.20",
        "🔴 SELL XAUUSD\n\nEntry: 3348.80\nSL: 3352.00\nTP: 3342.80"
    ]
    await update.message.reply_text(random.choice(signals))

async def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("Gold Sniper Bot Started")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(run_bot())