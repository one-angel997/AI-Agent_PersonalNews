from telegram.ext import ApplicationBuilder, CommandHandler
from news_agent import get_tech_news

TOKEN = "INSERISCI_IL_TUO_TOKEN"
# Richiama lo script per ricavare le notizie
async def tech(update, context):
    risposta = get_tech_news()
    await update.message.reply_text("📰 Ultime notizie tech italiane:\n\n" + risposta)

app = ApplicationBuilder().token(TOKEN).build()
# Avvio il ricavo delle notizie sia con il comando /start che /tech
# Il comando /start è quello di default quando la chat è vuota 
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tech", tech))
app.run_polling()
