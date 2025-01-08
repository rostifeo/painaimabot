import logging
import os
from dotenv import load_dotenv  # Импортируем для загрузки переменных окружения
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

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
"ru": [
    "Амнатчарен",
    "Ангтхонг",
    "Бангкок",
    "Бурирам",
    "Бунгкан",
    "Галасин",
    "Кампхэнгпхет",
    "Канчанабури",
    "Конкэн",
    "Краби",
    "Лампанг",
    "Лампхун",
    "Лoeй",
    "Маехонгсон",
    "Махасаракхам",
    "Мукдахан",
    "Накхоннайок",
    "Накхонпатхом",
    "Накхонпханом",
    "Накхонратчасима",
    "Накхонситхаммарат",
    "Накхонсаван",
    "Наративат",
    "Нонгбуалампху",
    "Нонгкхай",
    "Нонтхабури",
    "Паттани",
    "Патхумтхани",
    "Пхетчабун",
    "Пхетчабури",
    "Пхичит",
    "Пхитсанулок",
    "Пхетчбун",
    "Прачинбури",
    "Прачуапкхирикхан",
    "Пхангнга",
    "Пхатталунг",
    "Пхаяо",
    "Ранонг",
    "Ратчабури",
    "Районг",
    "Роет",
    "Са Kaeo",
    "Саконнакхон",
    "Самутпракан",
    "Самутсакхон",
    "Самутсонгкхрам",
    "Сарабури",
    "Сатун",
    "Сингбури",
    "Сисакет",
    "Сонгкхла",
    "Сукхотхай",
    "Супханбури",
    "Сураттхани",
    "Сурин",
    "Так",
    "Транг",
    "Трат",
    "Убонратчатхани",
    "Удонтхани",
    "Утхайтхани",
    "Чайяпхум",
    "Чантхабури",
    "Ченгмай",
    "Чиангмай",
    "Чианграй",
    "Чонбури",
    "Чумпхон",
    "Яла",
    "Ясотхон"
  ],
  "en": [
    "Amnat Charoen",
    "Ang Thong",
    "Bangkok",
    "Bueng Kan",
    "Buri Ram",
    "Chachoengsao",
    "Chai Nat",
    "Chaiyaphum",
    "Chanthaburi",
    "Chiang Mai",
    "Chiang Rai",
    "Chonburi",
    "Chumphon",
    "Kalasin",
    "Kamphaeng Phet",
    "Kanchanaburi",
    "Khon Kaen",
    "Krabi",
    "Lampang",
    "Lamphun",
    "Loei",
    "Lopburi",
    "Mae Hong Son",
    "Maha Sarakham",
    "Mukdahan",
    "Nakhon Nayok",
    "Nakhon Pathom",
    "Nakhon Phanom",
    "Nakhon Ratchasima",
    "Nakhon Sawan",
    "Nakhon Si Thammarat",
    "Nan",
    "Narathiwat",
    "Nong Bua Lamphu",
    "Nong Khai",
    "Nonthaburi",
    "Pathum Thani",
    "Pattani",
    "Phang Nga",
    "Phatthalung",
    "Phayao",
    "Phetchabun",
    "Phetchaburi",
    "Phichit",
    "Phitsanulok",
    "Phrae",
    "Prachin Buri",
    "Prachuap Khiri Khan",
    "Ranong",
    "Ratchaburi",
    "Rayong",
    "Roi Et",
    "Sa Kaeo",
    "Sakon Nakhon",
    "Samut Prakan",
    "Samut Sakhon",
    "Samut Songkhram",
    "Saraburi",
    "Satun",
    "Sing Buri",
    "Si Sa Ket",
    "Songkhla",
    "Sukhothai",
    "Suphan Buri",
    "Surat Thani",
    "Surin",
    "Tak",
    "Trang",
    "Trat",
    "Ubon Ratchathani",
    "Udon Thani",
    "Uthai Thani",
    "Uttaradit",
    "Yala",
    "Yasothon"
  ]
}


async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE, channel_username: str):
    try:
        chat_member = await context.bot.get_chat_member(chat_id=channel_username, user_id=update.effective_user.id)
        return chat_member.status in ("member", "creator", "administrator")
    except Exception as e:
        logger.error(f"Error checking subscription: {e}")
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data="lang_ru"),
         InlineKeyboardButton("English", callback_data="lang_en")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите язык / Choose a language:", reply_markup=reply_markup)


async def select_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = query.data.split("_")[1]
    context.user_data["language"] = lang

    channel_username = "@mrsaforost" if lang == "ru" else "@rostifeoth"
    if await check_subscription(update, context, channel_username):
        await query.edit_message_text(
            "Круто, что ты любишь Таиланд и хочешь посетить все провинции! Давай посмотрим, где ты уже был?" if lang == "ru" else \
            "Great that you love Thailand and want to visit all provinces! Let's see where you have been?"
        )
        await show_main_menu(update, context)
    else:
        await query.edit_message_text(
            f"Пожалуйста, подпишитесь на канал {channel_username} для продолжения." if lang == "ru" else \
            f"Please subscribe to the channel {channel_username} to continue."
        )


async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("language", "en")
    keyboard = [
        [InlineKeyboardButton("Добавить провинцию" if lang == "ru" else "Add Province", callback_data="add_province"),
         InlineKeyboardButton("Посмотреть результат" if lang == "ru" else "View Result", callback_data="view_result")],
        [InlineKeyboardButton("Авиабилеты дешево ✈️" if lang == "ru" else "Cheap Flights ✈️", 
                               url="https://aviasales.tp.st/vYFLdQPU" if lang == "ru" else "https://wayaway.tp.st/jf2iwRrr")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        "Главное меню" if lang == "ru" else "Main menu",
        reply_markup=reply_markup
    )


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
        "Выберите провинцию, которую хотите добавить:" if lang == "ru" else "Select a province you want to add:",
        reply_markup=reply_markup
    )


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
        f"Сохранил провинцию: {province}. {visited_count} из {total_count} провинций посещено ({progress:.2f}%)." if lang == "ru" else \
        f"Saved province: {province}. {visited_count} out of {total_count} provinces visited ({progress:.2f}%)."
    )

    keyboard = [
        [InlineKeyboardButton("Добавить еще", callback_data="add_province"),
         InlineKeyboardButton("Посмотреть результат", callback_data="view_result")],
        [InlineKeyboardButton("Меню", callback_data="back_to_main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text(
        "Выберите действие:" if lang == "ru" else "Choose an action:",
        reply_markup=reply_markup
    )


async def view_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("language", "en")
    visited = context.user_data.get("visited_provinces", set())
    total = len(provinces[lang])
    visited_count = len(visited)
    progress = (visited_count / total) * 100

    await update.callback_query.edit_message_text(
        f"Вы посетили {visited_count} из {total} провинций ({progress:.2f}%)." if lang == "ru" else \
        f"You have visited {visited_count} out of {total} provinces ({progress:.2f}%)."
    )

    keyboard = [
        [InlineKeyboardButton("Добавить провинцию", callback_data="add_province"),
         InlineKeyboardButton("Меню", callback_data="back_to_main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "Что бы вы хотели сделать?" if lang == "ru" else "What would you like to do?",
        reply_markup=reply_markup
    )


def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(select_language, pattern="^lang_"))
    application.add_handler(CallbackQueryHandler(show_main_menu, pattern="back_to_main_menu"))
    application.add_handler(CallbackQueryHandler(show_provinces, pattern="^add_province$"))
    application.add_handler(CallbackQueryHandler(select_province, pattern="^province_"))
    application.add_handler(CallbackQueryHandler(view_result, pattern="^view_result$"))

    application.run_polling()


if __name__ == "__main__":
    main()
