import random

class ChatBot:
  def __init__(self,nome):
    self.nome = nome

  def responder(self, mensagem):
    mensagem = mensagem.lower()

    if "oi" in mensagem:
      respostas = [
          "Olá!",
          "Seja bem-vindo(a) ao Sistema de Chat Bot!",
          "Seja bem-vindo!"
      ]
      return random.choice(respostas)

    elif "criador" in mensagem:
      return "O criador do Chat Bot é Theo Silva Prado!"

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
          "Pode repetir? Por favor."
      ]
      return random.choice(respostas)

class BotEngracado(ChatBot):

  def responder (self,mensagem):
    mensagem = mensagem.lower()
    if "piada" in mensagem:
      return random.choice([
          "O que o pato disse para a pata? Vem quá!",
          "Era uma vez um pintinho chamado Relam. Quando chovia Relam piava!",
          "Por que a idosa não usa relógio? Porque ela é sem hora!",
      ])

    return super().responder(mensagem)

class BotSerio(ChatBot):

  def responder (self,mensagem):
    mensagem = mensagem.lower()

    if "piada" in mensagem:
      return "Eu não brinco em serviço."

    return super().responder(mensagem)

bot_list = [
    ChatBot,
    BotEngracado,
    BotSerio
]
bot_choice = random.choice(bot_list)
bot = bot_choice(bot_choice.__name__)


try:
    while True:
        usuario = input("Você: ")

        if usuario.lower() == "sair":
            break
        elif usuario.lower() == "trocar":

            removed_bot_class = bot_choice
            bot_list.remove(removed_bot_class)
            bot_choice = random.choice(bot_list)
            bot = bot_choice(bot_choice.__name__)
            bot_list.append(removed_bot_class)

            print(f"Bot trocado com sucesso! Agora você esta conversando com {bot.nome}.")
            continue

        print(f"{bot.nome}: {bot.responder(usuario)}")
except KeyboardInterrupt:
    print("Obrigado por utilizar nossos bots!")
