import random

class ChatBot:
    def __init__(self, nome):
        self.nome = nome

    def responder(self, mensagem):
        mensagem = mensagem.lower()

        if "oi" in mensagem:
            respostas = [
                "Olá!",
            ]
            return random.choice(respostas)

        elif "piada" in mensagem:
            piadas = [
                "Por que o computador foi ao médico? Porque estava com vírus!",
                "Qual é o café mais perigoso? O ex-presso!",
                "Por que o livro de matemática ficou triste? Porque tinha muitos problemas!"
            ]
            return random.choice(piadas)

        else:
            respostas = [
                "Não entendi.",
                "Pode explicar melhor?",
                "Minha inteligência artificial ainda está aprendendo!"
            ]
            return random.choice(respostas)

class BotEngracado(ChatBot):
    def responder(self, mensagem):
      mensagem = mensagem.lower()
      if "oi" in mensagem:
        return "Olá, humano!"
      elif "piada" in mensagem:
        respostas = [
            "O que o pato disse para a pata? Vem quá!",
            "Era uma vez um pintinho chamado Relam. Quando chovia Relam piava!",
            "Por que a idosa não usa relógio? Porque ela é sem hora!",
        ]
        return random.choice(respostas)
      else:
        return "Meu cérebro cibernético deu tela azul. Pode repetir?"

class BotSerio(ChatBot):
    def responder(self, mensagem):
      mensagem = mensagem.lower()
      if "oi" in mensagem:
        return "Olá, senhor(a)."
      elif "piada" in mensagem:
        return "Eu não brinco em serviço."
      else:
        return "Eu não compreendi o conteúdo da sua mensagem. Por obséquio tente novamente."
bot_list = [
    ChatBot,
    BotEngracado,
    BotSerio
]
bot_choice = random.choice(bot_list)
bot = bot_choice(bot_choice.__name__)

while True:
    usuario = input("Você: ")

    if usuario.lower() == "sair":
        break
    elif usuario.lower() == "trocar":
      bot_choice = random.choice(bot_list)
      bot = bot_choice(bot_choice.__name__)
      continue

    print(f"{bot.nome}: {bot.responder(usuario)}")
