import telebot
import openai from keys import keys
from gtts import gTTS

openai.api_key=keys.get('gpt')
bot=telebot.TeleBot(keys.get('bot'))
@bot.message_handler(commands=['chat'])
    def handle_chat(message):
        question=message.text[6:]
        response=openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            temperature=0.7,
            top_p=0.7,
            max_tokens=200)
        answer=response['choices'][0]['text']
        print(question)
        bot.send_message(message.chat.id, answer)
        audio(answer)
        bot.send_audio(message.chat.id, audio=open(r'path','rb'), caption='Resposta em áudio')
    def audio(answer):
        tts = gTTS(answer,lang='pt')
        tts.save('s.mp3')

bot.polling()