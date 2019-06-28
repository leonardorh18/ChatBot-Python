from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('JB Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Qual teu nome?', 'Estou Bem', "Como está seu dia?", "Quer conversar" ]

trainer= ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    
    if float(resposta.confidence) > 0.7:
        print('Leo Bot: ', resposta)
    else:
        print('Leo Bot: Ainda não sei responder esta pergunta, mas eu posso aprender com você :)')
