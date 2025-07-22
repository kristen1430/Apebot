import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from web3 import Web3

BOT_TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID'))
ROUTER_CONTRACT = os.getenv('ROUTER_CONTRACT')
APECHAIN_RPC = os.getenv('APECHAIN_RPC')

w3 = Web3(Web3.HTTPProvider(APECHAIN_RPC))
router_contract = w3.eth.contract(address=Web3.to_checksum_address(ROUTER_CONTRACT), abi=[])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("You are not authorized to use this bot.")
        return
    await update.message.reply_text("Welcome to ApeExpress Bot. Send me a token contract address or link.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("You are not authorized to use this bot.")
        return
    text = update.message.text.strip()
    await update.message.reply_text(f"Received input: {text}. (Buying feature not implemented in this placeholder.)")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
