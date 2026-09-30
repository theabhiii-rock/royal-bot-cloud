import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    CallbackQueryHandler,
    filters,
)

# =========================================================
# 24/7 CLOUD HEALTH CHECK SERVER
# =========================================================

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK - Bot is running 24/7!")

    def log_message(self, format, *args):
        return

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    try:
        server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
        server.serve_forever()
    except Exception as e:
        print(f"Health server error: {e}")

# =========================================================
# CONFIG
# =========================================================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

REGISTRATION_LINK = "https://one-vv4926.com/?open=register&p=4ej1"
PROMO_CODE = "RBETKING"
SUPPORT_USERNAME = "@Royal_BetKing"

# Temporary user data
user_data = {}


# =========================================================
# START
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message is None:
        return

    chat_id = update.effective_chat.id
    first_name = update.effective_user.first_name or "User"

    user_data[chat_id] = {
        "state": "waiting_for_id",
        "user_id": None,
    }

    keyboard = [
        [
            InlineKeyboardButton(
                "🔗 REGISTER NOW",
                url=REGISTRATION_LINK,
            )
        ],
        [
            InlineKeyboardButton(
                "📖 HOW TO REGISTER",
                callback_data="guide",
            )
        ],
        [
            InlineKeyboardButton(
                "🎟️ PROMO CODE",
                callback_data="promo",
            ),
            InlineKeyboardButton(
                "💬 SUPPORT",
                url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}",
            ),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    message = (
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👑 <b>WELCOME TMP KINGS 👑 </b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"Hello <b>{first_name}</b> 👋\n\n"
        "🚀 <b>Get Started in 3 Easy Steps</b>\n\n"
        "① Register your account\n"
        "② Send your User ID here\n"
        "③ Contact our support if required\n\n"
        "🎟️ <b>Promo Code:</b> "
        f"<code>{PROMO_CODE}</code>\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔐 <b>SECURE REGISTRATION</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "Tap <b>REGISTER NOW</b> to continue.\n\n"
        "After registration, send your "
        "<b>User ID</b> here 👇"
    )

    await update.message.reply_text(
        message,
        parse_mode="HTML",
        reply_markup=reply_markup,
    )


# =========================================================
# PROMO BUTTON
# =========================================================

async def promo_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.callback_query

    if query is None:
        return

    await query.answer()

    await query.message.reply_text(
        "🎟️ <b>Your Promo Code</b>\n\n"
        f"<code>{PROMO_CODE}</code>\n\n"
        "Tap and copy the code.",
        parse_mode="HTML",
    )


# =========================================================
# GUIDE BUTTON
# =========================================================

async def guide_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    if query is None:
        return
    await query.answer()

    steps = [
        ("step1.jpg", "① <b>Welcome & Bonus</b>\n\nSite open karein aur Registration button par tap karein."),
        ("step2.jpg", "② <b>Registration & Promo Code</b>\n\nApna Number/Email daalein aur Promo Code me <code>RBETKING</code> zaroor check karein."),
        ("step3.jpg", "③ <b>Deposit Methods</b>\n\nDeposit section me jakar local payment methods (UPI, Paytm, PhonePe) chunein."),
        ("step4.jpg", "④ <b>Deposit Confirmation</b>\n\nPayment ke baad 12-digit UTR number daal kar Submit karein — aapka deposit turant confirm ho jayega! ✅"),
    ]

    sent_any = False
    for filename, caption in steps:
        if os.path.exists(filename):
            with open(filename, "rb") as photo:
                await query.message.reply_photo(photo=photo, caption=caption, parse_mode="HTML")
            sent_any = True

    if not sent_any:
        text = "📖 <b>Registration & Deposit Guide</b>\n\n" + "\n\n".join([c for _, c in steps])
        await query.message.reply_text(text, parse_mode="HTML")


# =========================================================
# CHANGE ID BUTTON
# =========================================================

async def change_id_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query
    if query is None:
        return
    await query.answer()

    chat_id = update.effective_chat.id
    user_data[chat_id] = {
        "state": "waiting_for_id",
        "user_id": None,
    }

    await query.message.reply_text(
        "🔄 <b>Send your new User ID below:</b> 👇",
        parse_mode="HTML",
    )


# =========================================================
# MESSAGE HANDLER
# =========================================================

async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id

    if not update.message.text:
        return

    text = update.message.text.strip()

    # Automatically initialize session if not in memory (seamless across restarts)
    if chat_id not in user_data:
        user_data[chat_id] = {
            "state": "waiting_for_id",
            "user_id": None,
        }

    state = user_data[chat_id]["state"]

    # -----------------------------------------------------
    # USER ID
    # -----------------------------------------------------

    if state == "waiting_for_id":

        if not text:

            await update.message.reply_text(
                "⚠️ Please send a valid User ID.",
                parse_mode="HTML",
            )

            return

        user_data[chat_id]["user_id"] = text
        user_data[chat_id]["state"] = "waiting_for_support"

        keyboard = [
            [
                InlineKeyboardButton(
                    "💬 CONTACT SUPPORT",
                    url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔄 CHANGE USER ID",
                    callback_data="change_id",
                )
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        message = (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>USER ID RECEIVED</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🆔 Your ID: <code>{text}</code>\n\n"
            "Your User ID has been CONNECTED TO PREDICTOR ✅ successfully.\n\n"
            "📸 <b>Next Step</b>\n\n"
            "If you need verification/support, "
            "contact our support account and send "
            "the required information there.\n\n"
            f"👤 <b>{SUPPORT_USERNAME}</b>"
        )

        await update.message.reply_text(
            message,
            parse_mode="HTML",
            reply_markup=reply_markup,
        )

        return

    # -----------------------------------------------------
    # SUPPORT STATE
    # -----------------------------------------------------

    if state == "waiting_for_support":

        keyboard = [
            [
                InlineKeyboardButton(
                    "💬 CONTACT SUPPORT",
                    url=f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🔄 CHANGE USER ID",
                    callback_data="change_id",
                )
            ],
        ]

        await update.message.reply_text(
            "ℹ️ <b>Your User ID is already received.</b>\n\n"
            "For further assistance, contact our support:",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

        return


# =========================================================
# CANCEL
# =========================================================

async def cancel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    chat_id = update.effective_chat.id

    user_data.pop(chat_id, None)

    await update.message.reply_text(
        "❌ <b>Session cancelled.</b>\n\n"
        "Send /start whenever you want to begin again.",
        parse_mode="HTML",
    )


# =========================================================
# HELP
# =========================================================

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if update.message is None:
        return

    await update.message.reply_text(
        "ℹ️ <b>HELP</b>\n\n"
        "1️⃣ Register using the registration button.\n"
        "2️⃣ Send your User ID here.\n"
        "3️⃣ Contact support if further assistance is required.\n\n"
        "Use /start to begin again.",
        parse_mode="HTML",
    )


# =========================================================
# ERROR HANDLER
# =========================================================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
):

    print(f"ERROR: {context.error}")


# =========================================================
# MAIN
# =========================================================

def main():

    # Start 24/7 cloud health check server
    threading.Thread(target=run_health_server, daemon=True).start()

    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN environment variable is not set.")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("cancel", cancel)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    app.add_handler(
        CallbackQueryHandler(
            promo_callback,
            pattern="^promo$",
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            guide_callback,
            pattern="^guide$",
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            change_id_callback,
            pattern="^change_id$",
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message,
        )
    )

    app.add_error_handler(error_handler)

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("      BOT IS RUNNING 24/7")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    app.run_polling(drop_pending_updates=False)


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    main()
