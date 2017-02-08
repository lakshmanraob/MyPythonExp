import logging
from telegram.ext import Updater
import pyrebase

updater = Updater(token='304998522:AAH0rrkQC-GdH2MWDT7CTmq_wtCXZF71_3Y')

dispatcher = updater.dispatcher

# start
def start(bot, update):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    bot.sendMessage(chat_id=update.message.chat_id, text='I am bot, please talk to me')


from telegram.ext import Handler
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# Echo handling - any message will echoed back to you
def echo(bot, update):
    print(update.message.text)
    simpleMessage = ''
    if (update.message.text == 'hotel'):
        simpleMessage = "this is hotel"
    else:
        simpleMessage = update.message.text
    bot.sendMessage(chat_id=update.message.chat_id, text=simpleMessage)
    # update.message.reply_text("general message")


from telegram.ext import MessageHandler, Filters

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


# caps handler /caps
def caps(bot, update, args):
    print(args)
    simpleMessgae = ''.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=simpleMessgae)


caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)


# addition of two integers
def add(bot, update, args):
    print("add", args)
    simpleMessage = ''
    if len(args) == 2:
        if checkInt(args[0]) and checkInt(args[1]):
            simpleMessage = int(args[0]) + int(args[1])
        elif checkFloat(args[0]) and checkFloat(args[1]):
            simpleMessage = float(args[0]) + float(args[1])
        else:
            simpleMessage = args[0] + "" + args[1]
    else:
        simpleMessage = "Need two arguments to get results"

    print(simpleMessage)
    bot.sendMessage(chat_id=update.message.chat_id, text=simpleMessage)


def checkInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def checkFloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

add_handler = CommandHandler('add', add, pass_args=True)
dispatcher.add_handler(add_handler)

# inline Results article
from telegram import InlineQueryResultArticle,InputTextMessageContent
def inline_caps(bot,update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(InlineQueryResultArticle(id=query.upper(),
                                            title='caps',
                                            input_message_content=InputTextMessageContent(query.upper())))

    bot.answerInlineQuery(update.inline_query.id,results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


def deviceStatus(bot, update, args):
    print(args[0])
    # workInprogess = "Status is unknown right now"
    workInprogess = getStatus(samplename=args[0])
    bot.sendMessage(chat_id=update.message.chat_id, text=workInprogess)


def getStatus(samplename):
        print("firebase", samplename)
        config = {
            "apiKey": "AIzaSyAPjtYSivTfIVEti8nZxcqAH-ykwWWzps0",
            "authDomain": "fbauthentication-9b3a2.firebaseapp.com",
            "databaseURL": "https://fbauthentication-9b3a2.firebaseio.com",
            "storageBucket": "fbauthentication-9b3a2.appspot.com",
        };

        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()

        user = auth.sign_in_with_email_and_password("lak@z1.com", "Dev12345")

        print(user)

        db = firebase.database()

        # parsed_json = json.loads(db.child('sampleList').get(user['idToken']).val()[])

        samplelist = db.child('sampleList').get(user['idToken']).val()

        sampleStatus = "sampleSattsu"

        for sample in samplelist:
            if sample['modelString'] == samplename:
                if sample['status'] == 'available':
                    sampleStatus = sample['modelString'] + " is available"
                    return sampleStatus
                else:
                    sampleStatus = sample['modelString'] + " is enagaged"
                    return sampleStatus
            else:
                sampleStatus = samplename + " is not available"
        return sampleStatus



status_handler = CommandHandler("status", deviceStatus, pass_args=True)
dispatcher.add_handler(status_handler)


def deviceHistory(bot, update, args):
    print(args)
    workInprogess = "History is unknown right now"
    bot.sendMessage(chat_id=update.message.chat_id, text=workInprogess)


history_handler = CommandHandler("history", deviceHistory, pass_args=True)
dispatcher.add_handler(history_handler)


updater.start_polling()
