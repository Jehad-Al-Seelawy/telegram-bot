from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# ضع التوكن مباشرة
TOKEN = "7756938468:AAG0n8ynT2FV3KQoeu641XIL_x8WyoV2wdI"

# دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تفضل تستحيش")

# إعداد البوت باستخدام ApplicationBuilder
app = ApplicationBuilder().token(TOKEN).build()

# إضافة الأمر /start
app.add_handler(CommandHandler("start", start))

# Webhook لإعادة التشغيل على Render بدون تعارض
PORT = int(os.environ.get('PORT', 5000))
WEBHOOK_URL = f"https://Sarehny.onrender.com/{TOKEN}"

# تشغيل البوت
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL,
    secret_token=TOKEN
)
