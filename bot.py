from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# التوكن الحقيقي للبوت
TOKEN = "7756938468:AAG0n8ynT2FV3KQoeu641XIL_x8WyoV2wdI"

# كلمة سرية بسيطة للـ Webhook (لا تستخدم التوكن هنا)
SECRET = "mysecret123"

# دالة الرد على /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تفضل تستحيش")

# إعداد التطبيق
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# إعداد Webhook للـ Render
PORT = int(os.environ.get("PORT", 5000))
WEBHOOK_URL = f"https://Sarehny.onrender.com/{SECRET}"

# تشغيل البوت
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL,
    secret_token=SECRET
)
