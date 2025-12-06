from telegram.ext import Updater, CommandHandler
import os

# ضع التوكن مباشرة
TOKEN = "7756938468:AAG0n8ynT2FV3KQoeu641XIL_x8WyoV2wdI"

# دالة البداية
def start(update, context):
    update.message.reply_text("Hello! Bot is running.")

# إعداد البوت
updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))

# ===== Webhook لإعادة التشغيل على Render بدون تعارض =====
PORT = int(os.environ.get('PORT', 5000))

updater.start_webhook(
    listen="0.0.0.0",
    port=PORT,
    url_path=TOKEN
)

# رابط البوت على Render مع اسم الخدمة (تأكد من مطابقة الحروف)
updater.bot.set_webhook(f"https://Sarehny.onrender.com/{TOKEN}")

# تشغيل البوت
updater.idle()
