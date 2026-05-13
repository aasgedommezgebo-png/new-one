import asyncio
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)
from telegram.request import HTTPXRequest

# ======================
# TOKEN (Render + Local safe)
# ======================
TOKEN = os.getenv("TOKEN") or "PUT_YOUR_BOT_TOKEN_HERE"

# ======================
# /start COMMAND
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is working successfully!")

# ======================
# MAIN FUNCTION
# ======================
async def main():
    # FIX: Connection timeout (prevents ConnectTimeout error)
    request = HTTPXRequest(
        connect_timeout=30,
        read_timeout=30,
        write_timeout=30,
        pool_timeout=30,
    )

    # Build bot
    app = ApplicationBuilder().token(TOKEN).request(request).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot running...")

    # Run bot
    await app.run_polling()

# ======================
# RUN BOT
# ======================
if __name__ == "__main__":
    asyncio.run(main())
