import telegram.ext
import autopy
def message(update, context):
    if update.message.text == '+': autopy.key.tap(autopy.key.Code.RIGHT_ARROW)
    if update.message.text == '-': autopy.key.tap(autopy.key.Code.LEFT_ARROW)
updater = telegram.ext.Updater('put your API-Key here', use_context=True)
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message))
updater.start_polling()
updater.idle()