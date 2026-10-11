import telebot
import requests

TOKEN = "ضع_التوكن_هنا"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "أهلاً بك في بوت نور ✨\nأرسل أي رسالة وسأرد عليك")

@bot.message_handler(func=lambda m: True)
def reply(m):
    try:
        text = m.text
        url = f"https://api.simsimi.net/v2/?text={text}&lc=ar&cf=false"
        r = requests.get(url).json()
        ans = r.get('success', 'ما فهمت، ممكن تعيد؟')
        bot.reply_to(m, ans)
    except:
        bot.reply_to(m, "أهلاً بك يا غالي، كيف أقدر أساعدك؟")

bot.infinity_polling()
