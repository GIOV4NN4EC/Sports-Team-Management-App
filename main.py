players = [] #lista de jogadores
recruits = [] #lista de recrutas
matches = [] #lista de eventos (partidas ou treinos)
trainings =[] #lista de treinos
equipments = [] #lista de equipamentos
posts = [] #lista de posts criados
polls = [] #lista de enquetes criadas

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
        self.age = age #nome do jogador
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
        self.time = time
        self.location = location #local da partida
        self.opponent = opponent #oponente (se houver)
        self.result = None  #resultado (se houver)

class Training:
    training_id_counter = 0 #contador para identificar os eventos

    def __init__(self, date, time, location, focus):
        Training.training_id_counter += 1
        self.id = Training.training_id_counter #ID da partida
        self.date = date #data do evento
        self.time = time
        self.location = location #local da partida
        self.focus = focus #objetivo do treino (se houiver)


def add_player():
    name = input("NAME: ")
    age = input("AGE: ")
    position = input("POSITION: ")
    
    print("\nPLAYER STATS:")
    try:
        score = int(input("GOALS SCORED: "))
        games_played = int(input("GAMES PLAYED: "))
    except ValueError:
        print("INVALID VALUES. USE INTEGERS")
        return
    
    stats = Stats(score, games_played)
    health = input("PLAYER HEALTH STATUS: ")

    new_player = Player(Player.id_inicial, name, age, position, stats, health)
    players.append(new_player)
    print("PLAYER REGISTERED SUCCESSFULLY!")

def list_players():
    if not players:
        print("NO PLAYERS REGISTERED IN THE SYSTEM.")
        return
    
    print("\nPLAYERS LIST:")
    for player in players:
        print(f"ID: {player.id} | NAME: {player.name} | AGE: {player.age} | POSITION: {player.position} | HEALTH STATUS: {player.health}")
        print("-" * 90)

def edit_player():
    try:
        search_id = int(input("ENTER PLAYER ID TO EDIT: "))
    except ValueError:
        print("INVALID ID.")
        return
    
    for player in players:
        if player.id == search_id:
            print(f"\nEDITING PLAYER {player.name} (ID {player.id})")

            new_name = input(f"NEW NAME (OR ENTER TO KEEP '{player.name}'): ")
            new_position = input(f"NEW POSITION (OR ENTER TO KEEP '{player.position}'): ")

            if new_name.strip():
                player.name = new_name
            if new_position.strip():
                player.position = new_position
            
            print("\nEDIT STATS:")
            try:
                new_score = input(f"GOALS (CURRENT: {player.stats.score}): ")
                new_games = input(f"GAMES (CURRENT: {player.stats.games_played}): ")
                
                if new_score.strip():
                    player.stats.score = new_score
                if new_games.strip():
                    player.stats.games_played = new_games
                    
            except ValueError:
                print("INVALID VALUE FOR STATS.")

            print("PLAYER UPDATED SUCCESSFULLY!")
            return
    print("PLAYER NOT FOUND!")
        
def remove_player():
    try:
        search_id = int(input("ENTER PLAYER ID TO REMOVE: "))
    except ValueError:
        print("INVALID ID.")
        return
    
    for player in players:
        if player.id == search_id:
            players.remove(player)
            print("PLAYER REMOVED SUCCESSFULLY!")
            return
    print("PLAYER NOT FOUND!")


def schedule_match():
    date = input("ENTER MATCH DATE: ")
    time = input("ENTER MATCH TIME: ")
    opponent = input("ENTER OPPONENT NAME: ")
    location = input("ENTER MATCH LOCATION: ")
    new_match = Match(date, time, opponent, location)
    matches.append(new_match)

def schedule_training():
    date = input("ENTER TRAINING DATE (EX: 18/08/2025): ")
    time = input("ENTER TRAINING TIME: ")
    location = input("ENTER TRAINING LOCATION: ")
    focus = input("ENTER TRAINING OBJECTIVE: ")
    new_training = Training(date, time, location, focus)
    trainings.append(new_training)

def delete_match():
    if not matches:
        print("NO MATCHES REGISTERED.")
        print("MATCH NOT FOUND!")
            
    list_matches()
    try:
        id_remove = int(input("\nENTER MATCH ID TO REMOVE: "))
    except ValueError:
        print("INVALID ID.")
        return

    for match in matches:
        if match.id == id_remove:
            matches.remove(match)
            print("MATCH REMOVED SUCCESSFULLY!")
            return
        
def delete_training():
    if not trainings:
        print("NO TRAININGS REGISTERED.")
        return
        
    list_trainings()
    try:
        id_remove = int(input("\nENTER TRAINING ID TO REMOVE: "))
    except ValueError:
        print("INVALID ID.")
        return

    for training in trainings:
        if training.id == id_remove:
            trainings.remove(training)
            print("TRAINING REMOVED SUCCESSFULLY!")
            return
    print("TRAINING NOT FOUND!")

def delete_event():
    print("\nREMOVE EVENT")
    print("1. REMOVE MATCH")
    print("2. REMOVE TRAINING")
    print("0. BACK")
    option = input("CHOOSE: ")

    if option == "1":
        delete_match()        
    elif option == "2":
        delete_training()
    elif option == "0":
        return
    else:
        print("INVALID OPTION!")

def list_matches():
    if not matches:
        print("NO MATCHES REGISTERED.")
        return
    
    print("\nMATCHES LIST:")
    for match in matches:
        print(f"ID: {match.id} | OPPONENT: {match.opponent} | DATE: {match.date} | TIME: {match.time} | LOCATION: {match.location} | RESULT: {match.result or 'NOT DEFINED YET!'}")
        print("-" * 90)

def list_trainings():
    if not trainings:
        print("NO TRAININGS REGISTERED.")
        return
    
    print("\nTRAININGS LIST:")
    for training in trainings:
        print(f"ID: {training.id} | DATE: {training.date} | TIME: {training.time} | LOCATION: {training.location} | OBJECTIVE: {training.focus}")
        print("-" * 90)

def register_result():
    if not matches:
        print("NO MATCHES REGISTERED.")
        return

    try:
        match_id = int(input("ENTER MATCH ID TO REGISTER RESULT: "))
    except ValueError:
        print("INVALID ID.")
        return

    for match in matches:
        if match.id == match_id:
            result = input("ENTER MATCH RESULT (EX: WIN 2x1, LOSS 0x3): ")
            if result:
                match.result = result
                print("RESULT REGISTERED SUCCESSFULLY.")
            else:
                print("NO CHANGES MADE.")
            return
    print("MATCH NOT FOUND.")


def performance_tracking():
    if not players:
        print("NO PLAYERS REGISTERED.")
        return

    print("\nPLAYERS PERFORMANCE REPORT:")
    for player in players:
        aproveitamento = float(player.stats.score/player.stats.games_played)
        print(f"ID: {player.id} | NAME: {player.name} | GOALS PER GAME AVERAGE: {aproveitamento:.2f} |")
        print("-" * 90)

def check_health():
    health_id = input("ENTER PLAYER ID TO CHECK HEALTH STATUS: ")

    for player in players:
        if player.id == health_id:
            print(f"PLAYER {player.name} IS {player.health}")

def update_health():
    health_id = input("ENTER PLAYER ID TO UPDATE HEALTH STATUS: ")

    for player in players:
        if player.id == health_id:
            print(f"\nEDITING PLAYER {player.name} (ID {player.id})")

            new_health_status = input(f"NEW HEALTH STATUS (OR ENTER TO KEEP '{player.health}'): ")
    if player.health.strip():
        player.heatlh = new_health_status

def list_injuried_players():
    print("\n| INJURIED PLAYERS LIST |")
    print("-"*30)
    for player in injuried_players:
        print(f"{player.name}")
        print("-"*30)

def manage_player_recruitment():
    print("\nRECRUITS MANAGEMENT")
    while True:
        print("1. ADD RECRUIT")
        print("2. LIST RECRUITS")
        print("0. BACK")
        escolha = input("CHOOSE: ")

        if escolha == "1":
            name = input("NAME: ")
            age = input("AGE: ")
            pros = input("STRENGTHS: ")
            cons = input("WEAKNESSES: ")
            position = input("POSITION: ")
            observation = input("OBSERVATION: ")
            recruit = Recruit(name, age, pros, cons, position, observation)
            recruits.append(recruit)
        elif escolha == "2":
            for recruit in recruits:
                print(f"NAME: {recruit.name} | AGE: {recruit.age} | POSITION: {recruit.position} | STRENGTHS: {recruit.pros} | WEAKNESSES: {recruit.cons} | OBS: {recruit.observation}")
                print("-"*90)
        elif escolha == "0":
            break
        else:
            print("INVALID OPTION!")

def manage_players():
    while True:
        print("\nPLAYERS MANAGEMENT MENU")
        print("1. ADD PLAYER")
        print("2. LIST PLAYERS")
        print("3. EDIT PLAYER")
        print("4. REMOVE PLAYER")
        print("5. MANAGE RECRUITS")
        print("0. BACK")
        option = input("CHOOSE: ")

        if option == "1":
            add_player()
        elif option == "2":
            list_players()
        elif option == "3":
            edit_player()
        elif option == "4":
            remove_player()
        elif option == "5":
           manage_player_recruitment()
        elif option == "0":
            break
        else:
            print("INVALID OPTION.")

def team_management():
    while True:
        print("\nTEAM MANAGEMENT MENU")
        print("1. MANAGE PLAYERS")
        print("2. PERFORMANCE TRACKING")
        print("3. HEALTH MONITORING")
        print("4. MANAGE RECRUITS")
        print("0. BACK")
        option = input("CHOOSE: ")
        if option == "1":
            manage_players()
        elif option == "2":
            performance_tracking()
        elif option == "3":
            health_monitoring()
        elif option == "4":
            manage_player_recruitment()
        elif option == "0":
            break
        else:
            print("INVALID OPTION.")

def schedule_event():
    while True:
        print("\nEVENTS MANAGEMENT MENU")
        print("1. SCHEDULE MATCH")
        print("2. SCHEDULE TRAINING")
        print("3. LIST MATCHES")
        print("4. LIST TRAININGS")
        print("5. REMOVE MATCHES/TRAININGS")
        print("6. ADD MATCH RESULT")
        print("0. BACK")
        option = input("CHOOSE: ")

        if option == "1":
            schedule_match()
        elif option == "2":
            schedule_training()
        elif option == "3":
            list_matches()
        elif option == "4":
            list_trainings()
        elif option == "5":
           delete_event()
        elif option == "6":
            register_result()
        elif option == "0":
            break
        else:
            print("INVALID OPTION.")

def performance_tracking():
    if not players:
        print("NO PLAYERS REGISTERED.")
        return

    print("\nPLAYERS PERFORMANCE REPORT:")
    for player in players:
        aproveitamento = float(player.stats.score/player.stats.games_played)
        print(f"ID: {player.id} | NAME: {player.name} | GOALS PER GAME AVERAGE: {aproveitamento:.2f} |")
        print("-" * 90)

def check_health():
    health_id = input("ENTER PLAYER ID TO CHECK HEALTH STATUS: ")

    for player in players:
        if player.id == health_id:
            print(f"PLAYER {player.name} IS {player.health}")

def update_health():
    health_id = input("ENTER PLAYER ID TO UPDATE HEALTH STATUS: ")

    for player in players:
        if player.id == health_id:
            print(f"\nEDITING PLAYER {player.name} (ID {player.id})")

            new_health_status = input(f"NEW HEALTH STATUS (OR ENTER TO KEEP '{player.health}'): ")
    if player.health.strip():
        player.heatlh = new_health_status

def list_injuried_players():
    print("\n| INJURIED PLAYERS LIST |")
    print("-"*30)
    for player in players:
        if player.health != 'healthy':
            print(f" #{player.id} - {player.name} ({player.health})")
        print("-"*30)

def health_monitoring():
    while True:
        print("\nHEALTH MONITORING")
        print("1. CHECK HEALTH STATUS")
        print("2. UPDATE HEALTH STATUS")
        print("3. LIST INJURIED PLAYERS")
        print("0. BACK TO MAIN MENU")

        option = input("CHOOSE AN OPTION: ").strip()

        if option == "1":
            check_health()
        elif option == "2":
            update_health()
        elif option == "3":
            list_injuried_players()
        elif option == "0":
            break
        else:
            print("INVALID OPTION.")

def manage_equipments():
    print("\nEQUIPMENT MANAGEMENT")
    while True:
        print("1. ADD EQUIPMENT")
        print("2. LIST EQUIPMENTS")
        print("0. BACK")
        escolha = input("CHOOSE: ")

        if escolha == "1":
            name = input("NAME: ")
            type = input("TYPE: ")
            quantity = input("QUANTITY: ")
            status = input("STATUS: ")
            observation = input("OBSERVATIONS: ")
            new_equipment = Equipment(name, type, quantity, status, observation)
            equipments.append(new_equipment)
        elif escolha == "2":
            for equipment in equipments:
                print(f"NAME: {equipment.name} | TYPE: {equipment.type} | QUANTITY: {equipment.quantity} | STATUS: {equipment.status} | OBSERVATION: {equipment.observation}")
                print("-"*90)
        elif escolha == "0":
            break
        else:
            print("INVALID OPTION!")

def manage_finances():
    print("\nFINANCIAL MANAGEMENT")
    while True:
        print(f"CURRENT BALANCE: $ {account.balance:.2f}")
        print("1. REGISTER INCOME")
        print("2. REGISTER EXPENSE")
        print("0. BACK")
        option = input("CHOOSE: ")

        if option == "1":
            value = float(input("INCOME VALUE: "))
            account.balance += value
        elif option == "2":
            value = float(input("EXPENSE VALUE: "))
            account.balance -= value
        elif option == "0":
            break
        else:
            print("INVALID OPTION!")

account = Account(0.0)

def media_and_social():
    print("\nMEDIA AND PUBLIC RELATIONS")
    while True:
        print("1. CREATE POLL")
        print("2. CREATE POST")
        print("3. LIST POLLS")
        print("4. LIST POSTS")
        print("0. BACK")
        option = input("CHOOSE: ")

        if option == "1":
            title = input("POLL TITLE: ")
            desc = input("DESCRIPTION: ")
            opt1 = input("OPTION 1: ")
            opt2 = input("OPTION 2: ")
            opt3 = input("OPTION 3: ")
            polls.append(Poll(title, desc, opt1, opt2, opt3))
        elif option == "2":
            title = input("POST TITLE: ")
            content = input("CONTENT: ")
            date = input("DATE: ")
            posts.append(Post(title, content, date))
        elif option == "3":
            for p in polls:
                print("-"*90)
                print(f"POLL: {p.title} | {p.description} \n[1] {p.opt1} [2] {p.opt2} [3] {p.opt3}")
                print("-"*90)
        elif option == "4":
            for post in posts:
                print("-"*90)
                print(f"POST: {post.title} | {post.date}\n{post.content}\n")
                print("-"*90)
        elif option == "0":
            break
        else:
            print("INVALID OPTION!")

def main():
    while True:
        print("\n-----SPORTS TEAM MANAGEMENT APP-----")
        print(" SELECT AN OPTION:")
        print("1. MANAGE TEAM AND PLAYERS")
        print("2. MANAGE MATCHES AND TRAININGS")
        print("3. MANAGE EQUIPMENT")
        print("4. MANAGE FINANCES")
        print("5. MEDIA AND SOCIAL")
        print("0. EXIT")

        option = input("")

        if option == "1":
            team_management()
        elif option == "2":
            schedule_event()
        elif option == "3":
            manage_equipments()
        elif option == "4":
            manage_equipments()
        elif option == '5':
            manage_finances()
        elif option == "6":
            media_and_social()
        elif option == "0":
            print("CLOSING SYSTEM.")
            break
        else:
            print("INVALID OPTION!")

if __name__ == "__main__":
    main()
