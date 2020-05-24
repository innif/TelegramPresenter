import telegram.ext # import Telegram-API
import autopy       # imports library to simulate keypresses
def message(update, context):   # callback-methos
    if update.message.text == '+': autopy.key.tap(autopy.key.Code.RIGHT_ARROW)  # tap right-key if + is received
    if update.message.text == '-': autopy.key.tap(autopy.key.Code.LEFT_ARROW)   # tap left-key if - is received
updater = telegram.ext.Updater('put your API-Key here', use_context=True)       # creates the Telegram-Bot
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message)) # add handler for incomming messages
updater.start_polling() # starts listining
updater.idle()