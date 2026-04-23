from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from news_agent import get_tech_news

TOKEN = "INSERISCI_IL_TUO_TOKEN"

# Comando /start con pulsanti inline
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📰 Ultime Notizie", callback_data="news")],
        [InlineKeyboardButton("🔄 Ricarica", callback_data="reload")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Benvenuto! Scegli un'opzione:",
        reply_markup=reply_markup
    )

# Comando /tech
async def tech(update: Update, context: ContextTypes.DEFAULT_TYPE):
    risposta = get_tech_news()
    await update.message.reply_text("📰 Ultime notizie tech italiane:\n\n" + risposta)

# Gestisci i click sui pulsanti
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "news":
        risposta = get_tech_news()
        await query.edit_message_text("📰 Ultime notizie tech italiane:\n\n" + risposta)
    elif query.data == "reload":
        await start(update, context)

# Configurazione del bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tech", tech))
app.add_handler(CallbackQueryHandler(button_callback))
app.run_polling()
