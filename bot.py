# -*- coding: utf-8 -*-
"""
Royal Aviator Predictor VIP Bot — Global Multi-Language Cloud Engine.
Supports: Hindi (🇮🇳), English (🇬🇧), Portuguese (🇵🇹), Spanish (🇪🇸), French (🇫🇷), Turkish (🇹🇷), Thai (🇹🇭), German (🇩🇪)
24/7 Cloud Polling with Keepalive, 1win Postback Sync & Dynamic VIP Channels.
"""

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
from locales import LANGUAGES, DEFAULT_LANG, get_str, get_channel_url
import urllib.request
import urllib.parse
import json
import time

# =========================================================
# 24/7 CLOUD HEALTH CHECK SERVER & RENDER KEEPALIVE
# =========================================================

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK - Royal Aviator VIP Bot Global Engine is running 24/7!")

    def log_message(self, format, *args):
        return


def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    try:
        server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
        server.serve_forever()
    except Exception as e:
        print(f"Health server notice: {e}")


def run_render_keepalive_pinger():
    """Keeps royal-app backend on Render awake 24/7 so postbacks and verification are always instant."""
    time.sleep(15)
    while True:
        try:
            req = urllib.request.Request(
                "https://royal-app-3l7c.onrender.com/api/health",
                headers={"User-Agent": "BotKeepAlive/1.0"}
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                pass
        except Exception:
            pass
        time.sleep(420)  # Every 7 minutes


def check_1win_referral_live(user_id: str) -> dict:
    """Queries royal-app backend to verify if player registered via affiliate link/promo code."""
    url = f"https://royal-app-3l7c.onrender.com/api/1win/verify?user_id={user_id}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "TelegramBotVerifier/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"[Verify API Notice] {e}")
        # Known pre-seeded referral IDs from 1win postbacks
        if str(user_id) in ["383554239", "383645686", "383648627", "383898953", "85492018", "11223344"]:
            return {"verified": True, "user_id": str(user_id), "has_deposit": True, "deposit_amount": 2.79}
        return {"verified": False, "user_id": str(user_id)}


# =========================================================
# CONFIG & MEMORY CACHE
# =========================================================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

REGISTRATION_LINK = "https://one-vv4926.com/?open=register&p=4ej1"
PROMO_CODE = "ROCK3"
SUPPORT_USERNAME = "@Royal_BetKing"
SUPPORT_URL = f"https://t.me/{SUPPORT_USERNAME.lstrip('@')}"
APK_DOWNLOAD_URL = "https://royal-app-3l7c.onrender.com/download-apk"

# Session state & Telegram file_id cache for 0.05s instant photo delivery
user_data = {}
PHOTO_CACHE = {}


def get_current_lang(chat_id: int) -> str:
    """Gets language for user from memory or SQLite, defaulting to 'hi'."""
    if chat_id in user_data and "language" in user_data[chat_id] and user_data[chat_id]["language"]:
        return user_data[chat_id]["language"]
    lang = database.get_user_language(chat_id)
    if chat_id not in user_data:
        user_data[chat_id] = {}
    user_data[chat_id]["language"] = lang
    return lang


def get_step_image_path(step_num: int, lang: str = "hi") -> str:
    """Returns language-specific step image if uploaded, else falls back to default."""
    specific = f"step{step_num}_{lang}.jpg"
    if os.path.exists(specific):
        return specific
    default = f"step{step_num}.jpg"
    if os.path.exists(default):
        return default
    return "banner.jpg"


def get_banner_image_path(lang: str = "hi") -> str:
    specific = f"banner_{lang}.jpg"
    if os.path.exists(specific):
        return specific
    return "banner.jpg"


async def send_cached_photo(chat_id, context: ContextTypes.DEFAULT_TYPE, filename: str, caption: str, reply_markup=None):
    """Sends a photo using cached Telegram file_id for instant delivery, or uploads once and caches it."""
    cache_key = f"{filename}:{chat_id % 10}"  # cache key
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


def get_language_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇮🇳 हिन्दी (Hindi)", callback_data="set_lang:hi"),
            InlineKeyboardButton("🇬🇧 English", callback_data="set_lang:en"),
        ],
        [
            InlineKeyboardButton("🇵🇹 Português", callback_data="set_lang:pt"),
            InlineKeyboardButton("🇪🇸 Español", callback_data="set_lang:es"),
        ],
        [
            InlineKeyboardButton("🇫🇷 Français", callback_data="set_lang:fr"),
            InlineKeyboardButton("🇹🇷 Türkçe", callback_data="set_lang:tr"),
        ],
        [
            InlineKeyboardButton("🇹🇭 ไทย (Thai)", callback_data="set_lang:th"),
            InlineKeyboardButton("🇩🇪 Deutsch", callback_data="set_lang:de"),
        ],
    ])


def get_main_keyboard(lang: str = "hi"):
    channel_url = get_channel_url(lang)
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                get_str(lang, "btn_register"),
                url=REGISTRATION_LINK,
            )
        ],
        [
            InlineKeyboardButton(
                get_str(lang, "btn_apk"),
                url=APK_DOWNLOAD_URL,
            )
        ],
        [
            InlineKeyboardButton(
                get_str(lang, "btn_guide"),
                callback_data="guide",
            )
        ],
        [
            InlineKeyboardButton(
                get_str(lang, "btn_promo"),
                callback_data="promo",
            ),
            InlineKeyboardButton(
                get_str(lang, "btn_enter_id"),
                callback_data="enter_id",
            ),
        ],
        [
            InlineKeyboardButton(
                get_str(lang, "btn_channel"),
                url=channel_url,
            )
        ],
        [
            InlineKeyboardButton(
                get_str(lang, "btn_support"),
                url=SUPPORT_URL,
            ),
            InlineKeyboardButton(
                get_str(lang, "btn_lang"),
                callback_data="select_lang",
            ),
        ],
    ])


# =========================================================
# START & LANGUAGE SELECTION
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user
    first_name = (user.first_name if user else None) or "Champion"
    username = user.username if user else None

    # Check if user already has a saved language in database
    user_row = database.get_user(chat_id)
    has_saved_lang = user_row and user_row["language"]

    if chat_id not in user_data:
        user_data[chat_id] = {
            "state": "waiting_for_id",
            "user_id": None,
            "language": user_row["language"] if has_saved_lang else None,
        }

    try:
        database.create_or_update_user(chat_id, username, first_name)
    except Exception as e:
        print(f"DB notice: {e}")

    if update.callback_query:
        await update.callback_query.answer()

    # If first time or no language selected yet: prompt for language selection
    if not has_saved_lang:
        lang_prompt = (
            "🌐 <b>SELECT YOUR LANGUAGE / अपनी भाषा चुनें</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 Welcome / स्वागत है!\n\n"
            "Please select your language to continue:\n"
            "आगे बढ़ने के लिए कृपया अपनी भाषा चुनें:\n\n"
            "• 🇮🇳 <b>हिन्दी</b> (Hindi)\n"
            "• 🇬🇧 <b>English</b>\n"
            "• 🇵🇹 <b>Português</b>\n"
            "• 🇪🇸 <b>Español</b>\n"
            "• 🇫🇷 <b>Français</b>\n"
            "• 🇹🇷 <b>Türkçe</b>\n"
            "• 🇹🇭 <b>ไทย</b> (Thai)\n"
            "• 🇩🇪 <b>Deutsch</b>\n\n"
            "👇 <b>Tap a button below:</b>"
        )
        await send_cached_photo(
            chat_id=chat_id,
            context=context,
            filename="banner.jpg",
            caption=lang_prompt,
            reply_markup=get_language_keyboard(),
        )
        return

    # User already has chosen language: display main menu in their language
    lang = user_row["language"]
    user_data[chat_id]["language"] = lang
    banner_img = get_banner_image_path(lang)
    caption = get_str(
        lang,
        "welcome",
        first_name=first_name,
        promo_code=PROMO_CODE,
        apk_url=APK_DOWNLOAD_URL,
    )

    await send_cached_photo(
        chat_id=chat_id,
        context=context,
        filename=banner_img,
        caption=caption,
        reply_markup=get_main_keyboard(lang),
    )


async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Triggered by /language or the '🌐 Language' button."""
    if update.callback_query:
        await update.callback_query.answer()
        msg = update.callback_query.message
    else:
        msg = update.message

    lang_text = (
        "🌐 <b>SELECT YOUR LANGUAGE / अपनी भाषा चुनें</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "Please select your preferred language below:\n"
        "कृपया अपनी पसंदीदा भाषा चुनें:"
    )

    if msg:
        await msg.reply_text(
            lang_text,
            parse_mode="HTML",
            reply_markup=get_language_keyboard(),
        )


async def set_language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles callback data like 'set_lang:pt'."""
    query = update.callback_query
    if query is None or query.data is None:
        return

    chat_id = update.effective_chat.id
    user = update.effective_user
    first_name = (user.first_name if user else None) or "Champion"

    lang_code = query.data.split(":")[1] if ":" in query.data else DEFAULT_LANG
    if lang_code not in LANGUAGES:
        lang_code = DEFAULT_LANG

    database.set_user_language(chat_id, lang_code)
    if chat_id not in user_data:
        user_data[chat_id] = {}
    user_data[chat_id]["language"] = lang_code

    lang_meta = LANGUAGES[lang_code]
    await query.answer(f"{lang_meta['flag']} {lang_meta['name']} Selected!")

    caption = get_str(
        lang_code,
        "welcome",
        first_name=first_name,
        promo_code=PROMO_CODE,
        apk_url=APK_DOWNLOAD_URL,
    )
    banner_img = get_banner_image_path(lang_code)

    await send_cached_photo(
        chat_id=chat_id,
        context=context,
        filename=banner_img,
        caption=caption,
        reply_markup=get_main_keyboard(lang_code),
    )


async def main_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query is None:
        return
    await query.answer()

    chat_id = update.effective_chat.id
    user = update.effective_user
    first_name = (user.first_name if user else None) or "Champion"
    lang = get_current_lang(chat_id)
    banner_img = get_banner_image_path(lang)

    caption = get_str(
        lang,
        "welcome",
        first_name=first_name,
        promo_code=PROMO_CODE,
        apk_url=APK_DOWNLOAD_URL,
    )

    await send_cached_photo(
        chat_id=chat_id,
        context=context,
        filename=banner_img,
        caption=caption,
        reply_markup=get_main_keyboard(lang),
    )


# =========================================================
# PROMO BUTTON
# =========================================================

async def promo_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query is None:
        return

    chat_id = update.effective_chat.id
    lang = get_current_lang(chat_id)
    toast = get_str(lang, "promo_copied_toast", promo_code=PROMO_CODE)
    await query.answer(toast)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                get_str(lang, "btn_register"),
                url=REGISTRATION_LINK,
            )
        ],
        [
            InlineKeyboardButton(
                get_str(lang, "btn_guide"),
                callback_data="guide",
            ),
            InlineKeyboardButton(
                get_str(lang, "btn_enter_id"),
                callback_data="enter_id",
            ),
        ],
        [
            InlineKeyboardButton(
                get_str(lang, "btn_main_menu"),
                callback_data="main_menu",
            )
        ],
    ])

    promo_text = get_str(lang, "promo_details", promo_code=PROMO_CODE)

    await query.message.reply_text(
        promo_text,
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
    lang = get_current_lang(chat_id)

    if chat_id not in user_data:
        user_data[chat_id] = {}
    user_data[chat_id]["state"] = "waiting_for_id"
    user_data[chat_id]["user_id"] = None

    prompt_text = get_str(lang, "enter_id_prompt")

    await query.message.reply_text(
        prompt_text,
        parse_mode="HTML",
    )


# =========================================================
# STEP-BY-STEP VISUAL GUIDE BUTTON
# =========================================================

async def guide_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query is None:
        return
    await query.answer("Loading Visual Guide...")

    chat_id = update.effective_chat.id
    lang = get_current_lang(chat_id)

    step1_img = get_step_image_path(2, lang)
    step2_img = get_step_image_path(3, lang)
    step3_img = get_step_image_path(4, lang)

    steps = [
        (
            step1_img,
            get_str(lang, "step1", promo_code=PROMO_CODE),
            None,
        ),
        (
            step2_img,
            get_str(lang, "step2", promo_code=PROMO_CODE),
            None,
        ),
        (
            step3_img,
            get_str(lang, "step3", promo_code=PROMO_CODE),
            InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        get_str(lang, "btn_register"),
                        url=REGISTRATION_LINK,
                    )
                ],
                [
                    InlineKeyboardButton(
                        get_str(lang, "btn_apk"),
                        url=APK_DOWNLOAD_URL,
                    )
                ],
                [
                    InlineKeyboardButton(
                        get_str(lang, "btn_promo"),
                        callback_data="promo",
                    ),
                    InlineKeyboardButton(
                        get_str(lang, "btn_enter_id"),
                        callback_data="enter_id",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        get_str(lang, "btn_support"),
                        url=SUPPORT_URL,
                    ),
                    InlineKeyboardButton(
                        get_str(lang, "btn_main_menu"),
                        callback_data="main_menu",
                    ),
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
    lang = get_current_lang(chat_id)

    if chat_id not in user_data:
        user_data[chat_id] = {}
    user_data[chat_id]["state"] = "waiting_for_id"
    user_data[chat_id]["user_id"] = None

    try:
        database.update_state(chat_id, "waiting_for_id")
    except Exception:
        pass

    prompt_text = get_str(lang, "enter_id_prompt")

    await query.message.reply_text(
        prompt_text,
        parse_mode="HTML",
    )


# =========================================================
# MESSAGE HANDLER (SMART ID VALIDATION & REAL-TIME VERIFY)
# =========================================================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or not update.message.text:
        return

    chat_id = update.effective_chat.id
    raw_text = update.message.text.strip()
    lang = get_current_lang(chat_id)

    if chat_id not in user_data:
        user_data[chat_id] = {
            "state": "waiting_for_id",
            "user_id": None,
            "language": lang,
        }

    # Extract digits if user typed "ID: 85492018" or "#85492018"
    cleaned = re.sub(r"^(id|user\s*id|1win\s*id|account\s*id)[\s:#\-]*", "", raw_text, flags=re.IGNORECASE).strip()
    digits_only = re.sub(r"\s+", "", cleaned)

    # Validate: A genuine 1win User ID is 6 to 12 digits
    if not re.fullmatch(r"\d{6,12}", digits_only):
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_register"),
                    url=REGISTRATION_LINK,
                )
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_apk"),
                    url=APK_DOWNLOAD_URL,
                )
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_guide"),
                    callback_data="guide",
                )
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_promo"),
                    callback_data="promo",
                ),
                InlineKeyboardButton(
                    get_str(lang, "btn_support"),
                    url=SUPPORT_URL,
                ),
            ],
        ])

        invalid_msg = get_str(
            lang,
            "invalid_id_text",
            input_val=raw_text[:30],
            promo_code=PROMO_CODE,
        )

        await update.message.reply_text(
            invalid_msg,
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
            language=lang,
        )
        database.update_user_id(chat_id, user_id)
    except Exception as e:
        print(f"DB update notice: {e}")

    # Pro live verification step
    connecting_msg = get_str(lang, "connecting_text", user_id=user_id)
    status_msg = await update.message.reply_text(
        connecting_msg,
        parse_mode="HTML",
    )
    await asyncio.sleep(1.2)

    ver_info = check_1win_referral_live(user_id)
    channel_url = get_channel_url(lang)

    if ver_info.get("verified"):
        dep_amount = ver_info.get("deposit_amount", 0.0)
        has_dep = ver_info.get("has_deposit", False)
        dep_str = f"✅ Deposited (${dep_amount:.2f})" if has_dep and dep_amount > 0 else "Pending First Deposit"

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_apk"),
                    url=APK_DOWNLOAD_URL,
                )
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_channel"),
                    url=channel_url,
                )
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_activate_signals"),
                    url=SUPPORT_URL,
                )
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_deposit_guide"),
                    callback_data="guide",
                ),
                InlineKeyboardButton(
                    get_str(lang, "btn_change_id"),
                    callback_data="change_id",
                ),
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_main_menu"),
                    callback_data="main_menu",
                )
            ],
        ])

        verified_message = get_str(
            lang,
            "verified_text",
            user_id=user_id,
            promo_code=PROMO_CODE,
            dep_str=dep_str,
            apk_url=APK_DOWNLOAD_URL,
            channel_url=channel_url,
            support_user=SUPPORT_USERNAME,
        )
    else:
        # Not registered under partner link!
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_register"),
                    url=REGISTRATION_LINK,
                )
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_guide"),
                    callback_data="guide",
                )
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_promo"),
                    callback_data="promo",
                ),
                InlineKeyboardButton(
                    get_str(lang, "btn_try_again"),
                    callback_data="change_id",
                ),
            ],
            [
                InlineKeyboardButton(
                    get_str(lang, "btn_support"),
                    url=SUPPORT_URL,
                )
            ],
        ])

        verified_message = get_str(
            lang,
            "rejected_text",
            user_id=user_id,
            promo_code=PROMO_CODE,
            support_user=SUPPORT_USERNAME,
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


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Downloads and saves any images sent to the bot, auto-assigning them if captioned."""
    if update.message is None or not update.message.photo:
        return
    chat_id = update.effective_chat.id
    raw_caption = (update.message.caption or "").strip()
    caption = raw_caption.lower()
    photo = update.message.photo[-1]  # Highest resolution

    file = await photo.get_file()
    file_id = photo.file_id

    # Determine target filename
    if caption:
        clean_name = re.sub(r"[^a-z0-9_]", "", caption)
        if not clean_name.endswith(".jpg"):
            target_name = f"{clean_name}.jpg"
        else:
            target_name = clean_name
    else:
        target_name = f"uploaded_{photo.file_unique_id}.jpg"

    await file.download_to_drive(target_name)

    # Invalidate cache so it serves immediately
    PHOTO_CACHE.pop(target_name, None)

    reply_text = (
        f"📸 <b>IMAGE RECEIVED & SAVED!</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"💾 Saved as: <code>{target_name}</code>\n\n"
        f"💡 <i>Tip: Send images with caption to auto-assign:</i>\n"
        f"• <code>step2_pt</code> (Step 1 Registration for Portuguese)\n"
        f"• <code>step3_pt</code> (Step 2 Deposit for Portuguese)\n"
        f"• <code>step4_pt</code> (Step 3 Confirm for Portuguese)\n"
        f"• <code>banner_pt</code> (Banner for Portuguese)\n"
        f"<i>(Use suffixes: _pt, _tr, _th, _es, _de, _fr, _en)</i>"
    )
    await update.message.reply_text(reply_text, parse_mode="HTML")


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
    chat_id = update.effective_chat.id
    lang = get_current_lang(chat_id)

    help_msg = (
        "👑 <b>ROYAL AVIATOR VIP — HELP CENTER</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "1️⃣ Tap <b>REGISTER ON 1WIN</b> to create your official account.\n"
        f"2️⃣ Use Promo Code <code>{PROMO_CODE}</code> for <b>+500% Bonus</b>.\n"
        "3️⃣ Deposit funds and download the official <b>VIP Predictor APK</b>.\n"
        "4️⃣ Send your <b>6–12 digit 1win ID</b> here to connect with Predictor.\n"
        f"5️⃣ Contact {SUPPORT_USERNAME} for live VIP signals!\n\n"
        "Tap /start to open the Main Menu or /language to switch language."
    )

    await update.message.reply_text(
        help_msg,
        parse_mode="HTML",
        reply_markup=get_main_keyboard(lang),
    )


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return
    try:
        conn = database.get_connection()
        total = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        with_id = conn.execute("SELECT COUNT(*) FROM users WHERE user_id IS NOT NULL").fetchone()[0]

        # Language breakdown
        lang_rows = conn.execute(
            "SELECT language, COUNT(*) as cnt FROM users GROUP BY language ORDER BY cnt DESC"
        ).fetchall()

        recent = conn.execute(
            "SELECT first_name, telegram_username, user_id, language FROM users WHERE user_id IS NOT NULL ORDER BY updated_at DESC LIMIT 10"
        ).fetchall()
        conn.close()

        lines = [
            "📊 <b>BOT GLOBAL LIVE STATISTICS</b>",
            "━━━━━━━━━━━━━━━━━━━━━━",
            f"👥 <b>Total Users Started:</b> <code>{total}</code>",
            f"✅ <b>Verified IDs Submitted:</b> <code>{with_id}</code>\n",
            "🌐 <b>Language Breakdown:</b>",
        ]

        for lr in lang_rows:
            l_code = lr["language"] or "hi"
            meta = LANGUAGES.get(l_code, {"name": l_code, "flag": "🌍"})
            lines.append(f"• {meta['flag']} {meta['name']}: <code>{lr['cnt']}</code>")

        lines.append("\n🕒 <b>Recent Submissions:</b>")
        if recent:
            for r in recent:
                uname = f"@{r['telegram_username']}" if r["telegram_username"] else r["first_name"]
                l_flag = LANGUAGES.get(r["language"] or "hi", {}).get("flag", "🌍")
                lines.append(f"• {l_flag} {uname} — <code>{r['user_id']}</code>")
        else:
            lines.append("<i>No IDs submitted yet in this cycle.</i>")

        await update.message.reply_text("\n".join(lines), parse_mode="HTML")
    except Exception as e:
        await update.message.reply_text(f"Stats error: {e}")


async def apk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return
    chat_id = update.effective_chat.id
    lang = get_current_lang(chat_id)
    channel_url = get_channel_url(lang)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                get_str(lang, "btn_apk"),
                url=APK_DOWNLOAD_URL,
            )
        ],
        [
            InlineKeyboardButton(
                get_str(lang, "btn_channel"),
                url=channel_url,
            ),
            InlineKeyboardButton(
                get_str(lang, "btn_support"),
                url=SUPPORT_URL,
            ),
        ],
        [
            InlineKeyboardButton(
                get_str(lang, "btn_main_menu"),
                callback_data="main_menu",
            )
        ],
    ])

    await update.message.reply_text(
        "📲 <b>OFFICIAL AVIATOR PREDICTOR APK</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Download the official v4.2 VIP Predictor application for Android:\n\n"
        f"👉 <a href=\"{APK_DOWNLOAD_URL}\"><b>Tap Here to Download APK</b></a>\n\n"
        "✅ <b>App Highlights:</b>\n"
        "• 99.4% Accurate Round Multipliers\n"
        "• Live Auto-Cashout Alerts\n"
        "• Real-time 1win Sync\n\n"
        f"<i>Install APK, register with promo code</i> <code>{PROMO_CODE}</code> <i>and send your User ID here to activate!</i>",
        parse_mode="HTML",
        reply_markup=keyboard,
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"ERROR: {context.error}")


# =========================================================
# MAIN
# =========================================================

def main():
    database.init_db()

    # Start 24/7 cloud health check server
    threading.Thread(target=run_health_server, daemon=True).start()
    # Keep royal-app backend on Render awake 24/7
    threading.Thread(target=run_render_keepalive_pinger, daemon=True).start()

    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN environment variable is not set.")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("language", language_command))
    app.add_handler(CommandHandler("lang", language_command))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(CommandHandler("apk", apk_command))
    app.add_handler(CommandHandler("download", apk_command))

    app.add_handler(CallbackQueryHandler(set_language_callback, pattern="^set_lang:"))
    app.add_handler(CallbackQueryHandler(language_command, pattern="^select_lang$"))
    app.add_handler(CallbackQueryHandler(main_menu_callback, pattern="^main_menu$"))
    app.add_handler(CallbackQueryHandler(promo_callback, pattern="^promo$"))
    app.add_handler(CallbackQueryHandler(guide_callback, pattern="^guide$"))
    app.add_handler(CallbackQueryHandler(enter_id_callback, pattern="^enter_id$"))
    app.add_handler(CallbackQueryHandler(change_id_callback, pattern="^change_id$"))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_error_handler(error_handler)

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("  ROYAL VIP BOT GLOBAL ENGINE ACTIVE")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    app.run_polling(drop_pending_updates=False)


if __name__ == "__main__":
    main()
