# -*- coding: utf-8 -*-
"""
Multi-Language Localization for Royal Aviator Predictor VIP Bot.
Supports: Hindi (🇮🇳), English (🇬🇧), Portuguese (🇵🇹), Spanish (🇪🇸), French (🇫🇷), Turkish (🇹🇷), Thai (🇹🇭), German (🇩🇪)
"""

LANGUAGES = {
    "hi": {
        "code": "hi",
        "name": "हिन्दी (Hindi)",
        "flag": "🇮🇳",
        "channel": "https://t.me/Royal_Bet_King",
    },
    "en": {
        "code": "en",
        "name": "English",
        "flag": "🇬🇧",
        "channel": "https://t.me/Royal_Bet_King",
    },
    "pt": {
        "code": "pt",
        "name": "Português",
        "flag": "🇵🇹",
        "channel": "https://t.me/Royal_Bet_King2",
    },
    "es": {
        "code": "es",
        "name": "Español",
        "flag": "🇪🇸",
        "channel": "https://t.me/Royal_Bet_King5",
    },
    "fr": {
        "code": "fr",
        "name": "Français",
        "flag": "🇫🇷",
        "channel": "https://t.me/Royal_Bet_King",
    },
    "tr": {
        "code": "tr",
        "name": "Türkçe",
        "flag": "🇹🇷",
        "channel": "https://t.me/Royal_Bet_King3",
    },
    "th": {
        "code": "th",
        "name": "ไทย (Thai)",
        "flag": "🇹🇭",
        "channel": "https://t.me/Royal_Bet_King4",
    },
    "de": {
        "code": "de",
        "name": "Deutsch",
        "flag": "🇩🇪",
        "channel": "https://t.me/Royal_Bet_King6",
    },
    "zh": {
        "code": "zh",
        "name": "中文 (Mandarin)",
        "flag": "🇨🇳",
        "channel": "https://t.me/Royal_Bet_King7",
    },
}

DEFAULT_LANG = "hi"


def get_channel_url(lang: str) -> str:
    return LANGUAGES.get(lang, LANGUAGES[DEFAULT_LANG])["channel"]


STRINGS = {
    "hi": {
        "lang_name": "हिन्दी",
        "welcome": (
            "👑 <b>ROYAL AVIATOR PREDICTOR VIP</b> 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 Swagat hai, <b>{first_name}</b>!\n\n"
            "Unlock karein <b>99.4% Accurate VIP Aviator Signals</b> aur paayein <b>+500% Welcome Bonus</b> 3 aasan steps me:\n\n"
            "1️⃣ Neeche diye button se naya 1win account <b>Register</b> karein\n"
            "2️⃣ Promo Code daalein: <code>{promo_code}</code> <i>(Tap karke copy karein)</i>\n"
            "3️⃣ Deposit karein, <b>Aviator Predictor APK</b> download karein aur apni 1win ID bhej kar activate karein! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 <b>Bonus Code:</b> <code>{promo_code}</code> <i>(+500% First Deposit)</i>\n"
            "📲 <b>Predictor App:</b> <a href=\"{apk_url}\">Download APK</a>\n"
            "👇 <b>Neeche diye button par tap karein ya apni 1win ID yahan bhejein:</b>"
        ),
        "btn_register": "🚀 REGISTER ON 1WIN (+500% BONUS)",
        "btn_apk": "📲 DOWNLOAD PREDICTOR APK",
        "btn_guide": "📖 STEP-BY-STEP GUIDE",
        "btn_promo": "🎟️ COPY PROMO CODE",
        "btn_enter_id": "🆔 SUBMIT 1WIN ID",
        "btn_channel": "📢 OFFICIAL VIP CHANNEL",
        "btn_support": "💬 24/7 VIP SUPPORT",
        "btn_lang": "🌐 LANGUAGE / भाषा",
        "btn_change_id": "🔄 CHANGE ID",
        "btn_main_menu": "🏠 MAIN MENU",
        "btn_try_again": "🔄 TRY AGAIN",
        "btn_activate_signals": "👑 ACTIVATE VIP SIGNALS (SUPPORT)",
        "btn_deposit_guide": "💳 DEPOSIT GUIDE",
        "promo_copied_toast": "Promo Code: {promo_code} (Copied!)",
        "promo_details": (
            "🎟️ <b>OFFICIAL VIP PROMO CODE</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👉  <code>{promo_code}</code>  👈\n\n"
            "<i>(Code par tap karke ise copy karein!)</i>\n\n"
            "✅ <b>Faayde (Benefits):</b>\n"
            "• <b>+500% Welcome Bonus</b> aapke pehle deposit par\n"
            "• <b>Royal Aviator Predictor</b> ke sath instant sync\n"
            "• <b>Fast Priority Withdrawals</b> via UPI / Paytm / PhonePe"
        ),
        "enter_id_prompt": (
            "🆔 <b>SEND YOUR 1WIN USER ID</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Kripya apni <b>6 se 12 digit ki 1win Account ID</b> yahan type karke bhejein.\n\n"
            "📌 <i>Udaharan:</i> <code>85492018</code>\n\n"
            "👇 <b>Apni User ID abhi niche message box me likhein:</b>"
        ),
        "invalid_id_text": (
            "⚠️ <b>INVALID 1WIN USER ID</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Aapne bheja: <code>{input_val}</code>\n\n"
            "Kripya <b>6 se 12 digit numeric 1win Account ID</b> bhejein (jaise: <code>85492018</code>).\n\n"
            "💡 <i>Agar abhi tak account nahi banaya hai, toh niche button se Promo Code <code>{promo_code}</code> use karke register karein!</i>"
        ),
        "connecting_text": (
            "🔄 <b>Connecting to 1win Partners Server...</b>\n"
            "🔍 Verifying Referral Tag for ID: <code>{user_id}</code>"
        ),
        "verified_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>1WIN ACCOUNT VERIFIED!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>1win Account ID:</b> <code>{user_id}</code>\n"
            "🎟️ <b>Promo Code Tag:</b> <code>{promo_code}</code> ✅\n"
            "📡 <b>Referral Status:</b> <b>OFFICIAL PARTNER (Verified)</b>\n"
            "💰 <b>Deposit Status:</b> <code>{dep_str}</code>\n"
            "🚀 <b>VIP Predictor:</b> <b>CONNECTED & READY</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "<b>SIGNALS SHURU KARNE KE STEPS:</b>\n\n"
            "1️⃣ <b>Install App:</b> Niche <b>DOWNLOAD PREDICTOR APK</b> se official app install karein!\n"
            "2️⃣ <b>Join VIP Channel:</b> Rozana live signals ke liye VIP Channel join karein!\n"
            "3️⃣ <b>Activate VIP Access:</b> VIP Support ko apni ID bhej kar live rounds activate karwayein! 👇\n\n"
            "📲 <b>Download APK:</b> {apk_url}\n"
            "📢 <b>VIP Channel:</b> {channel_url}\n"
            "👤 <b>VIP Manager:</b> {support_user}"
        ),
        "rejected_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>ACCOUNT NOT VERIFIED!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>Entered ID:</b> <code>{user_id}</code>\n\n"
            "⚠️ <b>Ye ID hamare official referral link ya Promo Code ({promo_code}) se registered nahi hai!</b>\n\n"
            "VIP Predictor & 99.4% Accurate Signals sirf unhi accounts ke sath sync hote hain jo hamare official link se bane hon.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>Kaise Activate Karein:</b>\n"
            "1️⃣ Niche <b>REGISTER ON 1WIN</b> button par tap karein\n"
            "2️⃣ Naya account banate waqt Promo Code <code>{promo_code}</code> zaroor daalein\n"
            "3️⃣ First deposit karke apna naya ID yahan bhejein — turant verify ho jayega! ✅\n\n"
            "<i>Agar aapne hamare link se hi banaya hai, toh VIP Support par sampark karein:</i> {support_user}"
        ),
        "step1": (
            "📝 <b>STEP 1 OF 3: QUICK REGISTRATION</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Currency select karein & apna <b>Phone + Email</b> dalein\n"
            "② Promo Code me dalein: <code>{promo_code}</code> <i>(+500% Bonus & Predictor Sync)</i>\n"
            "③ Green <b>Register</b> button dabayein ✅"
        ),
        "step2": (
            "💳 <b>STEP 2 OF 3: CHOOSE DEPOSIT METHOD</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Top par <b>Deposit</b> button dabayein\n"
            "② Koi bhi fast payment method select karein:\n"
            "   • <b>PhonePe</b>  |  <b>Paytm</b>  |  <b>UPI</b>\n"
            "③ VIP Predictor ke liye recommended deposit: <b>₹500+</b>"
        ),
        "step3": (
            "✅ <b>STEP 3 OF 3: SUBMIT UTR & UNLOCK VIP</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Payment complete karke apna <b>12-Digit UTR / Ref No.</b> submit karein\n"
            "② Deposit confirm hote hi, <b>apna 1win User ID yahan bhejein</b> live VIP signals unlock karne ke liye! 🚀"
        ),
    },

    "en": {
        "lang_name": "English",
        "welcome": (
            "👑 <b>ROYAL AVIATOR PREDICTOR VIP</b> 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 Welcome, <b>{first_name}</b>!\n\n"
            "Unlock <b>99.4% Accurate VIP Aviator Signals</b> & claim your <b>+500% Welcome Bonus</b> in 3 easy steps:\n\n"
            "1️⃣ <b>Register</b> a new 1win account using the button below\n"
            "2️⃣ Enter Official Promo Code: <code>{promo_code}</code> <i>(Tap to copy)</i>\n"
            "3️⃣ Deposit, download the <b>Aviator Predictor APK</b> & send your 1win User ID to activate! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 <b>Bonus Code:</b> <code>{promo_code}</code> <i>(+500% First Deposit)</i>\n"
            "📲 <b>Predictor App:</b> <a href=\"{apk_url}\">Download APK</a>\n"
            "👇 <b>Tap a button below or send your 1win ID directly:</b>"
        ),
        "btn_register": "🚀 REGISTER ON 1WIN (+500% BONUS)",
        "btn_apk": "📲 DOWNLOAD PREDICTOR APK",
        "btn_guide": "📖 STEP-BY-STEP GUIDE",
        "btn_promo": "🎟️ COPY PROMO CODE",
        "btn_enter_id": "🆔 SUBMIT 1WIN ID",
        "btn_channel": "📢 OFFICIAL VIP CHANNEL",
        "btn_support": "💬 24/7 VIP SUPPORT",
        "btn_lang": "🌐 LANGUAGE",
        "btn_change_id": "🔄 CHANGE ID",
        "btn_main_menu": "🏠 MAIN MENU",
        "btn_try_again": "🔄 TRY AGAIN",
        "btn_activate_signals": "👑 ACTIVATE VIP SIGNALS (SUPPORT)",
        "btn_deposit_guide": "💳 DEPOSIT GUIDE",
        "promo_copied_toast": "Promo Code: {promo_code} (Copied!)",
        "promo_details": (
            "🎟️ <b>OFFICIAL VIP PROMO CODE</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👉  <code>{promo_code}</code>  👈\n\n"
            "<i>(Tap the code above to copy it automatically!)</i>\n\n"
            "✅ <b>Benefits Included:</b>\n"
            "• <b>+500% Welcome Bonus</b> on your first deposit\n"
            "• <b>Instant Synchronization</b> with Royal Aviator Predictor\n"
            "• <b>Priority Fast Withdrawals</b> on official payment systems"
        ),
        "enter_id_prompt": (
            "🆔 <b>SEND YOUR 1WIN USER ID</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Please type and send your <b>6 to 12 digit numeric 1win Account ID</b> below.\n\n"
            "📌 <i>Example:</i> <code>85492018</code>\n\n"
            "👇 <b>Type your User ID in the message box now:</b>"
        ),
        "invalid_id_text": (
            "⚠️ <b>INVALID 1WIN USER ID</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "You sent: <code>{input_val}</code>\n\n"
            "Please send a valid <b>6 to 12 digit numeric 1win Account ID</b> (for example: <code>85492018</code>).\n\n"
            "💡 <i>Don't have a 1win account yet? Register below using Promo Code</i> <code>{promo_code}</code> <i>and send your new ID here!</i>"
        ),
        "connecting_text": (
            "🔄 <b>Connecting to 1win Partners Server...</b>\n"
            "🔍 Verifying Referral Tag for ID: <code>{user_id}</code>"
        ),
        "verified_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>1WIN ACCOUNT VERIFIED!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>1win Account ID:</b> <code>{user_id}</code>\n"
            "🎟️ <b>Promo Code Tag:</b> <code>{promo_code}</code> ✅\n"
            "📡 <b>Referral Status:</b> <b>OFFICIAL PARTNER (Verified)</b>\n"
            "💰 <b>Deposit Status:</b> <code>{dep_str}</code>\n"
            "🚀 <b>VIP Predictor:</b> <b>CONNECTED & READY</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "<b>NEXT STEPS TO UNLOCK SIGNALS:</b>\n\n"
            "1️⃣ <b>Install App:</b> Tap <b>DOWNLOAD PREDICTOR APK</b> below to install the official app!\n"
            "2️⃣ <b>Join VIP Channel:</b> Tap button below for daily live signals & proofs!\n"
            "3️⃣ <b>Activate VIP Access:</b> Send your ID to VIP Support to start receiving rounds! 👇\n\n"
            "📲 <b>Download APK:</b> {apk_url}\n"
            "📢 <b>VIP Channel:</b> {channel_url}\n"
            "👤 <b>VIP Manager:</b> {support_user}"
        ),
        "rejected_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>ACCOUNT NOT VERIFIED!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>Entered ID:</b> <code>{user_id}</code>\n\n"
            "⚠️ <b>This ID is not registered under our official link or Promo Code ({promo_code})!</b>\n\n"
            "VIP Predictor & 99.4% Accurate Signals only synchronize with accounts registered under our official partnership link.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>How to Activate:</b>\n"
            "1️⃣ Tap <b>REGISTER ON 1WIN</b> below\n"
            "2️⃣ Ensure Promo Code <code>{promo_code}</code> is entered during registration\n"
            "3️⃣ Make your first deposit and send your new User ID here for instant activation! ✅\n\n"
            "<i>If you already registered via our link, contact VIP Support:</i> {support_user}"
        ),
        "step1": (
            "📝 <b>STEP 1 OF 3: QUICK REGISTRATION</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Select your currency & enter your <b>Phone + Email</b>\n"
            "② In Promo Code, enter: <code>{promo_code}</code> <i>(Required for +500% Bonus & Predictor Sync)</i>\n"
            "③ Tap the green <b>Register</b> button ✅"
        ),
        "step2": (
            "💳 <b>STEP 2 OF 3: CHOOSE DEPOSIT METHOD</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Tap the <b>Deposit</b> button at the top of the screen\n"
            "② Choose your preferred payment method\n"
            "③ Recommended minimum deposit for VIP Predictor: <b>$10+</b>"
        ),
        "step3": (
            "✅ <b>STEP 3 OF 3: CONFIRM & UNLOCK VIP</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Complete payment and copy transaction reference\n"
            "② Once confirmed, <b>send your 1win User ID here</b> to unlock live VIP Predictor signals! 🚀"
        ),
    },

    "pt": {
        "lang_name": "Português",
        "welcome": (
            "👑 <b>ROYAL AVIATOR PREDICTOR VIP</b> 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 Bem-vindo(a), <b>{first_name}</b>!\n\n"
            "Desbloqueie <b>Sinais VIP do Aviator com 99,4% de Precisão</b> e ganhe seu <b>Bônus de Boas-Vindas de +500%</b> em 3 passos simples:\n\n"
            "1️⃣ <b>Cadastre</b> uma nova conta na 1win pelo botão abaixo\n"
            "2️⃣ Insira o Código Promocional Oficial: <code>{promo_code}</code> <i>(Toque para copiar)</i>\n"
            "3️⃣ Faça um depósito, baixe o <b>APK do Aviator Predictor</b> e envie seu ID de Usuário para ativar! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 <b>Código de Bônus:</b> <code>{promo_code}</code> <i>(+500% no Primeiro Depósito)</i>\n"
            "📲 <b>Aplicativo:</b> <a href=\"{apk_url}\">Baixar APK</a>\n"
            "👇 <b>Toque em um botão abaixo ou envie seu ID da 1win:</b>"
        ),
        "btn_register": "🚀 REGISTRAR NA 1WIN (+500% BÔNUS)",
        "btn_apk": "📲 BAIXAR APK DO PREDICTOR",
        "btn_guide": "📖 GUIA PASSO A PASSO",
        "btn_promo": "🎟️ COPIAR CÓDIGO PROMOCIONAL",
        "btn_enter_id": "🆔 ENVIAR ID DE USUÁRIO",
        "btn_channel": "📢 CANAL VIP OFICIAL 🇵🇹",
        "btn_support": "💬 SUPORTE VIP 24/7",
        "btn_lang": "🌐 IDIOMA / LANGUAGE",
        "btn_change_id": "🔄 ALTERAR ID",
        "btn_main_menu": "🏠 MENU PRINCIPAL",
        "btn_try_again": "🔄 TENTAR NOVAMENTE",
        "btn_activate_signals": "👑 ATIVAR SINAIS VIP (SUPORTE)",
        "btn_deposit_guide": "💳 GUIA DE DEPÓSITO",
        "promo_copied_toast": "Código: {promo_code} (Copiado!)",
        "promo_details": (
            "🎟️ <b>CÓDIGO PROMOCIONAL OFICIAL VIP</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👉  <code>{promo_code}</code>  👈\n\n"
            "<i>(Toque no código acima para copiar automaticamente!)</i>\n\n"
            "✅ <b>Benefícios Inclusos:</b>\n"
            "• <b>+500% de Bônus</b> no seu primeiro depósito\n"
            "• <b>Sincronização Instantânea</b> com o Royal Aviator Predictor\n"
            "• <b>Saques Rápidos Prioritários</b> via PIX e outros métodos"
        ),
        "enter_id_prompt": (
            "🆔 <b>ENVIE SEU ID DE USUÁRIO DA 1WIN</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Por favor, digite e envie seu <b>ID da 1win (6 a 12 dígitos)</b> abaixo.\n\n"
            "📌 <i>Exemplo:</i> <code>85492018</code>\n\n"
            "👇 <b>Digite seu ID na caixa de mensagem agora:</b>"
        ),
        "invalid_id_text": (
            "⚠️ <b>ID DA 1WIN INVÁLIDO</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Você enviou: <code>{input_val}</code>\n\n"
            "Por favor, envie um ID numérico válido de 6 a 12 dígitos (ex: <code>85492018</code>).\n\n"
            "💡 <i>Ainda não tem conta? Cadastre-se pelo botão abaixo com o código</i> <code>{promo_code}</code>!"
        ),
        "connecting_text": (
            "🔄 <b>Conectando ao Servidor de Parceiros 1win...</b>\n"
            "🔍 Verificando ID: <code>{user_id}</code>"
        ),
        "verified_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>CONTA 1WIN VERIFICADA COM SUCESSO!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>ID da Conta:</b> <code>{user_id}</code>\n"
            "🎟️ <b>Código Promocional:</b> <code>{promo_code}</code> ✅\n"
            "📡 <b>Status:</b> <b>PARCEIRO OFICIAL (Verificado)</b>\n"
            "💰 <b>Status do Depósito:</b> <code>{dep_str}</code>\n"
            "🚀 <b>Predictor VIP:</b> <b>CONECTADO E PRONTO</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "<b>PRÓXIMOS PASSOS PARA ATIVAR:</b>\n\n"
            "1️⃣ <b>Instalar App:</b> Toque em <b>BAIXAR APK</b> abaixo para instalar o app oficial!\n"
            "2️⃣ <b>Entrar no Canal VIP:</b> Toque no botão para acompanhar os sinais ao vivo!\n"
            "3️⃣ <b>Ativar Acesso:</b> Chame o Suporte VIP para liberar as rodadas! 👇\n\n"
            "📲 <b>Baixar APK:</b> {apk_url}\n"
            "📢 <b>Canal VIP:</b> {channel_url}\n"
            "👤 <b>Gerente VIP:</b> {support_user}"
        ),
        "rejected_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>CONTA NÃO VERIFICADA!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>ID Informado:</b> <code>{user_id}</code>\n\n"
            "⚠️ <b>Este ID não está cadastrado pelo nosso link ou Código ({promo_code})!</b>\n\n"
            "O Predictor VIP e os sinais de 99,4% só funcionam com contas criadas pelo nosso link de parceria.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>Como Ativar:</b>\n"
            "1️⃣ Toque no botão <b>REGISTRAR NA 1WIN</b> abaixo\n"
            "2️⃣ Insira o código <code>{promo_code}</code> no campo de código promocional\n"
            "3️⃣ Faça seu primeiro depósito e envie seu novo ID aqui! ✅\n\n"
            "<i>Dúvidas? Fale com o Suporte VIP:</i> {support_user}"
        ),
        "step1": (
            "📝 <b>PASSO 1 DE 3: CADASTRO RÁPIDO</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Selecione a moeda (BRL/USD) e insira <b>Telefone e E-mail</b>\n"
            "② No campo Código Promocional, digite: <code>{promo_code}</code>\n"
            "③ Toque no botão verde <b>Registrar</b> ✅"
        ),
        "step2": (
            "💳 <b>PASSO 2 DE 3: ESCOLHA O MÉTODO DE DEPÓSITO</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Clique no botão <b>Depositar</b> no topo da tela\n"
            "② Escolha seu método favorito (ex: <b>PIX</b>)\n"
            "③ Depósito mínimo recomendado para o Predictor VIP: <b>R$ 30+</b>"
        ),
        "step3": (
            "✅ <b>PASSO 3 DE 3: CONFIRME E ATIVE O VIP</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Conclua o pagamento no seu banco\n"
            "② Após a confirmação, <b>envie seu ID de Usuário aqui</b> para liberar os sinais VIP do Aviator! 🚀"
        ),
    },

    "es": {
        "lang_name": "Español",
        "welcome": (
            "👑 <b>ROYAL AVIATOR PREDICTOR VIP</b> 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 ¡Bienvenido(a), <b>{first_name}</b>!\n\n"
            "Desbloquea <b>Señales VIP de Aviator con 99.4% de Precisión</b> y obtén tu <b>Bono de Bienvenida de +500%</b> en 3 simples pasos:\n\n"
            "1️⃣ <b>Regístrate</b> en 1win con el botón de abajo\n"
            "2️⃣ Ingresa el Código Promocional Oficial: <code>{promo_code}</code> <i>(Toca para copiar)</i>\n"
            "3️⃣ Deposita, descarga la <b>APK de Aviator Predictor</b> y envía tu ID de Usuario para activar! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 <b>Código de Bono:</b> <code>{promo_code}</code> <i>(+500% Primer Depósito)</i>\n"
            "📲 <b>Aplicación:</b> <a href=\"{apk_url}\">Descargar APK</a>\n"
            "👇 <b>Toca un botón abajo o envía tu ID de 1win:</b>"
        ),
        "btn_register": "🚀 REGISTRARSE EN 1WIN (+500% BONO)",
        "btn_apk": "📲 DESCARGAR APK PREDICTOR",
        "btn_guide": "📖 GUÍA PASO A PASO",
        "btn_promo": "🎟️ COPIAR CÓDIGO PROMO",
        "btn_enter_id": "🆔 ENVIAR ID DE USUARIO",
        "btn_channel": "📢 CANAL VIP OFICIAL 🇪🇸",
        "btn_support": "💬 SOPORTE VIP 24/7",
        "btn_lang": "🌐 IDIOMA / LANGUAGE",
        "btn_change_id": "🔄 CAMBIAR ID",
        "btn_main_menu": "🏠 MENÚ PRINCIPAL",
        "btn_try_again": "🔄 REINTENTAR",
        "btn_activate_signals": "👑 ACTIVAR SEÑALES VIP (SOPORTE)",
        "btn_deposit_guide": "💳 GUÍA DE DEPÓSITO",
        "promo_copied_toast": "Código: {promo_code} (¡Copiado!)",
        "promo_details": (
            "🎟️ <b>CÓDIGO PROMOCIONAL VIP OFICIAL</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👉  <code>{promo_code}</code>  👈\n\n"
            "<i>(¡Toca el código arriba para copiarlo automáticamente!)</i>\n\n"
            "✅ <b>Beneficios Incluidos:</b>\n"
            "• <b>+500% de Bono</b> en tu primer depósito\n"
            "• <b>Sincronización Instantánea</b> con Royal Aviator Predictor\n"
            "• <b>Retiros Rápidos Prioritarios</b>"
        ),
        "enter_id_prompt": (
            "🆔 <b>ENVÍA TU ID DE USUARIO DE 1WIN</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Por favor escribe y envía tu <b>ID numérico de 1win (6 a 12 dígitos)</b>.\n\n"
            "📌 <i>Ejemplo:</i> <code>85492018</code>\n\n"
            "👇 <b>Escribe tu ID en el cuadro de mensaje ahora:</b>"
        ),
        "invalid_id_text": (
            "⚠️ <b>ID DE 1WIN INVÁLIDO</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Enviaste: <code>{input_val}</code>\n\n"
            "Por favor envía un ID numérico válido de 6 a 12 dígitos (ej: <code>85492018</code>).\n\n"
            "💡 <i>¿No tienes cuenta aún? ¡Regístrate abajo usando el código</i> <code>{promo_code}</code>!"
        ),
        "connecting_text": (
            "🔄 <b>Conectando con Servidores de 1win...</b>\n"
            "🔍 Verificando ID: <code>{user_id}</code>"
        ),
        "verified_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>¡CUENTA DE 1WIN VERIFICADA CON ÉXITO!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>ID de Cuenta:</b> <code>{user_id}</code>\n"
            "🎟️ <b>Código Promo:</b> <code>{promo_code}</code> ✅\n"
            "📡 <b>Estado:</b> <b>SOCIO OFICIAL (Verificado)</b>\n"
            "💰 <b>Estado del Depósito:</b> <code>{dep_str}</code>\n"
            "🚀 <b>Predictor VIP:</b> <b>CONECTADO Y LISTO</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "<b>SIGUIENTES PASOS PARA ACTIVAR:</b>\n\n"
            "1️⃣ <b>Instalar App:</b> Toca <b>DESCARGAR APK</b> abajo para instalar la app oficial.\n"
            "2️⃣ <b>Unirse al Canal VIP:</b> Únete a nuestro canal para señales en vivo.\n"
            "3️⃣ <b>Activar Acceso:</b> Envía tu ID a Soporte VIP para desbloquear las rondas! 👇\n\n"
            "📲 <b>Descargar APK:</b> {apk_url}\n"
            "📢 <b>Canal VIP:</b> {channel_url}\n"
            "👤 <b>Gerente VIP:</b> {support_user}"
        ),
        "rejected_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>¡CUENTA NO VERIFICADA!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>ID Ingresado:</b> <code>{user_id}</code>\n\n"
            "⚠️ <b>¡Este ID no está registrado bajo nuestro link oficial o Código Promo ({promo_code})!</b>\n\n"
            "El Predictor VIP y las señales de 99.4% solo se sincronizan con cuentas creadas desde nuestro enlace oficial.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>Cómo Activar:</b>\n"
            "1️⃣ Toca el botón <b>REGISTRARSE EN 1WIN</b> abajo\n"
            "2️⃣ Asegúrate de ingresar el código <code>{promo_code}</code> al registrarte\n"
            "3️⃣ Haz tu primer depósito y envía tu nuevo ID aquí para activar al instante! ✅\n\n"
            "<i>¿Tienes dudas? Contacta a Soporte VIP:</i> {support_user}"
        ),
        "step1": (
            "📝 <b>PASO 1 DE 3: REGISTRO RÁPIDO</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Selecciona tu moneda e ingresa tu <b>Teléfono + Email</b>\n"
            "② En Código Promocional, escribe: <code>{promo_code}</code>\n"
            "③ Toca el botón verde <b>Registrarse</b> ✅"
        ),
        "step2": (
            "💳 <b>PASO 2 DE 3: ELIGE TU MÉTODO DE DEPÓSITO</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Toca el botón <b>Depositar</b> en la parte superior\n"
            "② Elige tu método preferido de pago local\n"
            "③ Depósito mínimo recomendado para el Predictor: <b>$10+</b>"
        ),
        "step3": (
            "✅ <b>PASSO 3 DE 3: CONFIRMA Y ACTIVA TU VIP</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Completa el pago en tu banco o billetera\n"
            "② Una vez confirmado, <b>envía tu ID de 1win aquí</b> para desbloquear las señales VIP! 🚀"
        ),
    },

    "fr": {
        "lang_name": "Français",
        "welcome": (
            "👑 <b>ROYAL AVIATOR PREDICTOR VIP</b> 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 Bienvenue, <b>{first_name}</b> !\n\n"
            "Débloquez des <b>Signaux VIP Aviator précis à 99,4%</b> et recevez votre <b>Bonus de Bienvenue de +500%</b> en 3 étapes faciles :\n\n"
            "1️⃣ <b>Inscrivez-vous</b> sur 1win avec le bouton ci-dessous\n"
            "2️⃣ Entrez le Code Promo Officiel : <code>{promo_code}</code> <i>(Appuyez pour copier)</i>\n"
            "3️⃣ Déposez, téléchargez l'<b>APK Aviator Predictor</b> et envoyez votre ID Utilisateur pour activer ! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 <b>Code Bonus :</b> <code>{promo_code}</code> <i>(+500% Premier Dépôt)</i>\n"
            "📲 <b>Application :</b> <a href=\"{apk_url}\">Télécharger l'APK</a>\n"
            "👇 <b>Appuyez sur un bouton ci-dessous ou envoyez votre ID 1win :</b>"
        ),
        "btn_register": "🚀 S'INSCRIRE SUR 1WIN (+500% BONUS)",
        "btn_apk": "📲 TÉLÉCHARGER L'APK PREDICTOR",
        "btn_guide": "📖 GUIDE ÉTAPE PAR ÉTAPE",
        "btn_promo": "🎟️ COPIER LE CODE PROMO",
        "btn_enter_id": "🆔 ENVOYER L'ID UTILISATEUR",
        "btn_channel": "📢 CANAL VIP OFFICIEL",
        "btn_support": "💬 SUPPORT VIP 24/7",
        "btn_lang": "🌐 LANGUE / LANGUAGE",
        "btn_change_id": "🔄 CHANGER D'ID",
        "btn_main_menu": "🏠 MENU PRINCIPAL",
        "btn_try_again": "🔄 RÉESSAYER",
        "btn_activate_signals": "👑 ACTIVER SIGNAUX VIP (SUPPORT)",
        "btn_deposit_guide": "💳 GUIDE DE DÉPÔT",
        "promo_copied_toast": "Code Promo: {promo_code} (Copié !)",
        "promo_details": (
            "🎟️ <b>CODE PROMO VIP OFFICIEL</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👉  <code>{promo_code}</code>  👈\n\n"
            "<i>(Appuyez sur le code pour le copier automatiquement !)</i>\n\n"
            "✅ <b>Avantages Inclus :</b>\n"
            "• <b>+500% de Bonus</b> sur votre premier dépôt\n"
            "• <b>Synchronisation Immédiate</b> avec Royal Aviator Predictor\n"
            "• <b>Retraits Rapides Prioritaires</b>"
        ),
        "enter_id_prompt": (
            "🆔 <b>ENVOYEZ VOTRE ID UTILISATEUR 1WIN</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Veuillez taper et envoyer votre <b>ID 1win (6 à 12 chiffres)</b> ci-dessous.\n\n"
            "📌 <i>Exemple :</i> <code>85492018</code>\n\n"
            "👇 <b>Tapez votre ID dans le message maintenant :</b>"
        ),
        "invalid_id_text": (
            "⚠️ <b>ID 1WIN INVALIDE</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Vous avez envoyé : <code>{input_val}</code>\n\n"
            "Veuillez envoyer un ID numérique valide de 6 à 12 chiffres (ex : <code>85492018</code>).\n\n"
            "💡 <i>Pas encore de compte ? Inscrivez-vous ci-dessous avec le code</i> <code>{promo_code}</code> !"
        ),
        "connecting_text": (
            "🔄 <b>Connexion aux serveurs partenaires 1win...</b>\n"
            "🔍 Vérification de l'ID : <code>{user_id}</code>"
        ),
        "verified_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>COMPTE 1WIN VÉRIFIÉ AVEC SUCCÈS !</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>ID de Compte :</b> <code>{user_id}</code>\n"
            "🎟️ <b>Code Promo :</b> <code>{promo_code}</code> ✅\n"
            "📡 <b>Statut :</b> <b>PARTENAIRE OFFICIEL (Vérifié)</b>\n"
            "💰 <b>Statut du Dépôt :</b> <code>{dep_str}</code>\n"
            "🚀 <b>Predictor VIP :</b> <b>CONNECTÉ ET PRÊT</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "<b>ÉTAPES POUR DÉMARRER LES SIGNAUX :</b>\n\n"
            "1️⃣ <b>Installer l'App :</b> Cliquez sur <b>TÉLÉCHARGER L'APK</b> ci-dessous pour installer l'application !\n"
            "2️⃣ <b>Rejoindre le Canal VIP :</b> Suivez les signaux en direct sur notre canal !\n"
            "3️⃣ <b>Activer l'Accès VIP :</b> Envoyez votre ID au Support VIP pour commencer ! 👇\n\n"
            "📲 <b>Télécharger l'APK :</b> {apk_url}\n"
            "📢 <b>Canal VIP :</b> {channel_url}\n"
            "👤 <b>Manager VIP :</b> {support_user}"
        ),
        "rejected_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>COMPTE NON VÉRIFIÉ !</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>ID Envoyé :</b> <code>{user_id}</code>\n\n"
            "⚠️ <b>Cet ID n'est pas enregistré sous notre lien officiel ou Code Promo ({promo_code}) !</b>\n\n"
            "Le Predictor VIP et les signaux précis à 99,4% ne fonctionnent qu'avec les comptes enregistrés sous notre lien partenaire.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>Comment Activer :</b>\n"
            "1️⃣ Cliquez sur <b>S'INSCRIRE SUR 1WIN</b> ci-dessous\n"
            "2️⃣ Entrez bien le Code Promo <code>{promo_code}</code> lors de l'inscription\n"
            "3️⃣ Faites un premier dépôt et renvoyez votre nouvel ID ici ! ✅\n\n"
            "<i>Besoin d'aide ? Contactez le Support VIP :</i> {support_user}"
        ),
        "step1": (
            "📝 <b>ÉTAPE 1 SUR 3 : INSCRIPTION RAPIDE</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Sélectionnez votre devise et entrez votre <b>Téléphone + E-mail</b>\n"
            "② Dans Code Promo, tapez : <code>{promo_code}</code>\n"
            "③ Cliquez sur le bouton vert <b>S'inscrire</b> ✅"
        ),
        "step2": (
            "💳 <b>ÉTAPE 2 SUR 3 : CHOISIR LE MODE DE DÉPÔT</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Cliquez sur <b>Dépôt</b> en haut de l'écran\n"
            "② Choisissez votre moyen de paiement préféré\n"
            "③ Dépôt minimum recommandé pour le Predictor : <b>10 €+</b>"
        ),
        "step3": (
            "✅ <b>ÉTAPE 3 SUR 3 : CONFIRMER ET DÉBLOQUER LE VIP</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Effectuez le paiement\n"
            "② Dès confirmation, <b>envoyez votre ID 1win ici</b> pour activer les signaux VIP en direct ! 🚀"
        ),
    },

    "tr": {
        "lang_name": "Türkçe",
        "welcome": (
            "👑 <b>ROYAL AVIATOR PREDICTOR VIP</b> 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 Hoş geldiniz, <b>{first_name}</b>!\n\n"
            "<b>%99.4 Doğruluk Oranına Sahip VIP Aviator Sinyallerini</b> ve <b>+%500 Hoş Geldin Bonusunu</b> 3 kolay adımda açın:\n\n"
            "1️⃣ Aşağıdaki butondan yeni bir 1win hesabı <b>Açın</b>\n"
            "2️⃣ Resmi Promosyon Kodunu Girin: <code>{promo_code}</code> <i>(Kopyalamak için dokunun)</i>\n"
            "3️⃣ Para yatırın, <b>Aviator Predictor APK</b> indirin ve Kullanıcı ID'nizi göndererek aktifleştirin! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 <b>Bonus Kodu:</b> <code>{promo_code}</code> <i>(+%500 İlk Para Yatırma)</i>\n"
            "📲 <b>Uygulama:</b> <a href=\"{apk_url}\">APK İndir</a>\n"
            "👇 <b>Aşağıdaki butonlardan birine dokunun veya 1win ID'nizi gönderin:</b>"
        ),
        "btn_register": "🚀 1WIN'E KAYDOL (%500 BONUS)",
        "btn_apk": "📲 PREDICTOR APK İNDİR",
        "btn_guide": "📖 ADIM ADIM REHBER",
        "btn_promo": "🎟️ KODU KOPYALA",
        "btn_enter_id": "🆔 KULLANICI ID'Sİ GÖNDER",
        "btn_channel": "📢 RESMİ VIP KANALI 🇹🇷",
        "btn_support": "💬 7/24 VIP DESTEK",
        "btn_lang": "🌐 DİL SEÇİMİ / LANGUAGE",
        "btn_change_id": "🔄 ID DEĞİŞTİR",
        "btn_main_menu": "🏠 ANA MENÜ",
        "btn_try_again": "🔄 TEKRAR DENE",
        "btn_activate_signals": "👑 VIP SİNYALLERİ AÇ (DESTEK)",
        "btn_deposit_guide": "💳 YATIRIM REHBERİ",
        "promo_copied_toast": "Promosyon Kodu: {promo_code} (Kopyalandı!)",
        "promo_details": (
            "🎟️ <b>RESMİ VIP PROMOSYON KODU</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👉  <code>{promo_code}</code>  👈\n\n"
            "<i>(Otomatik kopyalamak için koda dokunun!)</i>\n\n"
            "✅ <b>Dahil Olan Avantajlar:</b>\n"
            "• İlk para yatırmanızda <b>+%500 Hoş Geldin Bonusu</b>\n"
            "• <b>Royal Aviator Predictor</b> ile anında senkronizasyon\n"
            "• <b>Öncelikli Hızlı Para Çekme</b> imkanı"
        ),
        "enter_id_prompt": (
            "🆔 <b>1WIN KULLANICI ID'NİZİ GÖNDERİN</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Lütfen <b>6-12 haneli 1win Hesap ID'nizi</b> aşağıya yazıp gönderin.\n\n"
            "📌 <i>Örnek:</i> <code>85492018</code>\n\n"
            "👇 <b>Kullanıcı ID'nizi şimdi mesaj kutusuna yazın:</b>"
        ),
        "invalid_id_text": (
            "⚠️ <b>GEÇERSİZ 1WIN KULLANICI ID'Sİ</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Gönderilen: <code>{input_val}</code>\n\n"
            "Lütfen geçerli bir <b>6-12 haneli sayısal 1win ID</b> gönderin (örnek: <code>85492018</code>).\n\n"
            "💡 <i>Hesabınız yok mu? Aşağıdaki butondan</i> <code>{promo_code}</code> <i>koduyla kaydolun!</i>"
        ),
        "connecting_text": (
            "🔄 <b>1win Ortaklık Sunucusuna Bağlanılıyor...</b>\n"
            "🔍 ID Doğrulanıyor: <code>{user_id}</code>"
        ),
        "verified_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>1WIN HESABI BAŞARIYLA DOĞRULANDI!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>Hesap ID'si:</b> <code>{user_id}</code>\n"
            "🎟️ <b>Promosyon Kodu:</b> <code>{promo_code}</code> ✅\n"
            "📡 <b>Ortaklık Durumu:</b> <b>RESMİ PARTNER (Doğrulandı)</b>\n"
            "💰 <b>Yatırım Durumu:</b> <code>{dep_str}</code>\n"
            "🚀 <b>VIP Predictor:</b> <b>BAĞLANDI VE HAZIR</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "<b>SİNYALLERİ BAŞLATMAK İÇİN:</b>\n\n"
            "1️⃣ <b>Uygulamayı Yükleyin:</b> Aşağıdaki <b>PREDICTOR APK İNDİR</b> butonundan resmi uygulamayı kurun!\n"
            "2️⃣ <b>VIP Kanala Katılın:</b> Günlük canlı sinyaller için VIP Kanalımıza katılın!\n"
            "3️⃣ <b>VIP Erişimi Açın:</b> Turları başlatmak için ID'nizi VIP Destek ekibine gönderin! 👇\n\n"
            "📲 <b>APK İndir:</b> {apk_url}\n"
            "📢 <b>VIP Kanal:</b> {channel_url}\n"
            "👤 <b>VIP Yönetici:</b> {support_user}"
        ),
        "rejected_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>HESAP DOĞRULANAMADI!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>Girilen ID:</b> <code>{user_id}</code>\n\n"
            "⚠️ <b>Bu ID bizim resmi ortaklık linkimiz veya Promosyon Kodumuz ({promo_code}) ile açılmamış!</b>\n\n"
            "VIP Predictor ve %99.4 doğru sinyaller sadece bizim partner linkimizden açılan hesaplarla çalışır.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>Nasıl Aktif Edilir:</b>\n"
            "1️⃣ Aşağıdaki <b>1WIN'E KAYDOL</b> butonuna dokunun\n"
            "2️⃣ Kayıt olurken <code>{promo_code}</code> kodunu girdiğinizden emin olun\n"
            "3️⃣ İlk yatırımınızı yapıp yeni ID'nizi buraya gönderin, hemen onaylanacaktır! ✅\n\n"
            "<i>Bizim linkimizle açtıysanız VIP Destek ile görüşün:</i> {support_user}"
        ),
        "step1": (
            "📝 <b>1. ADIM (3): HIZLI KAYIT</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Para biriminizi seçin, <b>Telefon ve E-posta</b> bilgilerinizi girin\n"
            "② Promosyon Kodu kısmına yazın: <code>{promo_code}</code>\n"
            "③ Yeşil <b>Kaydol</b> butonuna basın ✅"
        ),
        "step2": (
            "💳 <b>2. ADIM (3): YATIRIM YÖNTEMİ SEÇİN</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Ekranın üstündeki <b>Para Yatır</b> butonuna tıklayın\n"
            "② İstediğiniz hızlı ödeme yöntemini seçin (Havale/Papara/Kripto vb.)\n"
            "③ VIP Predictor için önerilen minimum yatırım: <b>250 TL+</b>"
        ),
        "step3": (
            "✅ <b>3. ADIM (3): ONAYLAYIN VE VIP'Yİ AÇIN</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Ödemeyi tamamlayın\n"
            "② Yatırım onaylandıktan sonra, <b>1win ID'nizi buraya gönderin</b> ve VIP Predictor sinyallerini hemen başlatın! 🚀"
        ),
    },

    "th": {
        "lang_name": "ไทย",
        "welcome": (
            "👑 <b>ROYAL AVIATOR PREDICTOR VIP</b> 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 ยินดีต้อนรับ, <b>{first_name}</b>!\n\n"
            "ปลดล็อก <b>สัญญาณ VIP Aviator แม่นยำ 99.4%</b> และรับ <b>โบนัสต้อนรับ +500%</b> ง่ายๆ ใน 3 ขั้นตอน:\n\n"
            "1️⃣ <b>สมัครสมาชิก</b> บัญชี 1win ใหม่โดยใช้ปุ่มด้านล่าง\n"
            "2️⃣ กรอกรหัสโปรโมชั่นทางการ: <code>{promo_code}</code> <i>(แตะเพื่อคัดลอก)</i>\n"
            "3️⃣ ฝากเงิน, ดาวน์โหลด <b>Aviator Predictor APK</b> และส่ง 1win User ID เพื่อเปิดใช้งาน! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 <b>รหัสโบนัส:</b> <code>{promo_code}</code> <i>(+500% ฝากเงินครั้งแรก)</i>\n"
            "📲 <b>แอปพลิเคชัน:</b> <a href=\"{apk_url}\">ดาวน์โหลด APK</a>\n"
            "👇 <b>แตะปุ่มด้านล่างหรือส่ง 1win ID ของคุณมาได้เลย:</b>"
        ),
        "btn_register": "🚀 สมัครสมาชิก 1WIN (โบนัส +500%)",
        "btn_apk": "📲 ดาวน์โหลด PREDICTOR APK",
        "btn_guide": "📖 คู่มือขั้นตอนการสมัคร",
        "btn_promo": "🎟️ คัดลอกรหัสโปรโมชั่น",
        "btn_enter_id": "🆔 ส่งรหัสผู้ใช้ (USER ID)",
        "btn_channel": "📢 ช่อง VIP ทางการ 🇹🇭",
        "btn_support": "💬 ฝ่ายสนับสนุน VIP 24/7",
        "btn_lang": "🌐 เปลี่ยนภาษา / LANGUAGE",
        "btn_change_id": "🔄 เปลี่ยน ID",
        "btn_main_menu": "🏠 เมนูหลัก",
        "btn_try_again": "🔄 ลองใหม่อีกครั้ง",
        "btn_activate_signals": "👑 เปิดใช้งานสัญญาณ VIP (ติดต่อทีมงาน)",
        "btn_deposit_guide": "💳 วิธีการฝากเงิน",
        "promo_copied_toast": "รหัสโปรโมชั่น: {promo_code} (คัดลอกแล้ว!)",
        "promo_details": (
            "🎟️ <b>รหัสโปรโมชั่น VIP ทางการ</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👉  <code>{promo_code}</code>  👈\n\n"
            "<i>(แตะที่รหัสเพื่อคัดลอกอัตโนมัติ!)</i>\n\n"
            "✅ <b>สิทธิประโยชน์:</b>\n"
            "• <b>+500% โบนัสต้อนรับ</b> สำหรับการฝากเงินครั้งแรก\n"
            "• <b>ซิงค์ข้อมูลทันที</b> กับแอป Royal Aviator Predictor\n"
            "• <b>ถอนเงินด่วนพิเศษ</b> ผ่านระบบอัตโนมัติ"
        ),
        "enter_id_prompt": (
            "🆔 <b>ส่ง 1WIN USER ID ของคุณ</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "กรุณาพิมพ์และส่ง <b>1win Account ID ตัวเลข 6-12 หลัก</b> ด้านล่างนี้\n\n"
            "📌 <i>ตัวอย่าง:</i> <code>85492018</code>\n\n"
            "👇 <b>พิมพ์ User ID ของคุณในกล่องข้อความตอนนี้:</b>"
        ),
        "invalid_id_text": (
            "⚠️ <b>1WIN USER ID ไม่ถูกต้อง</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "คุณส่งมาว่า: <code>{input_val}</code>\n\n"
            "กรุณาส่ง ID ตัวเลข 6 ถึง 12 หลักที่ถูกต้อง (เช่น: <code>85492018</code>)\n\n"
            "💡 <i>ยังไม่มีบัญชี? สมัครด้านล่างโดยใช้รหัส</i> <code>{promo_code}</code> <i>ได้เลย!</i>"
        ),
        "connecting_text": (
            "🔄 <b>กำลังเชื่อมต่อกับเซิร์ฟเวอร์พันธมิตร 1win...</b>\n"
            "🔍 กำลังตรวจสอบ ID: <code>{user_id}</code>"
        ),
        "verified_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>บัญชี 1WIN ได้รับการยืนยันแล้ว!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>1win Account ID:</b> <code>{user_id}</code>\n"
            "🎟️ <b>รหัสโปรโมชั่น:</b> <code>{promo_code}</code> ✅\n"
            "📡 <b>สถานะพันธมิตร:</b> <b>พันธมิตรทางการ (ยืนยันแล้ว)</b>\n"
            "💰 <b>สถานะการฝาก:</b> <code>{dep_str}</code>\n"
            "🚀 <b>VIP Predictor:</b> <b>เชื่อมต่อพร้อมใช้งาน</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "<b>ขั้นตอนถัดไปเพื่อเริ่มใช้งานสัญญาณ:</b>\n\n"
            "1️⃣ <b>ติดตั้งแอป:</b> แตะ <b>ดาวน์โหลด PREDICTOR APK</b> ด้านล่างเพื่อติดตั้งแอปทางการ!\n"
            "2️⃣ <b>เข้าร่วมช่อง VIP:</b> แตะปุ่มด้านล่างเพื่อรับสัญญาณและรีวิวผลการเล่นสดทุกวัน!\n"
            "3️⃣ <b>เปิดใช้งาน VIP:</b> ส่ง ID ของคุณให้ฝ่ายสนับสนุน VIP เพื่อเริ่มรอบการทำกำไร! 👇\n\n"
            "📲 <b>ดาวน์โหลด APK:</b> {apk_url}\n"
            "📢 <b>ช่อง VIP:</b> {channel_url}\n"
            "👤 <b>ผู้ดูแล VIP:</b> {support_user}"
        ),
        "rejected_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>บัญชียังไม่ได้รับการยืนยัน!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>ID ที่ระบุ:</b> <code>{user_id}</code>\n\n"
            "⚠️ <b>ID นี้ไม่ได้สมัครผ่านลิงก์ทางการหรือรหัสโปรโมชั่น ({promo_code}) ของเรา!</b>\n\n"
            "แอป VIP Predictor และสัญญาณแม่นยำ 99.4% สามารถซิงค์ได้เฉพาะบัญชีที่สมัครผ่านลิงก์ทางการของเราเท่านั้น\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>วิธีเปิดใช้งาน:</b>\n"
            "1️⃣ แตะปุ่ม <b>สมัครสมาชิก 1WIN</b> ด้านล่าง\n"
            "2️⃣ กรอกรหัสโปรโมชั่น <code>{promo_code}</code> ตอนสมัคร\n"
            "3️⃣ ฝากเงินครั้งแรกแล้วส่ง ID ใหม่มาที่นี่ — ระบบจะยืนยันให้ทันที! ✅\n\n"
            "<i>หากสมัครผ่านลิงก์เราแล้ว ติดต่อฝ่ายสนับสนุน:</i> {support_user}"
        ),
        "step1": (
            "📝 <b>ขั้นตอนที่ 1 จาก 3: การสมัครสมาชิกด่วน</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① เลือกสกุลเงิน (THB/USD) และกรอก <b>เบอร์โทร + อีเมล</b>\n"
            "② ในช่อง Promo Code ให้กรอก: <code>{promo_code}</code>\n"
            "③ แตะปุ่มสีเขียว <b>สมัครสมาชิก</b> ✅"
        ),
        "step2": (
            "💳 <b>ขั้นตอนที่ 2 จาก 3: เลือกวิธีการฝากเงิน</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① แตะปุ่ม <b>ฝากเงิน</b> ที่ด้านบนของหน้าจอ\n"
            "② เลือกช่องทางการชำระเงินที่สะดวก (เช่น สแกน QR / ธนาคารไทย)\n"
            "③ ยอดฝากขั้นต่ำที่แนะนำสำหรับ VIP Predictor: <b>300 บาทขึ้นไป</b>"
        ),
        "step3": (
            "✅ <b>ขั้นตอนที่ 3 จาก 3: ยืนยันและปลดล็อก VIP</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① ทำการโอนเงินให้เรียบร้อย\n"
            "② เมื่อยอดเงินเข้าแล้ว <b>ส่ง 1win User ID ของคุณมาที่นี่</b> เพื่อปลดล็อกสัญญาณสดทันที! 🚀"
        ),
    },

    "de": {
        "lang_name": "Deutsch",
        "welcome": (
            "👑 <b>ROYAL AVIATOR PREDICTOR VIP</b> 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 Willkommen, <b>{first_name}</b>!\n\n"
            "Schalten Sie <b>zu 99,4% genaue VIP Aviator Signale</b> frei & sichern Sie sich Ihren <b>+500% Willkommensbonus</b> in 3 einfachen Schritten:\n\n"
            "1️⃣ <b>Registrieren</b> Sie ein neues 1win-Konto über den untenstehenden Button\n"
            "2️⃣ Geben Sie den offiziellen Promo-Code ein: <code>{promo_code}</code> <i>(Zum Kopieren tippen)</i>\n"
            "3️⃣ Zahlen Sie ein, laden Sie die <b>Aviator Predictor APK</b> herunter & senden Sie Ihre 1win-ID zur Aktivierung! 🚀\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎁 <b>Bonus-Code:</b> <code>{promo_code}</code> <i>(+500% Erste Einzahlung)</i>\n"
            "📲 <b>Predictor App:</b> <a href=\"{apk_url}\">APK Herunterladen</a>\n"
            "👇 <b>Tippen Sie auf einen Button unten oder senden Sie Ihre 1win-ID direkt:</b>"
        ),
        "btn_register": "🚀 BEI 1WIN REGISTRIEREN (+500% BONUS)",
        "btn_apk": "📲 PREDICTOR APK HERUNTERLADEN",
        "btn_guide": "📖 SCHRITT-FÜR-SCHRITT ANLEITUNG",
        "btn_promo": "🎟️ PROMO-CODE KOPIEREN",
        "btn_enter_id": "🆔 BENUTZER-ID SENDEN",
        "btn_channel": "📢 OFFIZIELLER VIP-KANAL 🇩🇪",
        "btn_support": "💬 24/7 VIP-SUPPORT",
        "btn_lang": "🌐 SPRACHE / LANGUAGE",
        "btn_change_id": "🔄 ID ÄNDERN",
        "btn_main_menu": "🏠 HAUPTMENÜ",
        "btn_try_again": "🔄 ERNEUT VERSUCHEN",
        "btn_activate_signals": "👑 VIP-SIGNALE AKTIVIEREN (SUPPORT)",
        "btn_deposit_guide": "💳 EINZAHLUNGSANLEITUNG",
        "promo_copied_toast": "Promo-Code: {promo_code} (Kopiert!)",
        "promo_details": (
            "🎟️ <b>OFFIZIELLER VIP PROMO-CODE</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👉  <code>{promo_code}</code>  👈\n\n"
            "<i>(Tippen Sie auf den Code oben, um ihn automatisch zu kopieren!)</i>\n\n"
            "✅ <b>Enthaltene Vorteile:</b>\n"
            "• <b>+500% Willkommensbonus</b> auf Ihre erste Einzahlung\n"
            "• <b>Sofortige Synchronisation</b> mit dem Royal Aviator Predictor\n"
            "• <b>Prioritäre schnelle Auszahlungen</b>"
        ),
        "enter_id_prompt": (
            "🆔 <b>SENDEN SIE IHRE 1WIN BENUTZER-ID</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Bitte geben Sie Ihre <b>6- bis 12-stellige 1win Konto-ID</b> unten ein.\n\n"
            "📌 <i>Beispiel:</i> <code>85492018</code>\n\n"
            "👇 <b>Geben Sie Ihre Benutzer-ID jetzt in das Nachrichtenfeld ein:</b>"
        ),
        "invalid_id_text": (
            "⚠️ <b>UNGÜLTIGE 1WIN BENUTZER-ID</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Eingabe: <code>{input_val}</code>\n\n"
            "Bitte senden Sie eine gültige <b>6- bis 12-stellige numerische 1win ID</b> (z.B.: <code>85492018</code>).\n\n"
            "💡 <i>Noch kein Konto? Registrieren Sie sich unten mit dem Promo-Code</i> <code>{promo_code}</code>!"
        ),
        "connecting_text": (
            "🔄 <b>Verbindung zum 1win Partner-Server wird hergestellt...</b>\n"
            "🔍 Verifiziere ID: <code>{user_id}</code>"
        ),
        "verified_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>1WIN-KONTO ERFOLGREICH VERIFIZIERT!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>1win Konto-ID:</b> <code>{user_id}</code>\n"
            "🎟️ <b>Promo-Code:</b> <code>{promo_code}</code> ✅\n"
            "📡 <b>Status:</b> <b>OFFIZIELLER PARTNER (Verifiziert)</b>\n"
            "💰 <b>Einzahlungsstatus:</b> <code>{dep_str}</code>\n"
            "🚀 <b>VIP Predictor:</b> <b>VERBUNDEN & BEREIT</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "<b>NÄCHSTE SCHRITTE ZUR FREISCHALTUNG:</b>\n\n"
            "1️⃣ <b>App installieren:</b> Tippen Sie auf <b>PREDICTOR APK HERUNTERLADEN</b>!\n"
            "2️⃣ <b>VIP-Kanal beitreten:</b> Folgen Sie täglich den Live-Signalen im Kanal!\n"
            "3️⃣ <b>VIP-Zugang aktivieren:</b> Senden Sie Ihre ID an den Support, um Runden zu starten! 👇\n\n"
            "📲 <b>APK herunterladen:</b> {apk_url}\n"
            "📢 <b>VIP-Kanal:</b> {channel_url}\n"
            "👤 <b>VIP-Manager:</b> {support_user}"
        ),
        "rejected_text": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>KONTO NICHT VERIFIZIERT!</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>Eingegebene ID:</b> <code>{user_id}</code>\n\n"
            "⚠️ <b>Diese ID ist nicht über unseren offiziellen Link oder Promo-Code ({promo_code}) registriert!</b>\n\n"
            "Der VIP Predictor und die 99,4% genauen Signale synchronisieren nur mit Partnerkonten.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>Aktivierungsanleitung:</b>\n"
            "1️⃣ Tippen Sie unten auf <b>BEI 1WIN REGISTRIEREN</b>\n"
            "2️⃣ Geben Sie bei der Registrierung unbedingt <code>{promo_code}</code> ein\n"
            "3️⃣ Zahlen Sie ein und senden Sie Ihre neue ID hierher zur sofortigen Freischaltung! ✅\n\n"
            "<i>Haben Sie sich bereits registriert? Kontaktieren Sie den Support:</i> {support_user}"
        ),
        "step1": (
            "📝 <b>SCHRITT 1 VON 3: SCHNELLE REGISTRIERUNG</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Währung wählen und <b>Telefonnummer + E-Mail</b> eingeben\n"
            "② Bei Promo-Code eingeben: <code>{promo_code}</code>\n"
            "③ Auf den grünen Button <b>Registrieren</b> tippen ✅"
        ),
        "step2": (
            "💳 <b>SCHRITT 2 VON 3: EINZAHLUNGSMETHODE WÄHLEN</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Oben auf <b>Einzahlen</b> tippen\n"
            "② Bevorzugte Zahlungsmethode auswählen\n"
            "③ Empfohlene Mindesteinzahlung für VIP Predictor: <b>10 €+</b>"
        ),
        "step3": (
            "✅ <b>SCHRITT 3 VON 3: BESTÄTIGEN & VIP FREISCHALTEN</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① Einzahlung abschließen\n"
            "② Sobald bestätigt, <b>senden Sie Ihre 1win-ID hierher</b>, um die Live-Signale zu starten! 🚀"
        ),
    },
    # =========================================================
    # 🇨🇳 MANDARIN CHINESE
    # =========================================================
    "zh": {
        "lang_name": "中文",
        "welcome": (
            "👑 <b>皇家飞行员VIP精准预测器 • v4.2 PRO</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "👋 欢迎，<b>{first_name}</b>！\n\n"
            "🟢 <b>系统状态：</b> 联机已同步\n"
            "⚡ <b>信号准确率：</b> 99.4% 精确倍数\n"
            "🎁 <b>VIP首充红利：</b> +500% 独家奖励\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>只需3个简单步骤即可激活：</b>\n"
            "1️⃣ 点击下方 <b>在 1WIN 注册</b> 创建新账户\n"
            "2️⃣ Promo Code 优惠码：<code>{promo_code}</code> <i>(点击复制)</i>\n"
            "3️⃣ 完成充值并在此发送您的 <b>1win 用户ID</b>！ ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎟️ <b>专属优惠码：</b> <code>{promo_code}</code>\n"
            "📲 <b>预测器应用：</b> <a href=\"{apk_url}\">点击下载 APK</a>\n\n"
            "👇 <b>点击下方按钮或直接发送您的 1win ID：</b>"
        ),
        "btn_register": "🚀 在 1WIN 注册 (+500% 红利)",
        "btn_apk": "📲 下载预测器 APK",
        "btn_guide": "📖 新手图文指引",
        "btn_promo": "🎟️ 复制优惠码",
        "btn_enter_id": "🆔 提交 1WIN ID",
        "btn_channel": "📢 官方 VIP 频道",
        "btn_support": "💬 24/7 VIP 客服",
        "btn_lang": "🌐 切换语言 / LANGUAGE",
        "btn_change_id": "🔄 更换 ID",
        "btn_main_menu": "🏠 主菜单",
        "btn_try_again": "🔄 重试",
        "btn_activate_signals": "👑 联系客服激活 VIP 信号",
        "btn_deposit_guide": "💳 充值指南",
        "promo_copied_toast": "优惠码: {promo_code} (已复制!)",
        "promo_details": (
            "🎟️ <b>官方 VIP 专属优惠码</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👉  <code>{promo_code}</code>  👈\n\n"
            "<i>(点击代码即可复制!)</i>\n\n"
            "✅ <b>VIP 特权：</b>\n"
            "• 首次充值立享 <b>+500% 欢迎红利</b>\n"
            "• 与 <b>Royal Aviator Predictor</b> 实时同步\n"
            "• 极速优先提现通道"
        ),
        "enter_id_prompt": (
            "🆔 <b>发送您的 1WIN 用户 ID</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "请在此输入并发送您的 <b>6 至 12 位 1win 账号 ID</b>。\n\n"
            "📌 <i>示例：</i> <code>85492018</code>\n\n"
            "👇 <b>请在下方输入框中直接发送：</b>"
        ),
        "step1": (
            "📝 <b>第 1 步（共 3 步）：快速注册与优惠码</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① 点击下方按钮打开 1win 注册页面\n"
            "② 选择币种并输入您的<b>手机号与邮箱</b>\n"
            "③ 在<b>优惠码（PROMO CODE）</b>栏填入：<code>{promo_code}</code>\n"
            "④ 点击 <b>注册（Register）</b> 按钮。"
        ),
        "step2": (
            "💳 <b>第 2 步（共 3 步）：选择充值方式</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① 点击右上角绿色的 <b>充值（Deposit）</b> 按钮\n"
            "② 选择您偏好的支付方式：<b>USDT / 银行卡 / 电子钱包</b>\n"
            "③ 激活 VIP 信号的推荐充值金额：<b>10 USDT 以上</b>。"
        ),
        "step3": (
            "✅ <b>第 3 步（共 3 步）：确认充值并激活 VIP</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "① 完成充值支付\n"
            "② 账户余额到账后，<b>在此聊天中发送您的 1win 用户 ID</b>\n"
            "③ 您的 VIP 预测器将立即自动激活！ 🚀"
        ),
        "verified": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>账户验证成功！</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>您的 1win ID：</b> <code>{user_id}</code>\n"
            "🟢 <b>同步状态：</b> 已成功连接预测器系统\n"
            "⚡ <b>VIP 信号精准度：</b> 99.4%\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>如何开始盈利：</b>\n"
            "1️⃣ 打开 1win 平台上的 <b>Aviator</b> 游戏\n"
            "2️⃣ 保持此聊天窗口开启或下载 APK\n"
            "3️⃣ 按照实时信号倍数自动兑现获利！ 💰\n\n"
            "👇 <b>点击下方按钮进入官方 VIP 频道获取实时信号：</b>"
        ),
        "rejected": (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>账户未验证！</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆔 <b>输入的 ID：</b> <code>{user_id}</code>\n\n"
            "⚠️ <b>该 ID 未通过我们的官方链接或优惠码 ({promo_code}) 注册！</b>\n\n"
            "VIP 预测器与 99.4% 精准信号仅与通过官方邀请链接创建的账户同步。\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 <b>如何正确激活：</b>\n"
            "1️⃣ 点击下方 <b>在 1WIN 注册</b> 按钮\n"
            "2️⃣ 创建新账户时务必填写优惠码 <code>{promo_code}</code>\n"
            "3️⃣ 完成首充并在此发送您的新 ID，即可秒级验证！ ✅\n\n"
            "<i>如果您确已通过我们链接注册，请联系客服：</i> {support_username}"
        ),
    },
}


def get_str(lang: str, key: str, **kwargs) -> str:
    lang_dict = STRINGS.get(lang, STRINGS[DEFAULT_LANG])
    template = lang_dict.get(key, STRINGS[DEFAULT_LANG].get(key, ""))
    if kwargs:
        try:
            return template.format(**kwargs)
        except Exception:
            return template
    return template
