import pyttsx3

# Inicializa a engine de síntese de fala
engine = pyttsx3.init()

# Fala uma mensagem de boas-vindas ao iniciar o programa
engine.say("Bem-vindo! Eu sou um programa desenvolvido em Python que fala o que for escrito pelo usuário.")
engine.runAndWait()

while True:
    texto = input("Digite algo: ")
    
    if texto.lower() == "sair":
        # Fala uma mensagem de despedida antes de encerrar o programa
        engine.say("Encerrando o programa. Obrigado por utilizar nosso serviço!")
        engine.runAndWait()
        break
        
    engine.say(texto)
    engine.runAndWait()
    
    while True:
        repetir = input("Deseja repetir o que foi dito? (sim/não) ")
        
        if repetir.lower() == "sim":
            engine.say(texto)
            engine.runAndWait()
            break
        elif repetir.lower() == "não":
            break
        else:
            print("Opção inválida! Por favor, digite 'sim' ou 'não'.")    