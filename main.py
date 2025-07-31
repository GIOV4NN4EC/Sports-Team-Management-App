team = [] #Lista com os jogadores titulares
players = [] #lista de jogadores
recruits = [] #lista de recrutas
matches = [] #lista de eventos partidas
trainings =[] #lista de treinos
equipments = [] #lista de equipamentos
injuried_players = [] #lista de jogadores lesionados
posts = [] #lista de posts
polls = [] #lista de enquetes

class Poll:
    poll_id_counter = 0
    def __init__(self, title, description, opt1, opt2, opt3):
        Poll.poll_id_counter += 1
        self.title = title
        self.description = description
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3
        
class Post:
    post_id_counter = 0
    def __init__(self, title, content, date):
        Post.post_id_counter += 1
        self.title = title
        self.content = content
        self.date = date


class Account:
    def __init__(self, balance):
        self.balance  = balance

class Recruit:
    recruit_id_counter = 0
    def __init__(self, name, age, pros, cons, position, observation):
        Recruit.recruit_id_counter += 1
        self.name = name
        self.age = age
        self.pros = pros
        self.cons = cons
        self.position = position
        self.observation = observation
        
class Equipment:
    equipment_id_counter = 0
    def __init__(self, name, type, quantity, status, observation):
        Equipment.equipment_id_counter += 1
        self.name = name
        self.type = type
        self.quantity = quantity
        self.status = status
        self.observation = observation
        
class Stats:
    def __init__(self, score, games_played):
        self.score = score
        self.games_played = games_played

#Classe para os jogadores
class Player:
    id_inicial = 0 #contador para que não tenham IDs repetidos

    def __init__(self, id, name, age, position, stats, health):
        Player.id_inicial += 1
        self.id = Player.id_inicial #ID único do jogador
        self.name = name #nome do jogador
        self.age = age #idade do jogador
        self.position = position #posição do jogador
        self.stats = stats #estatística do jogador (nesse caso, aproveitamento)
        self.health = health #estado de saúde do jogador

#Classe para os eventos
class Match:
    match_id_counter = 0 #contador para identificar as partidas

    def __init__(self, date, time, opponent, location):
        Match.match_id_counter += 1
        self.id = Match.match_id_counter #ID da partida
        self.date = date #data do evento
        self.time = time #hora
        self.location = location #local da partida
        self.opponent = opponent #oponente (se houver)
        self.result = None  #resultado (se houver)

class Training:
    training_id_counter = 0 #contador para identificar os treinos

    def __init__(self, date, time, location, focus):
        Training.training_id_counter += 1
        self.id = Training.training_id_counter #ID da partida
        self.date = date #data do evento
        self.time = time
        self.location = location #local da partida
        self.focus = focus #objetivo do treino (se houiver)

def add_player():
    name = input("Nome: ")
    age = input("Idade: ")
    position = input("Posição: ")
    
    print("\nInforme as estatísticas do jogador:")
    try:
        score = int(input("Gols marcados: "))
        games_played = int(input("Jogos disputados: "))
    except ValueError:
        print("Valor inválido para estatísticas. Use números inteiros.")
        return
    
    stats = Stats(score, games_played)
    health = input("Estado de saúde atual do jogador: ")

    new_player = Player(Player.id_inicial, name, age, position, stats, health)
    players.append(new_player)
    print("Jogador adicionado com sucesso!")

def list_players():
    if not players:
        print("Nenhum jogador cadastrado no sistema.")
        return
    
    print("\nLista de Jogadores:")
    for jogador in players:
        print(f"ID: {jogador.id} | Nome: {jogador.name} | Idade: {jogador.age} | Posição: {jogador.position} | Estado de Saúde: {jogador.health}")
        print("-" * 30)

def edit_player():
    try:
        id_busca = int(input("Digite o ID do jogador a ser editado: "))
    except ValueError:
        print("ID inválido.")
        return
    
    for jogador in players:
        if jogador.id == id_busca:
            print(f"\nEditando jogador {jogador.name} (ID {jogador.id})")

            new_name = input(f"Novo nome (ou Enter para manter o anterior '{jogador.name}'): ")
            new_position = input(f"Nova posição (ou Enter para manter a anterior '{jogador.position}'): ")
            
            print("\nEditar estatísticas:")
            try: 
                print(f"Quantidade atual de gols: {jogador.stats.score}")
                print(f"Quantidade atual de partidas jogadas: {jogador.stats.games_played}")
                new_score = input(f"Gols (nova quantidade): ")
                new_games = input(f"Jogos (nova quantidade): ")
                
                jogador.stats.score = int(new_score)
                jogador.stats.games_played = int(new_games)
            except ValueError:
                print("Valor inválido para estatísticas (use números inteiros).")

            jogador.name = new_name
            jogador.position = new_position

            print("Jogador atualizado com sucesso!")
            return
    print("Jogador não encontrado!")
        
def remove_player():
    try:
        id_busca = int(input("Digite o ID do jogador a ser editado: "))
    except ValueError:
        print("ID inválido.")
        return
    
    for jogador in players:
        if jogador.id == id_busca:
            players.remove(jogador)
            print("Jogador removido com sucesso!")
            return
    print("Jogador não encontrado!")

def schedule_match():
    date = input("Digite a data da partida: ")
    time = input("Digite o horário da partida")
    opponent = input("Digite o nome do oponente: ")
    location = input("Local da partida: ")
    new_match = Match(date, time, opponent, location)
    matches.append(new_match)

def schedule_training():
    date = input("Data da do treino (ex: 18/08/2025): ")
    time = input("Digite o horário do treino: ")
    location = input("Local do treino: ")
    focus = input("Digite o objetivo do treino: ")
    new_training = Training(date, time, location, focus)
    trainings.append(new_training)

def delete_match():
    if not matches:
        print("Não há partidas cadastradas.")
        print("Partida não encontrada!")
        
    list_matches()
    try:
        id_remove = int(input("\nDigite o ID da partida a ser removida: "))
    except ValueError:
        print("ID inválido.")
        return

    for match in matches:
        if match.id == id_remove:
            matches.remove(match)
            print("Partida removida com sucesso!")
            return
        
def delete_training():
    if not trainings:
        print("Não há treinos cadastrados.")
        return
        
    list_trainings()
    try:
        id_remove = int(input("\nDigite o ID do treino a ser removido: "))
    except ValueError:
        print("ID inválido.")
        return

    for training in trainings:
        if training.id == id_remove:
            trainings.remove(training)
            print("Treino removido com sucesso!")
            return
    print("Treino não encontrado!")

def delete_event():
    print("\nREMOVER EVENTO")
    print("1. Remover Partida")
    print("2. Remover Treino")
    opcao = input("Escolha (ou Enter para voltar): ")

    if opcao == "1":
        delete_match()        

    elif opcao == "2":
        delete_training()

def list_matches():
    if not matches:
        print("Nenhum evento cadastrado no sistema.")
        return
    
    print("\nLista de Partidas:")
    for match in matches:
        print(f"ID: {match.id} | Oponente: {match.opponent} | Data: {match.date} | Hora: {match.time} |Local: {match.location} | Resultado: {match.result or 'Ainda não definido!'}")
        print("-" * 30)

def list_trainings():
    if not trainings:
        print("Nenhum evento cadastrado no sistema.")
        return
    
    print("\nLista de Treinos:")
    for training in trainings:
        print(f"ID: {training.id} | Data: {training.date} | Hora: {training.time} |Local: {training.location} | Objetivo: {training.focus}")
        print("-" * 30)

def team_management():
    while True:
        print("\nMENU DE GERENCIAMENTO DE JOGADORES")
        print("1. Adicionar Jogador")
        print("2. Listar Jogadores")
        print("3. Editar Jogador")
        print("4. Remover Jogador")
        print("5. Gerenciar Recrutas")
        print("6. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            add_player()
        elif opcao == "2":
            list_players()
        elif opcao == "3":
            edit_player()
        elif opcao == "4":
            remove_player()
        elif opcao == "5":
           manage_player_recruitment()
        elif opcao == "6":
            break
        else:
            print("Opção inválida.")

def schedule_event():
    while True:
        print("\nMENU DE GERENCIAMENTO DE EVENTOS")
        print("1. Agendar Partida")
        print("2. Agendar Treino")
        print("3. Listar Partidas")
        print("4. Listar Treinos")
        print("5. Remover Partidas/Treinos")
        print("6. Adicionar resultado à partida")
        print("7. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            schedule_match()
        elif opcao == "2":
            schedule_training()
        elif opcao == "3":
            list_matches()
        elif opcao == "4":
            list_trainings()
        elif opcao == "5":
           delete_event()
        elif opcao == "6":
            break
        else:
            print("Opção inválida.")

def performance_tracking():
    if not players:
        print("Nenhum jogador cadastrado.")
        return

    print("\nRelatório de Performance dos Jogadores:")
    for jogador in players:
        print(f"ID: {jogador.id} | Nome: {jogador.name} | Jogos: {jogador.stats.games_played} | Gols: {jogador.stats.score} |")
        print("-" * 30)

def health_monitoring():
    if not players:
        print("Nenhum jogador cadastrado.")
        return

    print("\nEstado de Saúde dos Jogadores:")
    for jogador in players:
        print(f"ID: {jogador.id} | Nome: {jogador.name} | Saúde: {jogador.health}")
        if jogador.health.lower() != "apto":
            injuried_players.append(jogador)
        print("-" * 30)

def manage_equipments():
    print("\nGERENCIAMENTO DE EQUIPAMENTOS")
    while True:
        print("1. Adicionar Equipamento")
        print("2. Listar Equipamentos")
        print("3. Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            name = input("Nome: ")
            type = input("Tipo: ")
            quantity = input("Quantidade: ")
            status = input("Status: ")
            observation = input("Observações: ")
            new_equipment = Equipment(name, type, quantity, status, observation)
            equipments.append(new_equipment)
        elif escolha == "2":
            for equipment in equipments:
                print(f"Nome: {equipment.name} | Tipo: {equipment.type} | Quantidade: {equipment.quantity} | Status: {equipment.status} | Observação: {equipment.observation}")
        elif escolha == "3":
            break
        else:
            print("Opção inválida!")

def manage_player_recruitment():
    print("\nGERENCIAMENTO DE RECRUTAS")
    while True:
        print("1. Adicionar Recruta")
        print("2. Listar Recrutas")
        print("3. Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            name = input("Nome: ")
            age = input("Idade: ")
            pros = input("Pontos fortes: ")
            cons = input("Pontos fracos: ")
            position = input("Posição: ")
            observation = input("Observação: ")
            new_recruit = Recruit(name, age, pros, cons, position, observation)
            recruits.append(new_recruit)
        elif escolha == "2":
            for recruit in recruits:
                print(f"Nome: {recruit.name} | Idade: {recruit.age} | Posição: {recruit.position} | Prós: {recruit.pros} | Contras: {recruit.cons} | Obs(se houver): {recruit.observation}")
        elif escolha == "3":
            break
        else:
            print("Opção inválida!")

def manage_finances():
    print("\nGERENCIAMENTO FINANCEIRO")
    while True:
        print(f"Saldo atual: R$ {conta.balance:.2f}")
        print("1. Registrar Receita")
        print("2. Registrar Despesa")
        print("3. Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            valor = float(input("Valor da receita: "))
            conta.balance += valor
        elif escolha == "2":
            valor = float(input("Valor da despesa: "))
            conta.balance -= valor
        elif escolha == "3":
            break
        else:
            print("Opção inválida!")

conta = Account(0.0)

def media_and_social():
    print("\nMÍDIA E RELAÇÕES PÚBLICAS")
    while True:
        print("1. Criar Enquete")
        print("2. Criar Postagem")
        print("3. Listar Enquetes")
        print("4. Listar Postagens")
        print("5. Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            title = input("Título da enquete: ")
            desc = input("Descrição: ")
            opt1 = input("Opção 1: ")
            opt2 = input("Opção 2: ")
            opt3 = input("Opção 3: ")
            polls.append(Poll(title, desc, opt1, opt2, opt3))
        elif escolha == "2":
            title = input("Título do post: ")
            content = input("Conteúdo: ")
            date = input("Data: ")
            posts.append(Post(title, content, date))
        elif escolha == "3":
            for p in polls:
                print("-"*30)
                print(f"Enquete: {p.title} | {p.description} \n[1] {p.opt1} [2] {p.opt2} [3] {p.opt3}")
                print("-"*30)
        elif escolha == "4":
            for post in posts:
                print("-"*30)
                print(f"Post: {post.title} | {post.date}\n{post.content}\n")
                print("-"*30)
        elif escolha == "5":
            break
        else:
            print("Opção inválida!")
    

def main():
    while True:
        print("\n===== SPORTS TEAM MANAGEMENT APP =====")
        print(" Selecione a opção desejada:")
        print("1. Gerenciar Equipe e Jogadores")
        print("2. Gerenciar Partidas e Treinos")
        print("3. Acompanhamento de Performance")
        print("4. Gerenciar Equipamentos")
        print("5. Gerenciar Finanças")
        print("6. Mídia e Social")
        print("Digite q para sair.")

        escolha = input("")

        if escolha == "1":
            team_management()
        elif escolha == "2":
            schedule_event()
        elif escolha == "3":
            performance_tracking()
        elif escolha == "4":
            manage_equipments()
        elif escolha == '5':
            manage_finances()
        elif escolha == "6":
            media_and_social()
        elif escolha == "q":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
