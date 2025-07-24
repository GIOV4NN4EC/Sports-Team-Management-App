import subfunctions as sbf

def manage_players():
    while True:
        print("\nMENU DE GERENCIAMENTO DE JOGADORES")
        print("1. Adicionar Jogador")
        print("2. Listar Jogadores")
        print("3. Editar Jogador")
        print("4. Remover Jogador")
        print("5. Voltar ao Menu Principal")
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
        print("\nPARTIDAS E TREINOS")
        print("1. Agendar Partida")
        print("2. Listar Partidas")
        print("3. Agendar Treino")
        print("4. Listar Treinos")
        print("5. Voltar ao Menu Principal")
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
        print("\nGERENCIAMENTO DE EQUIPAMENTOS")
        print("1. Adicionar Equipamento")
        print("2. Listar Equipamentos")
        print("3. Editar Equipamentos")
        print("4. Remover Equipamento")
        print("5. Voltar ao Menu Principal")
        option = input("Escolha uma opção: ")

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
            print("Opção inválida.")


def manage_finances():
    while True:
        print("\nGERENCIAR FINANÇAS")
        print("1. Registrar Receita")
        print("2. Registrar Despesa")
        print("3. Listar Transações")
        print("4. Gerar Relatório Financeiro")
        print("5. Voltar ao Menu Principal")
        option = input("Escolha uma opção: ")

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
            print("Opção inválida.")

def media_and_social():
    while True:
        print("\nMEDIA AND SOCIAL")
        print("1. Criar Post")
        print("2. Listar Posts")
        print("3. Criar Enquete")
        print("4. Listar Enquetes")
        print("5. Voltar ao Menu Principal")
        option = input("Escolha uma opção: ")

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
            print("Opção inválida.")




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
