import requests
from datetime import datetime
import telebot
from auth_data import token

def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_prise = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%m')}\nSell BTC price: {sell_prise}")

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Write the 'price' to find out the cost of BTC")
        bot.send_photo(message.chat.id, open('Bitcoin2.jpg', 'rb'))

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "/price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_prise = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%m')}\nSell BTC price: {sell_prise}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn...Something was wrong..."
                )

        else:
            bot.send_message(message.chat.id, "Whaaat??? Chack the command dude!")

    bot.polling()

if __name__ == '__main__':
    # get_data()
    telegram_bot(token)
