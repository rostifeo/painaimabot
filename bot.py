{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup\
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext\
\
# \uc0\u1057 \u1087 \u1080 \u1089 \u1086 \u1082  \u1087 \u1088 \u1086 \u1074 \u1080 \u1085 \u1094 \u1080 \u1081  \u1058 \u1072 \u1080 \u1083 \u1072 \u1085 \u1076 \u1072 \
provinces = \{\
    "ru": ["\uc0\u1041 \u1072 \u1085 \u1075 \u1082 \u1086 \u1082 ", "\u1063 \u1080 \u1072 \u1085 \u1075 \u1084 \u1072 \u1081 ", "\u1055 \u1093 \u1091 \u1082 \u1077 \u1090 ", "\u1050 \u1088 \u1072 \u1073 \u1080 ", "\u1063 \u1080 \u1072 \u1085 \u1075 \u1088 \u1072 \u1081 ", "\u1051 \u1072 \u1084 \u1087 \u1072 \u1085 \u1075 ", "\u1051 \u1072 \u1084 \u1087 \u1093 \u1091 \u1085 ", "\u1052 \u1072 \u1077  \u1061 \u1086 \u1085 \u1075  \u1057 \u1086 \u1085 ", \
"\uc0\u1053 \u1072 \u1082 \u1093 \u1086 \u1085 \u1089 \u1072 \u1074 \u1072 \u1085 ", "\u1059 \u1090 \u1093 \u1072 \u1081 \u1090 \u1093 \u1072 \u1085 \u1080 ", "\u1050 \u1072 \u1084 \u1087 \u1093 \u1101 \u1085 \u1075 \u1087 \u1093 \u1077 \u1090 ", "\u1058 \u1072 \u1082 ", "\u1057 \u1091 \u1082 \u1093 \u1086 \u1090 \u1093 \u1072 \u1081 ", "\u1055 \u1093 \u1080 \u1090 \u1089 \u1072 \u1085 \u1091 \u1083 \u1086 \u1082 ", "\u1055 \u1093 \u1080 \u1095 \u1080 \u1090 ", \
"\uc0\u1055 \u1093 \u1077 \u1090 \u1095 \u1072 \u1073 \u1091 \u1085 ", "\u1056 \u1072 \u1090 \u1095 \u1072 \u1073 \u1091 \u1088 \u1080 ", "\u1050 \u1072 \u1085 \u1095 \u1072 \u1085 \u1072 \u1073 \u1091 \u1088 \u1080 ", "\u1057 \u1091 \u1087 \u1093 \u1072 \u1085 \u1073 \u1091 \u1088 \u1080 ", "\u1053 \u1072 \u1082 \u1093 \u1086 \u1085 \u1087 \u1072 \u1090 \u1093 \u1086 \u1084 ", "\u1057 \u1072 \u1084 \u1091 \u1090 \u1089 \u1072 \u1082 \u1093 \u1086 \u1085 ", \
"\uc0\u1057 \u1072 \u1084 \u1091 \u1090 \u1089 \u1086 \u1085 \u1075 \u1082 \u1093 \u1088 \u1072 \u1084 ", "\u1055 \u1093 \u1077 \u1090 \u1095 \u1072 \u1073 \u1091 \u1088 \u1080 ", "\u1055 \u1088 \u1072 \u1095 \u1091 \u1072 \u1087 \u1082 \u1093 \u1080 \u1088 \u1080 \u1082 \u1093 \u1072 \u1085 ", "\u1063 \u1086 \u1085 \u1073 \u1091 \u1088 \u1080 ", "\u1056 \u1072 \u1081 \u1086 \u1085 \u1075 ", "\u1063 \u1072 \u1085 \u1090 \u1093 \u1072 \u1073 \u1091 \u1088 \u1080 ", \
"\uc0\u1058 \u1088 \u1072 \u1090 ", "\u1053 \u1072 \u1082 \u1093 \u1086 \u1085 \u1085 \u1072 \u1081 \u1086 \u1082 ", "\u1055 \u1088 \u1072 \u1095 \u1080 \u1085 \u1072 \u1073 \u1091 \u1088 \u1080 ", "\u1057 \u1072 \u1082 \u1101 \u1091 ", "\u1053 \u1072 \u1082 \u1093 \u1086 \u1085 \u1088 \u1072 \u1090 \u1095 \u1072 \u1089 \u1080 \u1084 \u1072 ", "\u1041 \u1091 \u1088 \u1080 \u1088 \u1072 \u1084 \u1080 ", "\u1057 \u1091 \u1088 \u1080 \u1085 ", \
"\uc0\u1057 \u1080 \u1089 \u1072 \u1082 \u1077 \u1090 ", "\u1059 \u1073 \u1086 \u1085 \u1088 \u1072 \u1090 \u1095 \u1072 \u1090 \u1093 \u1072 \u1085 \u1080 ", "\u1071 \u1089 \u1086 \u1090 \u1093 \u1086 \u1085 ", "\u1063 \u1072 \u1081 \u1103 \u1087 \u1093 \u1091 \u1084 ", "\u1040 \u1084 \u1085 \u1072 \u1090 \u1095 \u1072 \u1088 \u1077 \u1085 ", "\u1053 \u1086 \u1085 \u1075 \u1073 \u1091 \u1072 \u1083 \u1072 \u1084 \u1087 \u1093 \u1091 ", \
"\uc0\u1050 \u1086 \u1085 \u1082 \u1101 \u1085 ", "\u1059 \u1076 \u1086 \u1085 \u1090 \u1093 \u1072 \u1085 \u1080 ", "\u1051 \u1086 \u1081 ", "\u1053 \u1086 \u1085 \u1075 \u1082 \u1093 \u1072 \u1081 ", "\u1052 \u1072 \u1093 \u1072 \u1089 \u1072 \u1088 \u1072 \u1082 \u1093 \u1072 \u1084 ", "\u1056 \u1086 \u1077 \u1090 ", "\u1050 \u1072 \u1083 \u1072 \u1089 \u1080 \u1085 ", "\u1057 \u1072 \u1082 \u1086 \u1085 \u1085 \u1072 \u1082 \u1093 \u1086 \u1085 ", \
"\uc0\u1053 \u1072 \u1082 \u1093 \u1086 \u1085 \u1087 \u1093 \u1072 \u1085 \u1086 \u1084 ", "\u1052 \u1091 \u1082 \u1076 \u1072 \u1093 \u1072 \u1085 ", "\u1055 \u1093 \u1072 \u1090 \u1090 \u1072 \u1083 \u1091 \u1085 \u1075 ", "\u1057 \u1086 \u1085 \u1075 \u1082 \u1093 \u1083 \u1072 ", "\u1055 \u1072 \u1090 \u1090 \u1072 \u1085 \u1080 ", "\u1071 \u1083 \u1072 ", "\u1053 \u1072 \u1088 \u1072 \u1090 \u1080 \u1074 \u1072 \u1090 ", \
"\uc0\u1057 \u1072 \u1090 \u1091 \u1085 ", "\u1058 \u1088 \u1072 \u1085 \u1075 ", "\u1053 \u1072 \u1082 \u1093 \u1086 \u1085 \u1089 \u1080 \u1090 \u1093 \u1072 \u1084 \u1084 \u1072 \u1088 \u1072 \u1090 ", "\u1055 \u1093 \u1072 \u1085 \u1075 \u1085 \u1075 \u1072 ", "\u1056 \u1072 \u1085 \u1086 \u1085 \u1075 ", "\u1063 \u1091 \u1084 \u1087 \u1093 \u1086 \u1085 ", "\u1057 \u1091 \u1088 \u1072 \u1090 \u1090 \u1093 \u1072 \u1085 \u1080 "],\
    "en": ["Bangkok", "Chiang Mai", "Phuket", "Krabi", "Chiang Rai", "Lampang", "Lamphun", "Mae Hong Son", \
"Nakhon Sawan", "Uthai Thani", "Kamphaeng Phet", "Tak", "Sukhothai", "Phitsanulok", "Phichit", \
"Phetchabun", "Ratchaburi", "Kanchanaburi", "Suphan Buri", "Nakhon Pathom", "Samut Sakhon", \
"Samut Songkhram", "Phetchaburi", "Prachuap Khiri Khan", "Chon Buri", "Rayong", "Chanthaburi", \
"Trat", "Nakhon Nayok", "Prachin Buri", "Sa Kaeo", "Nakhon Ratchasima", "Buri Ram", "Surin", \
"Si Sa Ket", "Ubon Ratchathani", "Yasothon", "Chaiyaphum", "Amnat Charoen", "Nong Bua Lam Phu", \
"Khon Kaen", "Udon Thani", "Loei", "Nong Khai", "Maha Sarakham", "Roi Et", "Kalasin", "Sakon Nakhon", \
"Nakhon Phanom", "Mukdahan", "Phatthalung", "Songkhla", "Pattani", "Yala", "Narathiwat", \
"Satun", "Trang", "Nakhon Si Thammarat", "Phang Nga", "Ranong", "Chumphon", "Surat Thani"]\
\}\
\
user_data = \{\}\
\
# \uc0\u1050 \u1086 \u1084 \u1072 \u1085 \u1076 \u1072  /start\
def start(update: Update, context: CallbackContext):\
    keyboard = [\
        [InlineKeyboardButton("\uc0\u1056 \u1091 \u1089 \u1089 \u1082 \u1080 \u1081 ", callback_data="lang_ru"),\
         InlineKeyboardButton("English", callback_data="lang_en")]\
    ]\
    reply_markup = InlineKeyboardMarkup(keyboard)\
    update.message.reply_text("\uc0\u1042 \u1099 \u1073 \u1077 \u1088 \u1080 \u1090 \u1077  \u1103 \u1079 \u1099 \u1082  / Choose a language:", reply_markup=reply_markup)\
\
# \uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1095 \u1080 \u1082  \u1074 \u1099 \u1073 \u1086 \u1088 \u1072  \u1103 \u1079 \u1099 \u1082 \u1072 \
def select_language(update: Update, context: CallbackContext):\
    query = update.callback_query\
    query.answer()\
\
    if query.data == "lang_ru":\
        context.user_data["language"] = "ru"\
        query.edit_message_text(\
            "\uc0\u1057 \u1087 \u1072 \u1089 \u1080 \u1073 \u1086 , \u1095 \u1090 \u1086  \u1088 \u1077 \u1096 \u1080 \u1083 \u1080  \u1087 \u1086 \u1087 \u1088 \u1086 \u1073 \u1086 \u1074 \u1072 \u1090 \u1100  \u1085 \u1072 \u1096  \u1073 \u1086 \u1090 ! \u1044 \u1083 \u1103  \u1085 \u1072 \u1095 \u1072 \u1083 \u1072 , \u1087 \u1086 \u1078 \u1072 \u1083 \u1091 \u1081 \u1089 \u1090 \u1072 , \u1087 \u1086 \u1076 \u1087 \u1080 \u1096 \u1080 \u1090 \u1077 \u1089 \u1100  \u1085 \u1072  \u1101 \u1090 \u1086 \u1090  \u1082 \u1072 \u1085 \u1072 \u1083 : https://t.me/mrsaforost"\
        )\
    elif query.data == "lang_en":\
        context.user_data["language"] = "en"\
        query.edit_message_text(\
            "Thank you for trying our bot! To get started, please subscribe to this channel: https://t.me/rostifeoth"\
        )\
\
    # \uc0\u1055 \u1088 \u1086 \u1074 \u1077 \u1088 \u1082 \u1072  \u1087 \u1086 \u1076 \u1087 \u1080 \u1089 \u1082 \u1080  (\u1079 \u1072 \u1075 \u1083 \u1091 \u1096 \u1082 \u1072 )\
    # \uc0\u1055 \u1086 \u1089 \u1083 \u1077  \u1087 \u1086 \u1076 \u1090 \u1074 \u1077 \u1088 \u1078 \u1076 \u1077 \u1085 \u1080 \u1103  \u1087 \u1086 \u1076 \u1087 \u1080 \u1089 \u1080  \u1074 \u1099 \u1079 \u1074 \u1072 \u1090 \u1100  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1102  check_provinces\
\
# \uc0\u1055 \u1088 \u1086 \u1074 \u1077 \u1088 \u1082 \u1072  \u1087 \u1088 \u1086 \u1074 \u1080 \u1085 \u1094 \u1080 \u1081 \
def check_provinces(update: Update, context: CallbackContext):\
    lang = context.user_data.get("language", "en")\
    visited = user_data.get(update.effective_user.id, [])\
    available = [prov for prov in provinces[lang] if prov not in visited]\
\
    if not available:\
        update.message.reply_text(\
            "\uc0\u1042 \u1099  \u1091 \u1078 \u1077  \u1087 \u1086 \u1089 \u1077 \u1090 \u1080 \u1083 \u1080  \u1074 \u1089 \u1077  \u1087 \u1088 \u1086 \u1074 \u1080 \u1085 \u1094 \u1080 \u1080 !" if lang == "ru" else "You have already visited all provinces!"\
        )\
        return\
\
    keyboard = [[InlineKeyboardButton(prov, callback_data=f"province_\{prov\}") for prov in available]]\
    reply_markup = InlineKeyboardMarkup(keyboard)\
\
    update.message.reply_text(\
        "\uc0\u1042 \u1099 \u1073 \u1077 \u1088 \u1080 \u1090 \u1077  \u1087 \u1088 \u1086 \u1074 \u1080 \u1085 \u1094 \u1080 \u1102 , \u1074  \u1082 \u1086 \u1090 \u1086 \u1088 \u1086 \u1081  \u1074 \u1099  \u1073 \u1099 \u1083 \u1080 :" if lang == "ru" else "Select a province you have visited:",\
        reply_markup=reply_markup\
    )\
\
# \uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1095 \u1080 \u1082  \u1074 \u1099 \u1073 \u1086 \u1088 \u1072  \u1087 \u1088 \u1086 \u1074 \u1080 \u1085 \u1094 \u1080 \u1080 \
def select_province(update: Update, context: CallbackContext):\
    query = update.callback_query\
    query.answer()\
\
    province = query.data.replace("province_", "")\
    user_id = update.effective_user.id\
\
    if user_id not in user_data:\
        user_data[user_id] = []\
\
    user_data[user_id].append(province)\
\
    lang = context.user_data.get("language", "en")\
    visited = len(user_data[user_id])\
    total = len(provinces[lang])\
    progress = (visited / total) * 100\
\
    query.edit_message_text(\
        f"\uc0\u1055 \u1088 \u1086 \u1075 \u1088 \u1077 \u1089 \u1089 : \{visited\}/\{total\} \u1087 \u1088 \u1086 \u1074 \u1080 \u1085 \u1094 \u1080 \u1081  (\{progress:.2f\}%)" if lang == "ru" else \\\
        f"Progress: \{visited\}/\{total\} provinces (\{progress:.2f\}%)"\
    )\
\
# \uc0\u1054 \u1089 \u1085 \u1086 \u1074 \u1085 \u1072 \u1103  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1103 \
def main():\
    updater = Updater("
\f1\fs20\fsmilli10010 7761938356:AAHmFF40Kd8qNRONnfGFNgtP2-cUzQsDmL8
\f0\fs24 ")\
\
    updater.dispatcher.add_handler(CommandHandler("start", start))\
    updater.dispatcher.add_handler(CallbackQueryHandler(select_language, pattern="^lang_"))\
    updater.dispatcher.add_handler(CallbackQueryHandler(select_province, pattern="^province_"))\
\
    updater.start_polling()\
    updater.idle()\
\
if __name__ == "__main__":\
    main()}