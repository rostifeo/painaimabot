from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Список провинций Таиланда
provinces = {
    "ru": ["Бангкок", "Чиангмай", "Пхукет", "Краби", "Чианграй", "Лампанг", "Лампхун", "Мае Хонг Сон", 
"Накхонсаван", "Утхайтхани", "Кампхэнгпхет", "Так", "Сукхотхай", "Пхитсанулок", "Пхичит", 
"Пхетчабун", "Ратчабури", "Канчанабури", "Супханбури", "Накхонпатхом", "Самутсакхон", 
"Самутсонгкхрам", "Пхетчабури", "Прачуапкхирикхан", "Чонбури", "Районг", "Чантхабури", 
"Трат", "Накхоннайок", "Прачинабури", "Сакэу", "Накхонратчасима", "Бурирами", "Сурин", 
"Сисакет", "Убонратчатхани", "Ясотхон", "Чайяпхум", "Амнатчарен", "Нонгбуалампху", 
"Конкэн", "Удонтхани", "Лой", "Нонгкхай", "Махасаракхам", "Роет", "Каласин", "Саконнакхон", 
"Накхонпханом", "Мукдахан", "Пхатталунг", "Сонгкхла", "Паттани", "Яла", "Наративат", 
"Сатун", "Транг", "Накхонситхаммарат", "Пхангнга", "Ранонг", "Чумпхон", "Сураттхани"],
    "en": ["Bangkok", "Chiang Mai", "Phuket", "Krabi", "Chiang Rai", "Lampang", "Lamphun", "Mae Hong Son", 
"Nakhon Sawan", "Uthai Thani", "Kamphaeng Phet", "Tak", "Sukhothai", "Phitsanulok", "Phichit", 
"Phetchabun", "Ratchaburi", "Kanchanaburi", "Suphan Buri", "Nakhon Pathom", "Samut Sakhon", 
"Samut Songkhram", "Phetchaburi", "Prachuap Khiri Khan", "Chon Buri", "Rayong", "Chanthaburi", 
"Trat", "Nakhon Nayok", "Prachin Buri", "Sa Kaeo", "Nakhon Ratchasima", "Buri Ram", "Surin", 
"Si Sa Ket", "Ubon Ratchathani", "Yasothon", "Chaiyaphum", "Amnat Charoen", "Nong Bua Lam Phu", 
"Khon Kaen", "Udon Thani", "Loei", "Nong Khai", "Maha Sarakham", "Roi Et", "Kalasin", "Sakon Nakhon", 
"Nakhon Phanom", "Mukdahan", "Phatthalung", "Songkhla", "Pattani", "Yala", "Narathiwat", 
"Satun", "Trang", "Nakhon Si Thammarat", "Phang Nga", "Ranong", "Chumphon", "Surat Thani"]
}

user_data = {}

# Команда /start
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data="lang_ru"),
         InlineKeyboardButton("English", callback_data="lang_en")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Выберите язык / Choose a language:", reply_markup=reply_markup)

# Обработчик выбора языка
def select_language(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "lang_ru":
        context.user_data["language"] = "ru"
        query.edit_message_text(
            "Спасибо, что решили попробовать наш бот! Для начала, пожалуйста, подпишитесь на этот канал: https://t.me/mrsaforost"
        )
    elif query.data == "lang_en":
        context.user_data["language"] = "en"
        query.edit_message_text(
            "Thank you for trying our bot! To get started, please subscribe to this channel: https://t.me/rostifeoth"
        )

    # Проверка подписки (заглушка)
    # После подтверждения подписи вызвать функцию check_provinces

# Проверка провинций
def check_provinces(update: Update, context: CallbackContext):
    lang = context.user_data.get("language", "en")
    visited = user_data.get(update.effective_user.id, [])
    available = [prov for prov in provinces[lang] if prov not in visited]

    if not available:
        update.message.reply_text(
            "Вы уже посетили все провинции!" if lang == "ru" else "You have already visited all provinces!"
        )
        return

    keyboard = [[InlineKeyboardButton(prov, callback_data=f"province_{prov}") for prov in available]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Выберите провинцию, в которой вы были:" if lang == "ru" else "Select a province you have visited:",
        reply_markup=reply_markup
    )

# Обработчик выбора провинции
def select_province(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    province = query.data.replace("province_", "")
    user_id = update.effective_user.id

    if user_id not in user_data:
        user_data[user_id] = []

    user_data[user_id].append(province)

    lang = context.user_data.get("language", "en")
    visited = len(user_data[user_id])
    total = len(provinces[lang])
    progress = (visited / total) * 100

    query.edit_message_text(
        f"Прогресс: {visited}/{total} провинций ({progress:.2f}%)" if lang == "ru" else \
        f"Progress: {visited}/{total} provinces ({progress:.2f}%)"
    )

# Основная функция
def main():
    application = Application.builder().token("7761938356:AAHmFF40Kd8qNRONnfGFNgtP2-cUzQsDmL8").build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(select_language, pattern="^lang_"))
application.add_handler(CallbackQueryHandler(select_province, pattern="^province_"))

application.run_polling()

# Для ожидания завершения работы
application.idle()


if __name__ == "__main__":
    main()
