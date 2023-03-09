def highlight(colour, text):
    if colour == "red":
        return "\033[1;41m" + str(text) + "\033[1;m"
    if colour == "magenta":
        return "\033[1;45m" + str(text) + "\033[1;m"
    if colour == "cyan":
        return "\033[1;46m" + str(text) + "\033[1;m"
    if colour == "gray":
        return "\033[1;47m" + str(text) + "\033[1;m"
    return str(text)



class Player:
    def __init__(self, gender, physique, character, job, health, hobby, fear, inventory, info, skill_1, skill_2, id):
        self.gender = gender
        self.physique = physique
        self.character = character
        self.job = job
        self.health = health
        self.hobby = hobby
        self.fear = fear
        self.inventory = inventory
        self.info = info
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.id = id

    def unlock_gender(self):
        if players_count == 0:
            open_list_1['gender'] = self.gender
            print(highlight(f"cyan", self.gender))

        if players_count == 1:
            open_list_2['gender'] = self.gender
            print(highlight(f"cyan", self.gender))

    def unlock_physique(self):
        if players_count == 0:
            open_list_1['physique'] = self.physique
            print(highlight(f"cyan", self.physique))

        if players_count == 1:
            open_list_2['physique'] = self.physique
            print(highlight(f"cyan", self.physique))

    def unlock_character(self):
        if players_count == 0:
            open_list_1['character'] = self.character
            print(highlight(f"cyan", self.character))
        if players_count == 1:
            open_list_2['character'] = self.character
            print(highlight(f"cyan", self.character))

    def unlock_job(self):
        if players_count == 0:
            open_list_1['job'] = self.job
            print(highlight(f"cyan", self.job))
        if players_count == 1:
            open_list_2['job'] = self.job
            print(highlight(f"cyan", self.job))

    def unlock_health(self):
        if players_count == 0:
            open_list_1['health'] = self.health
            print(highlight(f"cyan", self.health))
        if players_count == 1:
            open_list_2['health'] = self.health
            print(highlight(f"cyan", self.health))

    def unlock_hobby(self):
        if players_count == 0:
            open_list_1['hobby'] = self.hobby
            print(highlight(f"cyan", self.hobby))
        if players_count == 1:
            open_list_2['hobby'] = self.hobby
            print(highlight(f"cyan", self.hobby))

    def unlock_fear(self):
        if players_count == 0:
            open_list_1['fear'] = self.fear
            print(highlight(f"cyan", self.fear))
        if players_count == 1:
            open_list_2['fear'] = self.fear
            print(highlight(f"cyan", self.fear))

    def unlock_inventory(self):
        if players_count == 0:
            open_list_1['inventory'] = self.inventory
            print(highlight(f"cyan", self.inventory))
        if players_count == 1:
            open_list_2['inventory'] = self.inventory
            print(highlight(f"cyan", self.inventory))

    def unlock_info(self):
        if players_count == 0:
            open_list_1['info'] = self.info
            print(highlight(f"cyan", self.info))
        if players_count == 1:
            open_list_2['info'] = self.info
            print(highlight(f"cyan", self.info))

    def unlock_skill_1(self):
        if players_count == 0:
            open_list_1['skill_1'] = self.skill_1
            print(highlight(f"cyan", self.skill_1))
        if players_count == 1:
            open_list_2['skill_1'] = self.skill_1
            print(highlight(f"cyan", self.skill_1))

    def unlock_skill_2(self):
        if players_count == 0:
            open_list_1['skill_2'] = self.skill_2
            print(highlight(f"cyan", self.skill_2))
        if players_count == 1:
            open_list_2['skill_2'] = self.skill_2
            print(highlight(f"cyan", self.skill_2))


player_1 = {'gender': 'male', 'physique': 'delicate', 'character': 'nasty', 'job': 'dentist',
            'health': 'perfectly healthy', 'hobby': 'painting', 'fear': 'fear of pain', 'inventory': 'hammer',
            'info': 'idol for teen', 'skill_1': 'change any characteristic of yourself', 'skill_2': 'heal any player',
            'id': '1234'}

player_2 = {'gender': 'female', 'physique': 'жосрсткий', 'character': 'добрий', 'job': 'лікар',
            'health': 'перелом ноги', 'hobby': 'відео ігри', 'fear': 'немає', 'inventory': 'цвяхи',
            'info': 'просто тіпок', 'skill_1': 'міняє всім стать ', 'skill_2': 'міняє всім вік', 'id': '5678'}

open_list_1 = {'gender': '',
               'physique': '',
               'character': '',
               'job': '',
               'health': '',
               'hobby': '',
               'fear': '',
               'inventory': '',
               'info': '',
               'skill_1': '',
               'skill_2': ''}

open_list_2 = {'gender': '',
               'physique': '',
               'character': '',
               'job': '',
               'health': '',
               'hobby': '',
               'fear': '',
               'inventory': '',
               'info': '',
               'skill_1': '',
               'skill_2': ''}

all_list = (open_list_1, open_list_2)

player_1 = Player(player_1['gender'], player_1['physique'], player_1['character'], player_1['job'], player_1['health'],
                  player_1['hobby'], player_1['fear'], player_1['inventory'], player_1['info'], player_1['skill_1'],
                  player_1['skill_2'], player_1['id'])

player_2 = Player(player_2['gender'], player_2['physique'], player_2['character'], player_2['job'], player_2['health'],
                  player_2['hobby'], player_2['fear'], player_2['inventory'], player_2['info'], player_2['skill_1'],
                  player_2['skill_2'], player_2['id'])
players = 2
players_count = 0
while True:
    if players_count == players:
        players_count = 0
        continue
    found = False
#    print(players_count)
    for i in range(len(all_list)):
        print('\n')
        print(highlight("magenta", f" ^ ^ ^ player {i + 1} ^ ^ ^"))
        print(f'\n'                      
              f'gender : {all_list[i].get("gender", " ")} \n'
              f'physique : {all_list[i].get("physique", " ")} \n'
              f'character : {all_list[i].get("character", " ")}\n'
              f'job : {all_list[i].get("job", " ")}\n'
              f'health : {all_list[i].get("health", " ")}\n'
              f'hobby : {all_list[i].get("hobby", " ")}\n'
              f'fear : {all_list[i].get("fear", " ")}\n'
              f'inventory : {all_list[i].get("inventory", " ")}\n'
              f'info : {all_list[i].get("info", " ")}\n'
              f'skill_1 : {all_list[i].get("skill_1", " ")}\n'
              f'skill_2 : {all_list[i].get("skill_2", " ")}\n')

    choice = input(f'Введіть те що ви гравець {players_count + 1}  хочете відкрити:  ')

    if players_count == 0 and choice == 'gender':
        player_1.unlock_gender()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'gender':
        player_2.unlock_gender()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'physique':
        player_1.unlock_physique()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'physique':
        player_2.unlock_physique()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'character':
        player_1.unlock_character()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'character':
        player_2.unlock_character()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'job':
        player_1.unlock_job()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'job':
        player_2.unlock_job()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'health':
        player_1.unlock_health()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'health':
        player_2.unlock_health()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'hobby':
        player_1.unlock_hobby()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'hobby':
        player_2.unlock_hobby()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'fear':
        player_1.unlock_fear()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'fear':
        player_2.unlock_fear()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'inventory':
        player_1.unlock_inventory()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'inventory':
        player_2.unlock_inventory()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'info':
        player_1.unlock_info()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'info':
        player_2.unlock_info()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'skill_1':
        player_1.unlock_skill_1()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'skill_1':
        player_2.unlock_skill_1()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 0 and choice == 'skill_2':
        player_1.unlock_skill_1()
        players_count = players_count + 1
        found = True
        continue

    if players_count == 1 and choice == 'skill_2':
        player_2.unlock_skill_2()
        players_count = players_count + 1
        found = True
        continue

    if found == False:
        print(highlight('red', '^ ^ ^ error in name, write again ^ ^ ^'
              ' '))
