
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

TOKEN = 8673682951:AAFa-tP8yU5nqcKvvxXE13xFxtNiAFvoJbM

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

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Gold Sniper Bot Started")
app.run_polling()