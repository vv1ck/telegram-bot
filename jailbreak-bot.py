
from telegram import *
from telegram.ext import *
from telegram.ext import Updater
import telegram
MYtoken = input('Enter your token: ')
reng1 = range(1)
iphn,ipd,ipd2,bck,bck2,ip6,ip12,ip11,ipXS,Allios, noj, yUN,yUT,UOD,crn,crUN,cte,all2,crUN2,ipdMIN5,ipdMIN5_2,air4,ipd7,ipd7_2,UDCK,ipdPRO,webJB,ipdPR4,ipdPR4_2= range(29)

def hlpe(update,context):
    ms = """
طريقة استخدام البوت:
اكتب info/ بعدها اختار نوع جهازك بعدها اصدار الجهاز وبس هذا كل شيء (:

How to use the bot :
Type the command /info Then choose your device type and version. 
That's it (:
    """
    update.message.bot.send_message(chat_id=update.message.chat_id,text="{}".format(ms))

def src(update,context):
    ms = """
bot version : 1.2
Developer : @JJNN1
The Source: github.com/vv1ck/telegram-bot"""
    update.message.bot.send_message(chat_id=update.message.chat_id,text="{}".format(ms),parse_mode=telegram.ParseMode.MARKDOWN)
def idd(update,context):
    iDD = update.message.chat_id
    ID = str(iDD)
    ms = "chat id : {}".format(ID)
    update.message.bot.send_message(chat_id=update.message.chat_id,text="{}".format(ms),parse_mode=telegram.ParseMode.MARKDOWN)

def Done(update,context):
    ms = """
لاستخدام البوت اكتب
/info

لمعرفة طريقة استخدام البوت اكتب
/help
    """
    update.message.bot.send_message(chat_id=update.message.chat_id,text="{}".format(ms))
def noNB(update,context):
    query = update.callback_query
    msg = """
اصدارك لايدعم الجلبريك !
Your version does not support the 
                """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1
def UNKFR(update,context):
    query = update.callback_query
    msg = """
يدعم جلبريك انكفر
Supports jailbreak Unc0ver 
                """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
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
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1
def UODS(update,context):
    query = update.callback_query
    msg = """
يدعم جلبريك انكفر و اوديسي
Supports jailbreak Unc0ver & Odyssey
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1
def UODS2(update,context):
    query = update.callback_query
    msg = """
يدعم جلبريك انكفر و اوديسي و شكرين
Supports jailbreak Unc0ver & Odyssey & Checkra1n
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1
def Ckren(update,context):
    query = update.callback_query
    msg = """
يدعم جلبريك  شكرين
Supports jailbreak Checkra1n
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1
def CkrUN(update,context):
    query= update.callback_query
    msg = """
يدعم جلبريك انكفر و شكرين
Supports jailbreak Unc0ver & Checkra1n
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1
def CkrUN2(update,context):
    query= update.callback_query
    msg = """
يدعم جلبريك انكفر و شكرين و تورين
Supports jailbreak Unc0ver & Checkra1n & Taurine
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1
def ckte(update,context):
    query= update.callback_query
    msg = """
يدعم جلبريك الكترا و تور و شكرين و انكفر 
Supports jailbreak Electra & Th0r & Checkra1n & Unc0ver
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1

def webJLB(update,context):
    query = update.callback_query
    msg = """
مواقع تنزيل تطبيقات تفعيل الجلبريك :
Jailbreak Apps Download Sites:

1- ipa-apps.me

2- https://app.app-valley.vip

3- https://tutubox.io

4- https://app.eonhubapp.com/apps/jailbreak.php
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1


def ipad7_2(update,context):
    query = update.callback_query
    msg = """
اختر اصدار الipad الخاص بك :

Choose your iPad version: 
            """
    Keyboard = [
        [InlineKeyboardButton("ios 14.8", callback_data=str(crn))],
        [InlineKeyboardButton("ios 14.7", callback_data=str(crn)),
         InlineKeyboardButton("ios 14.6", callback_data=str(crn)),
         InlineKeyboardButton("ios 14.5.1",callback_data=str(crn))],
        [InlineKeyboardButton("ios 14.5", callback_data=str(crn)),
         InlineKeyboardButton("ios 14.4.2", callback_data=str(crn))],
        [InlineKeyboardButton("ios 14.4.1", callback_data=str(crn)),
        InlineKeyboardButton("ios 14.3", callback_data=str(crUN2))],
         [InlineKeyboardButton("ios 14.2.1", callback_data=str(crUN2)),
        InlineKeyboardButton("ios 14.2", callback_data=str(crUN2)),
         InlineKeyboardButton("ios 14.1", callback_data=str(crUN2))],
         [InlineKeyboardButton("GO BACK ", callback_data=str(ipd7))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard) 
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
def ipad7(update,context):
    query = update.callback_query
    msg = """
اختر اصدار الipad الخاص بك :

Choose your iPad version: 
            """
    Keyboard = [
        [InlineKeyboardButton("ios 14.0", callback_data=str(crUN2)),
         InlineKeyboardButton("ios 13.7", callback_data=str(UDCK)),
        InlineKeyboardButton("ios 13.6.1", callback_data=str(UDCK))],
         [InlineKeyboardButton("ios 13.6", callback_data=str(UDCK)),
         InlineKeyboardButton("ios 13.5.1", callback_data=str(UDCK)),
        InlineKeyboardButton("ios 13.5", callback_data=str(UDCK))],
         [InlineKeyboardButton("ios 13.4.1", callback_data=str(UDCK)),
         InlineKeyboardButton("ios 13.4", callback_data=str(UDCK)),
        InlineKeyboardButton("ios 13.3.1", callback_data=str(UDCK))],
         [InlineKeyboardButton("ios 13.3", callback_data=str(UDCK))],
        [InlineKeyboardButton("More | المزيد", callback_data=str(ipd7_2))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(ipd))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)



def ipadPRO(update,context):
    query = update.callback_query
    msg = """
اختر اصدار الipad الخاص بك :

Choose your iPad version: 
            """
    Keyboard = [
        [InlineKeyboardButton("ios 13", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.8", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.7.1", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.7", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.6", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.5.1",callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.5", callback_data=str(noj))],
         [InlineKeyboardButton("GO BACK ", callback_data=str(ipd))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)

def ipad_air4(update,context):
    query = update.callback_query
    msg = """
اختر اصدار الipad الخاص بك :

Choose your iPad version: 
            """
    Keyboard = [
        [InlineKeyboardButton("ios 13", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.8", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.7", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.6", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.5.1",callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.5", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.4.2", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.4.1", callback_data=str(noj)),
        InlineKeyboardButton("ios 14.3", callback_data=str(yUT))],
         [InlineKeyboardButton("ios 14.2.1", callback_data=str(yUT)),
        InlineKeyboardButton("ios 14.2", callback_data=str(yUT)),
         InlineKeyboardButton("ios 14.1", callback_data=str(yUT))],
         [InlineKeyboardButton("GO BACK ", callback_data=str(ipd))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)

def ipadMIN5_2(update,context):
    query= update.callback_query
    msg = """
اختر اصدار الipad الخاص بك :

Choose your iPad version: 
            """
    Keyboard = [
    [InlineKeyboardButton("ios 13", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.8", callback_data=str(noj))],
    [InlineKeyboardButton("ios 14.7", callback_data=str(noj)),
     InlineKeyboardButton("ios 14.6", callback_data=str(noj))],
    [InlineKeyboardButton("ios 14.5.1",callback_data=str(noj)),
     InlineKeyboardButton("ios 14.5", callback_data=str(noj))],
    [InlineKeyboardButton("ios 14.4.2", callback_data=str(noj)),
     InlineKeyboardButton("ios 14.4.1", callback_data=str(noj))],
    [InlineKeyboardButton("ios 14.3", callback_data=str(yUT))],
    [InlineKeyboardButton("ios 14.2.1", callback_data=str(yUT)),
     InlineKeyboardButton("ios 14.2", callback_data=str(yUT))],
    [InlineKeyboardButton("ios 14.1", callback_data=str(yUT)),
     InlineKeyboardButton("ios 14.0.1", callback_data=str(yUT))],
    [InlineKeyboardButton("ios 14.0", callback_data=str(yUT)),
     InlineKeyboardButton("ios 13.7", callback_data=str(UOD))],
    [InlineKeyboardButton("GO BACK ", callback_data=str(ipdMIN5))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)


def ipadPRO4_2(update,context):
    query= update.callback_query
    msg = """
اختر اصدار الipad الخاص بك :

Choose your iPad version:
            """
    Keyboard = [
        [InlineKeyboardButton("ios 13", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.8", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.7", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.6", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.5.1",callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.5", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.4.2", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.4.1", callback_data=str(noj)),
        InlineKeyboardButton("ios 14.3", callback_data=str(yUT))],
         [InlineKeyboardButton("ios 14.2.1", callback_data=str(yUT)),
        InlineKeyboardButton("ios 14.2", callback_data=str(yUT))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(ipdPR4))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)

def ipadPRO4(update,context):
    query= update.callback_query
    msg = """
اختر اصدار الipad الخاص بك :

Choose your iPad version:
            """
    Keyboard = [
    [InlineKeyboardButton("ios 14.1", callback_data=str(yUT)),
     InlineKeyboardButton("ios 14.0.1", callback_data=str(yUT))],
    [InlineKeyboardButton("ios 14", callback_data=str(yUT)),
     InlineKeyboardButton("ios 13.7", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 13.6.1", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.6", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 13.5.1", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.5", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 13.4.1", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.4", callback_data=str(UOD))],
    [InlineKeyboardButton("More | المزيد", callback_data=str(ipdPR4_2))],
    [InlineKeyboardButton("GO BACK ", callback_data=str(ipd))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg),reply_markup=pnoe1)
def ipadMIN5(update,context):
    query= update.callback_query
    msg = """
اختر اصدار الipad الخاص بك :

Choose your iPad version:
            """
    Keyboard = [
    
    [InlineKeyboardButton("ios 13.6.1", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.6", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 13.5.1", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.5", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 13.4.1", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.4", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 13.3.1", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.3", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 13.2.3", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.2.2", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 13.2", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.1.3", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 13.1.2", callback_data=str(UOD)),
     InlineKeyboardButton("ios 13.1.1", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 12.4.1", callback_data=str(UOD)),
     InlineKeyboardButton("ios 12.4", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 12.3.1", callback_data=str(UOD)),
     InlineKeyboardButton("ios 12.3", callback_data=str(UOD))],
    [InlineKeyboardButton("ios 12.2", callback_data=str(UOD))],
    [InlineKeyboardButton("More | المزيد", callback_data=str(ipdMIN5_2))],
    [InlineKeyboardButton("GO BACK ", callback_data=str(ipd))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)

def ipad2(update,context):
    query= update.callback_query
    msg = """
سيتم اضافة هذا القسم قريبا ☑️
This section will be added soon
            """
    Keyboard = [
        [InlineKeyboardButton("GO BACK ", callback_data=str(ipd))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1

def ipad(update,context):
    query= update.callback_query
    msg = """
اختر نوع الipad الخاص بك من الازرار :

Choose your iPad type from the buttons :
            """
    Keyboard = [
         [InlineKeyboardButton("ipad Pro (11-inc|5th gener..)",callback_data=str(ipdPRO))],
        [InlineKeyboardButton("ipad Pro (12.9-inc|3rd gener..)",callback_data=str(ipdPRO))],
        [InlineKeyboardButton("ipad Pro 4 (11-inc|WiFi)",callback_data=str(ipdPR4))],
        [InlineKeyboardButton("ipad Pro 4 (12.9-inc|Cellular)",callback_data=str(ipdPR4))],
        [InlineKeyboardButton("ipad 8 (WiFi)",callback_data=str(air4)),
         InlineKeyboardButton("ipad 8 (Cellular)",callback_data=str(air4))],
        [InlineKeyboardButton("ipad 7 (WiFi)",callback_data=str(ipd7)),
         InlineKeyboardButton("ipad 7 (Cellular)",callback_data=str(ipd7))],
        [InlineKeyboardButton("ipad Air 4 (WiFi)",callback_data=str(air4)),
         InlineKeyboardButton("ipad Air 4 (Cellular)",callback_data=str(air4))],
        [InlineKeyboardButton("ipad Air 3 (WiFi)",callback_data=str(ipdMIN5)),
         InlineKeyboardButton("ipad Air 3 (Cellular)",callback_data=str(ipdMIN5))],
        [InlineKeyboardButton("ipad mini 5 (WiFi)",callback_data=str(ipdMIN5)),
         InlineKeyboardButton("ipad mini 5 (Cellular)",callback_data=str(ipdMIN5))],
        [InlineKeyboardButton("More | المزيد", callback_data=str(ipd2))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck))]]
    pnoe1 = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
def iponALL2(update,context):
    query = update.callback_query
    msg = f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("ios 13", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.8", callback_data=str(crn))],
        [InlineKeyboardButton("ios 14.7", callback_data=str(crn)),
        InlineKeyboardButton("ios 14.6", callback_data=str(crn)),
        InlineKeyboardButton("ios 14.5.1",callback_data=str(crn))],
        [InlineKeyboardButton("ios 14.5", callback_data=str(crn)),
         InlineKeyboardButton("ios 14.4.2", callback_data=str(crn)),
         InlineKeyboardButton("ios 14.4.1", callback_data=str(crn))],
         [InlineKeyboardButton("ios 14", callback_data=str(crn)),
        InlineKeyboardButton("ios 14.3", callback_data=str(crUN)),
         InlineKeyboardButton("ios 14.2.1", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 14.2", callback_data=str(crUN)),
        InlineKeyboardButton("ios 14.1", callback_data=str(crUN)),
        InlineKeyboardButton("ios 14.0.1", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 14.0", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.7", callback_data=str(crUN)),
        InlineKeyboardButton("ios 13.6.1", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 13.6", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.5.1", callback_data=str(crUN)),
        InlineKeyboardButton("ios 13.5", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 13.4.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.4", callback_data=str(crUN)),
        InlineKeyboardButton("ios 13.3.1", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 13.3", callback_data=str(crUN))],
         [InlineKeyboardButton("GO BACK ", callback_data=str(Allios))]]
    pnoe = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe)

def iponALL(update,context):
    query = update.callback_query
    msg = f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
         [InlineKeyboardButton("ios 13.2.3", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.2.2", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 13.2", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.1.3", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 13.1.2", callback_data=str(crUN)),
         InlineKeyboardButton("ios 13.1.1", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 13.1", callback_data=str(crUN)),
          InlineKeyboardButton("ios 13.0", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.4.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.4", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 12.3.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.3", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.2", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.1.4", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 12.1.3", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.1.2", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 12.1.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.1", callback_data=str(crUN))],
         [InlineKeyboardButton("ios 12.0.1", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.0", callback_data=str(crUN))],
        [InlineKeyboardButton("ios 11.4.1", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.4", callback_data=str(cte))],
         [InlineKeyboardButton("ios 11.3.1", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.3", callback_data=str(cte))],
        [InlineKeyboardButton("ios 11.2.6", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.2.5", callback_data=str(cte))],
         [InlineKeyboardButton("ios 11.2.2", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.2.1", callback_data=str(cte))],
        [InlineKeyboardButton("ios 11.2", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.1.2", callback_data=str(cte))],
         [InlineKeyboardButton("ios 11.1.1", callback_data=str(cte)),
         InlineKeyboardButton("ios 11.1", callback_data=str(cte))],
        [InlineKeyboardButton("More | المزيد", callback_data=str(all2))],
        [InlineKeyboardButton("GO BACK ", callback_data=str(bck2))]]
    pnoe = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe)
def iponXS(update,context):
    query = update.callback_query
    msg= f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("ios 13", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.8", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.7", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.6", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.5.1",callback_data=str(noj))],
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
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe)
def ipon11(update,context):
    query = update.callback_query
    msg = f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("ios 13", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.8", callback_data=str(noj))],
        [InlineKeyboardButton("ios 14.7", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.6", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.5.1", callback_data=str(noj))],
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
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe)
def ipon12(update,context: CallbackContext) -> None:
    query = update.callback_query
    msg = f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [

        [InlineKeyboardButton("ios 14.8", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.7", callback_data=str(noj))],
         [InlineKeyboardButton("ios 14.6", callback_data=str(noj)),
         InlineKeyboardButton("ios 14.5.1", callback_data=str(noj))],
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
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe1)
    return reng1
def ipon6(update,context):
    query = update.callback_query
    msg = f"""
ما هو اصدار جهازك ؟
What is the version of your device?
➖➖➖➖➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("ios 12.5.4", callback_data=str(crUN)),
         InlineKeyboardButton("ios 12.5.3", callback_data=str(crUN))],
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
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe)


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
        [InlineKeyboardButton("iphone X", callback_data=str(Allios)),
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
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe)
def start(update,context: CallbackContext) -> None:
    msg = f"""
ٰ           حدد نوع جهازك  📲
Select your device type 📲
➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("iphone | 🔘 | ايفون", callback_data=str(iphn))],
        [InlineKeyboardButton("  ipad | 🔘 | ايباد", callback_data=str(ipd))],
        [InlineKeyboardButton("Jailbreak Certificate", callback_data=str(webJB))]]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    update.message.bot.send_message(chat_id=update.message.chat_id,text="{}".format(msg), reply_markup=reply_markup)
    return reng1
def back(update,context: CallbackContext) -> None:
    query = update.callback_query
    msg = f"""
ٰ           حدد نوع جهازك  📲
Select your device type 📲
➖➖➖➖➖➖"""
    Keyboard = [
        [InlineKeyboardButton("iphone | 🔘 | ايفون", callback_data=str(iphn))],
        [InlineKeyboardButton("  ipad | 🔘 | ايباد", callback_data=str(ipd))],
        [InlineKeyboardButton("Jailbreak Certificate", callback_data=str(webJB))]]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(text="{}".format(msg), reply_markup=reply_markup)
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
        [InlineKeyboardButton("iphone X", callback_data=str(Allios)),
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
    query.edit_message_text(text="{}".format(msg), reply_markup=pnoe)
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
                CallbackQueryHandler(UODS2, pattern='^' + str(UDCK) + '$', run_async=True),
                CallbackQueryHandler(Ckren, pattern='^' + str(crn) + '$', run_async=True),
                CallbackQueryHandler(CkrUN2, pattern='^' + str(crUN2) + '$', run_async=True),
                CallbackQueryHandler(CkrUN, pattern='^' + str(crUN) + '$', run_async=True),
                CallbackQueryHandler(ckte, pattern='^' + str(cte) + '$', run_async=True),
                CallbackQueryHandler(webJLB, pattern='^' + str(webJB) + '$', run_async=True),
                CallbackQueryHandler(ipad, pattern='^' + str(ipd) + '$', run_async=True),
                CallbackQueryHandler(ipad2, pattern='^' + str(ipd2) + '$', run_async=True),
                CallbackQueryHandler(ipon6, pattern='^' + str(ip6) + '$', run_async=True),
                CallbackQueryHandler(ipon12, pattern='^' + str(ip12) + '$', run_async=True),
                CallbackQueryHandler(ipon11, pattern='^' + str(ip11) + '$', run_async=True),
                CallbackQueryHandler(iponALL, pattern='^' + str(Allios) + '$', run_async=True),
                CallbackQueryHandler(iponALL2, pattern='^' + str(all2) + '$', run_async=True),
                CallbackQueryHandler(iponXS, pattern='^' + str(ipXS) + '$', run_async=True),
                CallbackQueryHandler(ipadMIN5, pattern='^' + str(ipdMIN5) + '$', run_async=True),
                CallbackQueryHandler(ipadMIN5_2, pattern='^' + str(ipdMIN5_2) + '$', run_async=True),
                CallbackQueryHandler(ipad_air4, pattern='^' + str(air4) + '$', run_async=True),
                CallbackQueryHandler(ipad7, pattern='^' + str(ipd7) + '$', run_async=True),
                CallbackQueryHandler(ipad7_2, pattern='^' + str(ipd7_2) + '$', run_async=True),
                CallbackQueryHandler(ipadPRO, pattern='^' + str(ipdPRO) + '$', run_async=True),
                CallbackQueryHandler(ipadPRO4, pattern='^' + str(ipdPR4) + '$', run_async=True),
                CallbackQueryHandler(ipadPRO4_2, pattern='^' + str(ipdPR4_2) + '$', run_async=True),
                CallbackQueryHandler(back2, pattern='^' + str(bck2) + '$', run_async=True),
                CallbackQueryHandler(back, pattern='^' + str(bck) + '$',run_async=True),]},
        fallbacks=[CommandHandler('info', start)],)
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(CommandHandler('start', Done, run_async=True))
    dispatcher.add_handler(CommandHandler('source', src, run_async=True))
    dispatcher.add_handler(CommandHandler('help', hlpe, run_async=True))
    dispatcher.add_handler(CommandHandler('chat', idd, run_async=True))
    try:
        updater.start_polling(timeout=999999)
        updater.idle()
    except telegram.error.Unauthorized:
        print("Error !!")
startBOT()
