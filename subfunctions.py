players = [] #lista de jogadores
matches = [] #lista de partidas
trainings = [] #lista de treinos

#Classe para os jogadores
class Player:
    id_inicial = 0 #contador para que não tenham IDs repetidos

    def __init__(self, name, position, stats):
        Player.id_inicial += 1
        self.id = Player.id_inicial #ID único do jogador
        self.name = name #nome do jogador
        self.position = position #posição do jogador
        self.stats = stats #estatística do jogador (nesse caso, aproveitamento)

#Classe para as partidas
class Match:
    match_id_counter = 0 #contador para identificar as partidas

    def __init__(self, date, opponent, location):
        Match.match_id_counter += 1
        self.id = Match.match_id_counter #ID da partida
        self.date = date #data da partida
        self.opponent = opponent #oponente
        self.location = location #local da partida
        self.result = None  #resultado (a princípio não definido)

#Classe para os treinos
class Training:
    training_id_counter = 0 #contador para identificar os treinos

    def __init__(self, date, location, purpose):
        Training.training_id_counter += 1
        self.id = Training.training_id_counter #ID do treino
        self.date = date #data do treino
        self.location = location #local do treino
        self.purpose = purpose #propósito do treino


#ADICIONAR JOGADOR
def add_player():
    name = input("Nome: ")
    position = input("Posição: ")
    stats = input("Aproveitamento: ")

    #cria um novo objeto da classe jogador e o adiciona na lista de jogadores
    new_player = Player(Player.id_inicial, name, position, stats)
    players.append(new_player)
    print("Jogador adicionado com sucesso!")

#LISTAR JOGADORES
def list_players():
    if not players:
        print("Nenhum jogador cadastrado no sistema.")
        return
    
    print("\nLista de Jogadores:")
    for jogador in players:
        print(f"ID: {jogador.id} | Nome: {jogador.nome} | Posição: {jogador.posicao} | Aproveitamento: {jogador.stats}")
        print("-" * 20)

#EDITAR JOGADOR
def edit_player():
    try:
        id_busca = int(input("Digite o ID do jogador a ser editado: "))
    except ValueError:
        print("ID inválido.")
        return
    
    for jogador in players:
        if jogador.id == id_busca:
            print(f"\nEditando jogador {Player.name} (ID {Player.id})")

            new_name = input(f"Novo nome (ou Enter para manter '{Player.name}'): ")
            new_position = input(f"Nova posição (ou Enter para manter '{Player.position}'): ")
            new_stats = input(f"Novo aproveitamento (ou Enter para manter '{Player.stats}'): ")

            if new_name.strip():
                jogador.name = new_name
            if new_position.strip():
                jogador.position = new_position
            if new_stats.strip():
                jogador.stats = new_stats

            print("Jogador atualizado com sucesso!")
            return

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
    print("\nAgendar Nova Partida")
    date = input("Data da partida (ex: 18/08/2025): ")
    opponent = input("Nome do time adversário: ")
    location = input("Local da partida: ")

    new_match = Match(date, opponent, location)
    matches.append(new_match)
    print(f"Partida agendada com sucesso! O ID da partida é: {new_match.id}")


def list_matches():
    if not matches:
        print("Nenhuma partida cadastrada no sistema.")
        return
    
    print("\nLista de Partidas:")
    for partida in matches:
        print(f"ID: {partida.id} | Oponente: {partida.opponent} | Data: {partida.date} |Local: {partida.location} | Resultado: {partida.result or 'Ainda não definido!'}")
        print("-" * 20)

def schedule_training():
    print("\nAgendar Novo Treino")
    date = input("Data do Treino (ex: 18/08/2025): ")
    location = input("Local do treino: ")
    purpose = input("Objetivo do treino: ")

    new_training = Training(date, location, purpose)
    trainings.append(new_training)
    print(f"Partida agendada com sucesso! O ID da partida é: {new_training.id}")

def list_trainings():
    if not trainings:
        print("Nenhum treino cadastrado no sistema.")
        return
    
    print("\nLista de Treinos:")
    for treino in trainings:
        print(f"ID: {treino.id} | Data: {treino.date} |Local: {treino.location} | Objetivo: {treino.purpose}")
        print("-" * 20)

def add_equipment():
    pass

def list_equipment():
    pass

def edit_equipment():
    pass

def remove_equipment():
    pass

def register_income():
    pass

def register_expense():
    pass

def list_transactions():
    pass

def generate_financial_report():
    pass

def create_post():
    pass

def list_posts():
    pass

def create_poll():
    pass

def list_polls():
    pass
