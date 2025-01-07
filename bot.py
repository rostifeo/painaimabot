import logging
import os
from dotenv import load_dotenv  # Импортируем для загрузки переменных окружения
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Загружаем переменные окружения из файла .env
load_dotenv()

# Теперь токен будет загружен из переменной окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Список провинций Таиланда
provinces = {
    "ru": ["Бангкок", "Чиангмай", "Пхукет", "Краби", "Чианграй", "Лампанг", "Лампхун", "Мае Хонг Сон",
           "Накхонсаван", "Утхайтхани", "Кампхэнгпхет", "Так", "Сукхотхай", "Пхитсанулок", "Пхичит",
           "Пхетчабун", "Ратчабури", "Канчанабури", "Супханбури", "Накхонпатхом", "Самутсакхон",
           "Самутсонгкхрам", "Пхетчабури", "Прачуапкхирикхан", "Чонбури", "Районг", "Чантхабури",
           "Трат", "Накхоннайок", "Прачинабури", "Сакэу", "Накхонратчасима", "Бурирам", "Сурин",
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

# Проверка подписки на канал
async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE, channel_username: str):
    try:
        chat_member = await context.bot.get_chat_member(chat_id=channel_username, user_id=update.effective_user.id)
        return chat_member.status in ("member", "creator", "administrator")
    except Exception as e:
        logger.error(f"Error checking subscription: {e}")
        return False

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data="lang_ru"),
         InlineKeyboardButton("English", callback_data="lang_en")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите язык / Choose a language:", reply_markup=reply_markup)

# Обработчик выбора языка
async def select_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = query.data.split("_")[1]  # Извлекаем язык
    context.user_data["language"] = lang

    channel_username = "@mrsaforost" if lang == "ru" else "@rostifeoth"
    if await check_subscription(update, context, channel_username):
        await query.edit_message_text(
            "Как хорошо ты знаешь Таиланд? Давай проверим, в каких провинциях ты уже был?" if lang == "ru" else \
            "How well do you know Thailand? Let's check which provinces you have already visited?"
        )
        await show_provinces(update, context)
    else:
        await query.edit_message_text(
            f"Пожалуйста, подпишитесь на канал {channel_username} для продолжения." if lang == "ru" else \
            f"Please subscribe to the channel {channel_username} to continue."
        )

# Показ провинций
async def show_provinces(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("language", "en")
    visited = context.user_data.setdefault("visited_provinces", set())
    available = [prov for prov in provinces[lang] if prov not in visited]

    if not available:
        await update.callback_query.edit_message_text(
            "Вы уже посетили все провинции!" if lang == "ru" else "You have already visited all provinces!"
        )
        return

    keyboard = [[InlineKeyboardButton(prov, callback_data=f"province_{prov}")] for prov in available]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        "Выберите провинцию, в которой вы были:" if lang == "ru" else "Select a province you have visited:",
        reply_markup=reply_markup
    )

# Обработчик выбора провинции
async def select_province(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    province = query.data.replace("province_", "")
    lang = context.user_data.get("language", "en")
    visited = context.user_data.setdefault("visited_provinces", set())
    visited.add(province)

    visited_count = len(visited)
    total_count = len(provinces[lang])
    progress = (visited_count / total_count) * 100

    await query.edit_message_text(
        f"Прогресс: {visited_count}/{total_count} провинций ({progress:.2f}%)" if lang == "ru" else \
        f"Progress: {visited_count}/{total_count} provinces ({progress:.2f}%)"
    )

    await show_provinces(update, context)

# Запуск бота
def main():
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(select_language, pattern="^lang_"))
    application.add_handler(CallbackQueryHandler(select_province, pattern="^province_"))

    application.run_polling()

if __name__ == "__main__":
    main()
