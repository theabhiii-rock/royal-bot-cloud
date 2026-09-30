import os
import re
import asyncio
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
import database

# =========================================================
# 24/7 CLOUD HEALTH CHECK SERVER
# =========================================================

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK - Royal Aviator VIP Bot is running 24/7!")

    def log_message(self, format, *args):
        return

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    try:
        server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
        server.serve_forever()
    except Exception as e:
        print(f"Health server notice: {e}")

# =========================================================
# CONFIG & MEMORY CACHE
# =========================================================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

REGISTRATION_LINK = "https://one-vv4926.com/?open=register&p=4ej1"
PROMO_CODE = "RBETKING"
SUPPORT_USERNAME = "@Royal_BetKing"
SUPPORT_URL = f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}"

# Session state & Telegram file_id cache for 0.05s instant photo delivery
user_data = {}
PHOTO_CACHE = {}


async def send_cached_photo(chat_id, context: ContextTypes.DEFAULT_TYPE, filename: str, caption: str, reply_markup=None):
    """Sends a photo using cached Telegram file_id for instant delivery, or uploads once and caches it."""
    if filename in PHOTO_CACHE:
        try:
            return await context.bot.send_photo(
                chat_id=chat_id,
                photo=PHOTO_CACHE[filename],
                caption=caption,
                parse_mode="HTML",
                reply_markup=reply_markup,
            )
        except Exception:
            PHOTO_CACHE.pop(filename, None)

    if os.path.exists(filename):
        with open(filename, "rb") as f:
            msg = await context.bot.send_photo(
                chat_id=chat_id,
                photo=f,
                caption=caption,
                parse_mode="HTML",
                reply_markup=reply_markup,
            )
            if msg and msg.photo:
                PHOTO_CACHE[filename] = msg.photo[-1].file_id
            return msg
    else:
        return await context.bot.send_message(
            chat_id=chat_id,
            text=caption,
            parse_mode="HTML",
            reply_markup=reply_markup,
        )


def get_main_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🚀 REGISTER ON 1WIN (+500% BONUS)",
                url=REGISTRATION_LINK,
            )
        ],
        [
            InlineKeyboardButton(
                "📖 STEP-BY-STEP REGISTRATION GUIDE",
                callback_data="guide",
            )
        ],
        [
            InlineKeyboardButton(
                "🎟️ COPY PROMO CODE",
                callback_data="promo",
            ),
            InlineKeyboardButton(
                "🆔 SUBMIT USER ID",
                callback_data="enter_id",
            ),
        ],
        [
            InlineKeyboardButton(
                "💬 24/7 VIP SUPPORT",
                url=SUPPORT_URL,
            )
        ],
    ])


def get_welcome_caption(first_name: str) -> str:
    return (
        "👑 <b>ROYAL AVIATOR PREDICTOR VIP</b> 👑\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👋 Welcome, <b>{first_name}</b>!\n\n"
        "Unlock <b>99.4% Accurate VIP Aviator Signals</b> & claim your <b>+500% Welcome Bonus</b> in 3 easy steps:\n\n"
        "1️⃣ <b>Register</b> a new 1win account using the button below\n"
        f"2️⃣ Enter Official Promo Code: <code>{PROMO_CODE}</code> <i>(Tap to copy)</i>\n"
        "3️⃣ Deposit & <b>send your 1win User ID</b> here to activate Predictor! 🚀\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🎁 <b>Bonus Code:</b> <code>{PROMO_CODE}</code> <i>(+500% First Deposit)</i>\n"
        "👇 <b>Tap a button below or send your 1win ID directly:</b>"
    )


# =========================================================
# START & MAIN MENU
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user
    first_name = (user.first_name if user else None) or "Champion"
    username = user.username if user else None

    user_data[chat_id] = {
        "state": "waiting_for_id",
        "user_id": None,
    }

    try:
        database.create_or_update_user(chat_id, username, first_name)
    except Exception as e:
        print(f"DB notice: {e}")

    if update.callback_query:
        await update.callback_query.answer()

    await send_cached_photo(
        chat_id=chat_id,
        context=context,
        filename="banner.jpg",
        caption=get_welcome_caption(first_name),
        reply_markup=get_main_keyboard(),
    )


# =========================================================
# PROMO BUTTON
# =========================================================

async def promo_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query is None:
        return
    await query.answer("Promo Code: RBETKING")

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🚀 REGISTER WITH PROMO CODE",
                url=REGISTRATION_LINK,
            )
        ],
        [
            InlineKeyboardButton(
                "📖 HOW TO APPLY CODE",
                callback_data="guide",
            ),
            InlineKeyboardButton(
                "🆔 SUBMIT USER ID",
                callback_data="enter_id",
            ),
        ],
    ])

    await query.message.reply_text(
        "🎟️ <b>OFFICIAL VIP PROMO CODE</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👉  <code>{PROMO_CODE}</code>  👈\n\n"
        "<i>(Tap the code above to copy it automatically!)</i>\n\n"
        "✅ <b>Benefits Included:</b>\n"
        "• <b>+500% Welcome Bonus</b> on your first deposit\n"
        "• <b>Instant Synchronization</b> with Royal Aviator Predictor\n"
        "• <b>Priority Fast Withdrawals</b> via UPI / Paytm / PhonePe",
        parse_mode="HTML",
        reply_markup=keyboard,
    )


# =========================================================
# ENTER ID PROMPT BUTTON
# =========================================================

async def enter_id_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        "🆔 <b>SEND YOUR 1WIN USER ID</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "Please type and send your <b>6 to 12 digit numeric 1win Account ID</b> below.\n\n"
        "📌 <i>Example:</i> <code>85492018</code>\n\n"
        "👇 <b>Type your User ID in the message box now:</b>",
        parse_mode="HTML",
    )


# =========================================================
# STEP-BY-STEP VISUAL GUIDE BUTTON
# =========================================================

async def guide_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query is None:
        return
    await query.answer("Loading HD Visual Guide...")

    chat_id = update.effective_chat.id

    steps = [
        (
            "step2.jpg",
            "📝 <b>STEP 1 OF 3: QUICK REGISTRATION</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Select <b>Indian Rupee (₹)</b> & enter your <b>Phone + Email</b>\n"
            f"② In Promo Code, enter: <code>{PROMO_CODE}</code> <i>(Required for +500% Bonus & Predictor Sync)</i>\n"
            "③ Tap the green <b>Register</b> button ✅",
            None,
        ),
        (
            "step3.jpg",
            "💳 <b>STEP 2 OF 3: CHOOSE LOCAL DEPOSIT METHOD</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Open the <b>Deposit</b> section at the top of the screen\n"
            "② Choose any fast Indian payment method:\n"
            "   • <b>PhonePe</b>  |  <b>Paytm</b>  |  <b>UPI</b>\n"
            "③ Recommended deposit for VIP Predictor: <b>₹500+</b>",
            None,
        ),
        (
            "step4.jpg",
            "✅ <b>STEP 3 OF 3: SUBMIT UTR & UNLOCK VIP</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Scan QR or copy the <b>VPA / UPI ID</b> to complete payment\n"
            "② Enter your <b>12-Digit UTR / Ref No.</b> and tap <b>Submit</b>\n"
            "③ Once done, <b>send your 1win User ID here</b> to unlock live VIP Predictor signals! 🚀",
            InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🚀 OPEN 1WIN & REGISTER NOW",
                        url=REGISTRATION_LINK,
                    )
                ],
                [
                    InlineKeyboardButton(
                        f"🎟️ PROMO: {PROMO_CODE}",
                        callback_data="promo",
                    ),
                    InlineKeyboardButton(
                        "🆔 SUBMIT USER ID",
                        callback_data="enter_id",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "💬 NEED HELP? ASK VIP SUPPORT",
                        url=SUPPORT_URL,
                    )
                ],
            ]),
        ),
    ]

    for filename, caption, markup in steps:
        await send_cached_photo(
            chat_id=chat_id,
            context=context,
            filename=filename,
            caption=caption,
            reply_markup=markup,
        )


# =========================================================
# CHANGE ID BUTTON
# =========================================================

async def change_id_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query is None:
        return
    await query.answer()

    chat_id = update.effective_chat.id
    user_data[chat_id] = {
        "state": "waiting_for_id",
        "user_id": None,
    }
    try:
        database.update_state(chat_id, "waiting_for_id")
    except Exception:
        pass

    await query.message.reply_text(
        "🔄 <b>CHANGE 1WIN USER ID</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "Please send your new <b>numeric 1win Account ID</b> (6–12 digits) below 👇",
        parse_mode="HTML",
    )


# =========================================================
# MESSAGE HANDLER (SMART ID VALIDATION & VERIFICATION)
# =========================================================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or not update.message.text:
        return

    chat_id = update.effective_chat.id
    raw_text = update.message.text.strip()

    if chat_id not in user_data:
        user_data[chat_id] = {
            "state": "waiting_for_id",
            "user_id": None,
        }

    # Extract digits if user typed "ID: 85492018" or "#85492018"
    cleaned = re.sub(r"^(id|user\s*id|1win\s*id|account\s*id)[\s:#\-]*", "", raw_text, flags=re.IGNORECASE).strip()
    digits_only = re.sub(r"\s+", "", cleaned)

    # Validate: A genuine 1win User ID is 6 to 12 digits
    if not re.fullmatch(r"\d{6,12}", digits_only):
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🚀 REGISTER ON 1WIN (+500% BONUS)",
                    url=REGISTRATION_LINK,
                )
            ],
            [
                InlineKeyboardButton(
                    "📖 HOW TO REGISTER & DEPOSIT",
                    callback_data="guide",
                )
            ],
            [
                InlineKeyboardButton(
                    "🎟️ PROMO CODE",
                    callback_data="promo",
                ),
                InlineKeyboardButton(
                    "💬 VIP SUPPORT",
                    url=SUPPORT_URL,
                ),
            ],
        ])

        await update.message.reply_text(
            "⚠️ <b>INVALID 1WIN USER ID</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            f"You sent: <code>{raw_text[:30]}</code>\n\n"
            "Please send a valid <b>6 to 12 digit numeric 1win Account ID</b> (for example: <code>85492018</code>).\n\n"
            f"💡 <i>Don't have a 1win account yet? Register below using Promo Code</i> <code>{PROMO_CODE}</code> <i>and send your new ID here!</i>",
            parse_mode="HTML",
            reply_markup=keyboard,
        )
        return

    # Valid 6-12 digit 1win ID received!
    user_id = digits_only
    user_data[chat_id]["user_id"] = user_id
    user_data[chat_id]["state"] = "waiting_for_support"

    try:
        user = update.effective_user
        database.create_or_update_user(
            chat_id,
            user.username if user else None,
            (user.first_name if user else None) or "User",
        )
        database.update_user_id(chat_id, user_id)
    except Exception as e:
        print(f"DB update notice: {e}")

    # Pro live verification step
    status_msg = await update.message.reply_text(
        "🔄 <b>Connecting to 1win Predictor Server...</b>\n"
        f"🔍 Verifying Account ID: <code>{user_id}</code>",
        parse_mode="HTML",
    )
    await asyncio.sleep(1.0)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "👑 ACTIVATE VIP SIGNALS (MESSAGE SUPPORT)",
                url=SUPPORT_URL,
            )
        ],
        [
            InlineKeyboardButton(
                "💳 DEPOSIT GUIDE",
                callback_data="guide",
            ),
            InlineKeyboardButton(
                "🔄 CHANGE USER ID",
                callback_data="change_id",
            ),
        ],
        [
            InlineKeyboardButton(
                "🏠 MAIN MENU",
                callback_data="main_menu",
            )
        ],
    ])

    verified_message = (
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "✅ <b>VIP PREDICTOR CONNECTED!</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🆔 <b>1win Account ID:</b> <code>{user_id}</code>\n"
        f"🎟️ <b>Promo Code Tag:</b> <code>{PROMO_CODE}</code> ✅\n"
        "📡 <b>Predictor Server:</b> <code>CONNECTED (v4.2 VIP)</code>\n"
        "🎁 <b>Bonus Status:</b> <b>+500% Active</b>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🚀 <b>FINAL STEP TO UNLOCK SIGNALS:</b>\n\n"
        "Tap <b>ACTIVATE VIP SIGNALS</b> below and send your <b>1win ID & Deposit Screenshot</b> to our VIP Support Manager to start playing! 👇\n\n"
        f"👤 <b>VIP Manager:</b> {SUPPORT_USERNAME}"
    )

    try:
        await status_msg.edit_text(
            verified_message,
            parse_mode="HTML",
            reply_markup=keyboard,
        )
    except Exception:
        await update.message.reply_text(
            verified_message,
            parse_mode="HTML",
            reply_markup=keyboard,
        )


# =========================================================
# CANCEL & HELP & STATS
# =========================================================

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return
    chat_id = update.effective_chat.id
    user_data.pop(chat_id, None)
    await update.message.reply_text(
        "🔄 <b>Session Reset!</b>\n\nTap /start to return to the Main Menu.",
        parse_mode="HTML",
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return
    await update.message.reply_text(
        "👑 <b>ROYAL AVIATOR VIP — HELP CENTER</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "1️⃣ Tap <b>REGISTER ON 1WIN</b> to create your official account.\n"
        f"2️⃣ Use Promo Code <code>{PROMO_CODE}</code> for <b>+500% Bonus</b>.\n"
        "3️⃣ Deposit via <b>UPI / Paytm / PhonePe</b> & submit your 12-digit UTR.\n"
        "4️⃣ Send your <b>6–12 digit 1win ID</b> here to connect with Predictor.\n"
        f"5️⃣ Contact {SUPPORT_USERNAME} for live VIP signals!\n\n"
        "Tap /start to open the Main Menu.",
        parse_mode="HTML",
        reply_markup=get_main_keyboard(),
    )


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return
    try:
        conn = database.get_connection()
        total = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        with_id = conn.execute("SELECT COUNT(*) FROM users WHERE user_id IS NOT NULL").fetchone()[0]
        recent = conn.execute(
            "SELECT first_name, telegram_username, user_id FROM users WHERE user_id IS NOT NULL ORDER BY updated_at DESC LIMIT 10"
        ).fetchall()
        conn.close()

        lines = [
            "📊 <b>BOT LIVE STATISTICS</b>",
            "━━━━━━━━━━━━━━━━━━━━━━",
            f"👥 <b>Total Users Started:</b> <code>{total}</code>",
            f"✅ <b>Verified IDs Submitted:</b> <code>{with_id}</code>\n",
            "🕒 <b>Recent Submissions:</b>",
        ]
        if recent:
            for r in recent:
                uname = f"@{r['telegram_username']}" if r["telegram_username"] else r["first_name"]
                lines.append(f"• {uname} — <code>{r['user_id']}</code>")
        else:
            lines.append("<i>No IDs submitted yet in this cycle.</i>")

        await update.message.reply_text("\n".join(lines), parse_mode="HTML")
    except Exception as e:
        await update.message.reply_text(f"Stats error: {e}")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"ERROR: {context.error}")


# =========================================================
# MAIN
# =========================================================

def main():
    database.init_db()

    # Start 24/7 cloud health check server
    threading.Thread(target=run_health_server, daemon=True).start()

    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN environment variable is not set.")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats_command))

    app.add_handler(CallbackQueryHandler(start, pattern="^main_menu$"))
    app.add_handler(CallbackQueryHandler(promo_callback, pattern="^promo$"))
    app.add_handler(CallbackQueryHandler(guide_callback, pattern="^guide$"))
    app.add_handler(CallbackQueryHandler(enter_id_callback, pattern="^enter_id$"))
    app.add_handler(CallbackQueryHandler(change_id_callback, pattern="^change_id$"))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("  ROYAL VIP BOT RUNNING 24/7")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    app.run_polling(drop_pending_updates=False)


if __name__ == "__main__":
    main()
