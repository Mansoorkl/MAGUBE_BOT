import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Token ka bot-ka ka akhri environment variable
TOKEN = os.getenv("TOKEN", "7714320559:AAFeDlnYpid67psIpP5qdnUjra9V-CRebOU")

def start(update, context):
    update.message.reply_text(
        "👋 Salaan Kusoo dhawoow Magudbe bot 🙌 Waxaan kaa dhigaynaa xirfadle ka xamaasha saaxada shukaansiga!"
    )

def reply(update, context):
    text = update.message.text.lower()

    if "gabar" in text:
        update.message.reply_text("💁‍♀️ Gabdhaha lala hadlo: xishood, kaftan fiican, iyo qadarin 😌")
    elif "wiil" in text:
        update.message.reply_text("🧑 Wiilasha lala hadlo: si degan, qosol badan, ixtiraam leh 😎")
    elif "kaftan" in text:
        update.message.reply_text("😂 Kaftan: Maxaad u malaynaysaa in gabadh iyo wiil isla qaldamaan? Dabeecad ahaan! 😆")
    elif "jawaab" in text:
        update.message.reply_text("✍️ Jawaabta saxda ah waxay ku xirantahay waxaad rabto. Qalbi furan noqo!")
    else:
        update.message.reply_text("🤖 Fadlan sheeg: gabar / wiil / kaftan si aan kuu fahmo.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
