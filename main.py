import subfunctions as sbf

def manage_players():
    while True:
        print("\nMENU DE GERENCIAMENTO DE JOGADORES")
        print("1. Adicionar Jogador")
        print("2. Listar Jogadores")
        print("3. Editar Jogador")
        print("4. Remover Jogador")
        print("5. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            sbf.add_player()
        elif opcao == "2":
            sbf.list_players()
        elif opcao == "3":
            sbf.edit_player()
        elif opcao == "4":
            sbf.remove_player()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

def manage_matches():
    while True:
        print("\n--- PARTIDAS E TREINOS ---")
        print("1. Agendar Partida")
        print("2. Listar Partidas")
        print("3. Agendar Treino")
        print("4. Listar Treinos")
        print("5. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            sbf.schedule_match()
        elif opcao == "2":
            sbf.list_matches()
        elif opcao == "3":
            sbf.schedule_training()
        elif opcao == "4":
            sbf.list_trainings()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

def manage_equipment():
    while True:
        print("\n--- EQUIPMENT MANAGEMENT ---")
        print("1. Add Equipment")
        print("2. List Equipment")
        print("3. Edit Equipment")
        print("4. Remove Equipment")
        print("5. Back")
        option = input("Choose: ")

        if option == "1":
            sbf.add_equipment()
        elif option == "2":
            sbf.list_equipment()
        elif option == "3":
            sbf.edit_equipment()
        elif option == "4":
            sbf.remove_equipment()
        elif option == "5":
            break
        else:
            print("Invalid option.")


def manage_finances():
    while True:
        print("\n--- FINANCIAL MANAGEMENT ---")
        print("1. Register Income")
        print("2. Register Expense")
        print("3. List Transactions")
        print("4. Generate Report")
        print("5. Back")
        option = input("Choose: ")

        if option == "1":
            sbf.register_income()
        elif option == "2":
            sbf.register_expense()
        elif option == "3":
            sbf.list_transactions()
        elif option == "4":
            sbf.generate_financial_report()
        elif option == "5":
            break
        else:
            print("Invalid option.")

def media_and_social():
    while True:
        print("\nMEDIA AND SOCIAL")
        print("1. Create Post")
        print("2. List Posts")
        print("3. Create Poll")
        print("4. List Polls")
        print("5. Back")
        option = input("Choose: ")

        if option == "1":
            sbf.create_post()
        elif option == "2":
            sbf.list_posts()
        elif option == "3":
            sbf.create_poll()
        elif option == "4":
            sbf.list_polls()
        elif option == "5":
            break
        else:
            print("Invalid option.")




def main_menu():
    print("\n===== SPORTS TEAM MANAGEMENT APP =====")
    print(" Selecione a opção desejada:")
    print("1. Gerenciar Jogadores")
    print("2. Gerenciar Partidas e Treinos")
    print("3. Gerenciar Equipamentos")
    print("4. Gerenciar Finanças")
    print("5. Mídia e Social")
    print("Digite Q para sair.")

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
