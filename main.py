from pyrogram import Client, filters
from pyrogram.types import Message
from googletrans import Translator
from plugin import *

app = Client("translate_bot", api_hash=api__hash, api_id=api__id)


@app.on_message(filters.chat("mytesttrsttest"))
def my_channel(client: Client, message: Message):
    translator = Translator()
    # translate message
    translated_meesage = translator.translate(message.text, src="en", dest="fa").text
    # send to new chanell
    client.send_message(chat_id="testtestmtest",
                        text=(

                            f"**{translated_meesage}** \n\n\n (ساخته شده توسط سیدمحمدصالح مصطفایی و مهدی آقایی)"

                        )
                        )
    print("original text :", message.text)
    print("translated text :", translated_meesage)


app.run()
