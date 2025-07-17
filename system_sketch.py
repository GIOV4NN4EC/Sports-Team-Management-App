players = []

def manage_players():
    pass

def manage_matches():
    pass

def manage_equipment():
    pass

def manage_finances():
    pass

def media_and_social():
    pass



# Menu principal
def main_menu():
    print("\n===== SPORTS TEAM MANAGEMENT APP =====")
    print("\n Selecione a opção desejada:")
    print("\n1. Gerenciar Jogadores")
    print("\n2. Gerenciar Partidas e Treinos")
    print("\n3. Gerenciar Equipamentos")
    print("\n4. Gerenciar Finanças")
    print("\n5. Mídia e Social")
    print("\nDigite Q para sair.")

def main():
    while True:
        main_menu()
        escolha = input("")

        if escolha == "1":
            manage_players()
        elif escolha == "2":
            manage_matches()
        elif escolha == "3":
            manage_equipment()
        elif escolha == "4":
            manage_finances()
        elif escolha == "5":
            media_and_social()
        elif escolha == "Q":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
