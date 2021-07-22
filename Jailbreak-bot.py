from telegram import *
from telegram.ext import *
from telegram.ext import Updater
MYtoken = input('Enter your token: ')
reng1 = range(1)
iphn,ipd,bck,bck2,ip6,ip12,ip11,ipXS,Allios, noj, yUN,yUT,UOD,crn,crUN,cte= range(16)
def Done(update,context):
    ms = """
Activated ✅
لااستخدام البوت اكتب
/info
    """
    update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{ms} ")
def noNB(update,context):
    query = update.callback_query
    msg = """
اصدارك لايدعم الجلبريك !
Your version does not support the 
                """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe1)
    return reng1
def UNKFR(update,context):
    query = update.callback_query
    msg = """
يدعم جلبريك انكفر
Supports jailbreak Unc0ver 
                """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe1)
    return reng1
def UNtor(update,context):
    query = update.callback_query
    msg = """
يدعم جلبريك انكفر و تورين
Supports jailbreak Unc0ver & Taurine
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe1)
    return reng1
def UODS(update,context):
    query = update.callback_query
    msg = """
يدعم جلبريك انكفر و اوديسي
Supports jailbreak Unc0ver & Odyssey
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe1)
    return reng1
def Ckren(update,context):
    query = update.callback_query
    msg = """
يدعم جلبريك  شكرين
Supports jailbreak Checkra1
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe1)
    return reng1
def CkrUN(update,context):
    query= update.callback_query
    msg = """
يدعم جلبريك انكفر و شكرين
Supports jailbreak Unc0ver & Checkra1
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe1)
    return reng1
def ckte(update,context):
    query= update.callback_query
    msg = """
يدعم جلبريك الكترا و تور و شكرين و انكفر 
Supports jailbreak Electra & Th0r & Checkra1 & Unc0ver
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe1)
    return reng1
def ipad(update,context):
    query= update.callback_query
    msg = """
سيتم اضافة هذا القسم قريبا ☑️
This section will be added soon
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe1)
    return reng1



def iponALL(update,context):
    query = update.callback_query
    msg = f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("ios 14.5", callback_data=str(crn)),
         InlineKeyboardButton("ios 14.4.2", callback_data=str(crn)),
         InlineKeyboardButton("ios 14.4.1", callback_data=str(crn))],
         [InlineKeyboardButton("ios 14", callback_data=str(crn)),
        InlineKeyboardButton("ios 14.3", callback_data=str(crUN)),
         InlineKeyboardButton("ios 14.2.1", callback_data=str(crUN)),
        InlineKeyboardButton("ios 14.2", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 14.1", callback_data=str(crUN)),
        InlineKeyboardButton("ios 14.0.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 14.0", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.7", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 13.6.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.6", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.5.1", callback_data=str(crUN)),
        InlineKeyboardButton("ios 13.5", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 13.4.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.4", callback_data=str(crUN)),
        InlineKeyboardButton("ios 13.3.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.3", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 13.2.3", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.2.2", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.2", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.1.3", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 13.1.2", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.1.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.1", callback_data=str(crUN)),
          InlineKeyboardButton("ios 13.0", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.4.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.4", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.3.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.3", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.2", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.1.4", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.1.3", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.1.2", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.1.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.0.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.0", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 11.4.1", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.4", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.3.1", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.3", callback_data=str(cte))],
        [InlineKeyboardButton("ios 11.2.6", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.2.5", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.2.2", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.2.1", callback_data=str(cte))],
        [InlineKeyboardButton("ios 11.2", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.1.2", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.1.1", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.1", callback_data=str(cte))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe)
def iponXS(update,context):
    query = update.callback_query
    msg= f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("ios 14.5", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.4.2", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.4.1", callback_data=str(noj)),
         InlineKeyboardButton("ios 14", callback_data=str(noj)),
        InlineKeyboardButton("ios 14.3", callback_data=str(yUN))],
         [InlineKeyboardButton("ios 14.2.1", callback_data=str(yUN)),
        InlineKeyboardButton("ios 14.2", callback_data=str(yUN)),
         InlineKeyboardButton("ios 14.1", callback_data=str(yUN))],
        [InlineKeyboardButton("ios 14.0.1", callback_data=str(yUT)),
         InlineKeyboardButton("ios 14.0", callback_data=str(yUT)),
         InlineKeyboardButton("ios 13.7", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.6.1", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.6", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.5.1", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.5", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.4.1", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.4", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.3.1", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.3", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.2.3", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.2.2", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.2", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.1.3", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.1.2", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.1.1", callback_data=str(UOD))],
         [InlineKeyboardButton("ios 13.1", callback_data=str(UOD)),
          InlineKeyboardButton("ios 13.0", callback_data=str(UOD))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe)
def ipon11(update,context):
    query = update.callback_query
    msg = f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("ios 14.5", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.4.2", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.4.1", callback_data=str(noj)),
         InlineKeyboardButton("ios 14", callback_data=str(noj)),
        InlineKeyboardButton("ios 14.3", callback_data=str(yUN))],
         [InlineKeyboardButton("ios 14.2.1", callback_data=str(yUN)),
        InlineKeyboardButton("ios 14.2", callback_data=str(yUN)),
         InlineKeyboardButton("ios 14.1", callback_data=str(yUN))],
        [InlineKeyboardButton("ios 14.0.1", callback_data=str(yUT)),
         InlineKeyboardButton("ios 14.0", callback_data=str(yUT)),
         InlineKeyboardButton("ios 13.7", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.6.1", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.6", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.5.1", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.5", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.4.1", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.4", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.3.1", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.3", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.2.3", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.2.2", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.2", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.1.3", callback_data=str(UOD))],
        [InlineKeyboardButton("ios 13.1.2", callback_data=str(UOD)),
         InlineKeyboardButton("ios 13.1.1", callback_data=str(UOD))],
         [InlineKeyboardButton("ios 13.1", callback_data=str(UOD)),
          InlineKeyboardButton("ios 13.0", callback_data=str(UOD))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe)
def ipon12(update,context: CallbackContext) -> None:
    query = update.callback_query
    msg = f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("ios 14.5", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.4.2", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.4.1", callback_data=str(noj)),
         InlineKeyboardButton("ios 14", callback_data=str(noj)),
        InlineKeyboardButton("ios 14.3", callback_data=str(yUN))],
         [InlineKeyboardButton("ios 14.2.1", callback_data=str(yUN)),
        InlineKeyboardButton("ios 14.2", callback_data=str(yUN)),
         InlineKeyboardButton("ios 14.1", callback_data=str(yUN))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe1)
    return reng1
def ipon6(update,context):
    query = update.callback_query
    msg = f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("ios 12.5.2", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.5.1", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.5", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.4.9", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.4.8", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.4.7", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.4.6", callback_data=str(crUN)),
        InlineKeyboardButton("ios 12.4.5", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 12.4.4", callback_data=str(crUN)),
        InlineKeyboardButton("ios 12.4.3", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.4.2", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.4", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.3.1", callback_data=str(crUN)),
        InlineKeyboardButton("ios 12.3", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 12.2", callback_data=str(crUN)),
        InlineKeyboardButton("ios 12.1.4", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.1.3", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.1.2", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.1.1", callback_data=str(crUN)),
        InlineKeyboardButton("ios 12.1", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 12.0.1", callback_data=str(crUN)),
        InlineKeyboardButton("ios 12.0", callback_data=str(crUN)),
         InlineKeyboardButton("ios 11.4.1", callback_data=str(cte))],
        [InlineKeyboardButton("ios 11.4", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.3.1", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.3", callback_data=str(cte))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe)
def iphone(update,context):
    query = update.callback_query
    msg = f"""
اختار جهازك لمعرفة اذا كان له جلبريك او لا
Choose your device to see if it has a jailbreak or not
➖➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("iphone 12pro max", callback_data=str(ip12)),
         InlineKeyboardButton("iphone 12pro ", callback_data=str(ip12))],
        [InlineKeyboardButton("iphone 12", callback_data=str(ip12))],
        [InlineKeyboardButton("iphone 11pro max", callback_data=str(ip11)),
         InlineKeyboardButton("iphone 11pro", callback_data=str(ip11))],
        [InlineKeyboardButton("iphone 11", callback_data=str(ip11)),
         InlineKeyboardButton("iphone XR", callback_data=str(ipXS))],
        [InlineKeyboardButton("iphone XS max", callback_data=str(ipXS)),
         InlineKeyboardButton("iphone XS", callback_data=str(ipXS))],
        [InlineKeyboardButton("iphone X", callback_data=str(iponALL)),
         InlineKeyboardButton("iphone SE", callback_data=str(Allios))],
        [InlineKeyboardButton("iphone 8 plus", callback_data=str(Allios)),
         InlineKeyboardButton("iphone 8", callback_data=str(Allios))],
        [InlineKeyboardButton("iphone 7 plus", callback_data=str(Allios)),
         InlineKeyboardButton("iphone 7", callback_data=str(Allios))],
        [InlineKeyboardButton("iphone 6s plus", callback_data=str(Allios)),
         InlineKeyboardButton("iphone 6s", callback_data=str(Allios))],
        [InlineKeyboardButton("iphone 6 plus", callback_data=str(ip6)),
         InlineKeyboardButton("iphone 6", callback_data=str(ip6))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe)
def start(update,context: CallbackContext) -> None:
    msg = f"""
ٰ           حدد نوع جهازك  📲
Select your device type 📲
➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("iphone | 🔘 | ايفون", callback_data=str(iphn))],
        [InlineKeyboardButton("  ipad | 🔘 | ايباد", callback_data=str(ipd))]]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    update.message.bot.send_message(chat_id=update.message.chat_id, text=f"{msg} ", reply_markup=reply_markup)
    return reng1
def back(update,context: CallbackContext) -> None:
    query = update.callback_query
    msg = f"""
    ٰ           حدد نوع جهازك  📲
Select your device type 📲
    ➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("iphone | 🔘 | ايفون", callback_data=str(iphn))],
        [InlineKeyboardButton("  ipad | 🔘 | ايباد", callback_data=str(ipd))]]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=reply_markup)
    return reng1
def back2(update,context: CallbackContext) -> None:
    query = update.callback_query
    msg =  f"""
اختار جهازك لمعرفة اذا كان له جلبريك او لا
Choose your device to see if it has a jailbreak or not
➖➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("iphone 12pro max", callback_data=str(ip12)),
         InlineKeyboardButton("iphone 12pro ", callback_data=str(ip12))],
        [InlineKeyboardButton("iphone 12", callback_data=str(ip12))],
        [InlineKeyboardButton("iphone 11pro max", callback_data=str(ip11)),
         InlineKeyboardButton("iphone 11pro", callback_data=str(ip11))],
        [InlineKeyboardButton("iphone 11", callback_data=str(ip11)),
         InlineKeyboardButton("iphone XR", callback_data=str(ipXS))],
        [InlineKeyboardButton("iphone XS max", callback_data=str(ipXS)),
         InlineKeyboardButton("iphone XS", callback_data=str(ipXS))],
        [InlineKeyboardButton("iphone X", callback_data=str(iponALL)),
         InlineKeyboardButton("iphone SE", callback_data=str(Allios))],
        [InlineKeyboardButton("iphone 8 plus", callback_data=str(Allios)),
         InlineKeyboardButton("iphone 8", callback_data=str(Allios))],
        [InlineKeyboardButton("iphone 7 plus", callback_data=str(Allios)),
         InlineKeyboardButton("iphone 7", callback_data=str(Allios))],
        [InlineKeyboardButton("iphone 6s plus", callback_data=str(Allios)),
         InlineKeyboardButton("iphone 6s", callback_data=str(Allios))],
        [InlineKeyboardButton("iphone 6 plus", callback_data=str(ip6)),
         InlineKeyboardButton("iphone 6", callback_data=str(ip6))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text=f"{msg}", reply_markup=pnoe)
def startBOT() -> None:
    updater = Updater(MYtoken, use_context=True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('info', start,run_async=True)],
        states={
            reng1: [
                CallbackQueryHandler(iphone, pattern='^' + str(iphn) + '$',run_async=True),
                CallbackQueryHandler(noNB, pattern='^' + str(noj) + '$', run_async=True),
                CallbackQueryHandler(UNKFR, pattern='^' + str(yUN) + '$', run_async=True),
                CallbackQueryHandler(UNtor, pattern='^' + str(yUT) + '$', run_async=True),
                CallbackQueryHandler(UODS, pattern='^' + str(UOD) + '$', run_async=True),
                CallbackQueryHandler(Ckren, pattern='^' + str(crn) + '$', run_async=True),
                CallbackQueryHandler(CkrUN, pattern='^' + str(crUN) + '$', run_async=True),
                CallbackQueryHandler(ckte, pattern='^' + str(cte) + '$', run_async=True),
                CallbackQueryHandler(ipad, pattern='^' + str(ipd) + '$', run_async=True),
                CallbackQueryHandler(ipon6, pattern='^' + str(ip6) + '$', run_async=True),
                CallbackQueryHandler(ipon12, pattern='^' + str(ip12) + '$', run_async=True),
                CallbackQueryHandler(ipon11, pattern='^' + str(ip11) + '$', run_async=True),
                CallbackQueryHandler(iponALL, pattern='^' + str(Allios) + '$', run_async=True),
                CallbackQueryHandler(iponXS, pattern='^' + str(ipXS) + '$', run_async=True),
                CallbackQueryHandler(back2, pattern='^' + str(bck2) + '$', run_async=True),
                CallbackQueryHandler(back, pattern='^' + str(bck) + '$',run_async=True),]},
        fallbacks=[CommandHandler('info', start)],)
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(CommandHandler('start', Done, run_async=True))
    try:
        updater.start_polling(timeout=999999)
        updater.idle()
    except telegram.error.Unauthorized:
        print("Error !!")
startBOT()
