from colorama import Fore, Style

def iniciar_interface(bot):
    print(f"{Fore.CYAN}{bot.botPersonality.getName()}: Olá, estou pronta para servi-lo.{Style.RESET_ALL}")
    while True:
        user_input = input(f"{Fore.GREEN}User: {Style.RESET_ALL}")
        if user_input.lower() in ["sair", "exit"]:
            print(f"{Fore.CYAN}{bot.botPersonality.getName()}: Despedindo-me, mestre.{Style.RESET_ALL}")
            break
        elif user_input.startswith("/personalidade"):
            try:
                _, nome = user_input.split(" ", 1)
                if bot.switchPersonality(nome.strip()):
                    print(f"🔁 Personalidade trocada para: {nome.strip()}")
                else:
                    print("❌ Personalidade não encontrada!")
            except ValueError:
                print("❌ Uso correto: /personalidade <nome>")
            continue

        resposta = bot.botResponse(user_input)
        print(f"{Fore.CYAN}{bot.botPersonality.getName()}: {resposta}{Style.RESET_ALL}")
