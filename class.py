class Player:
    def __init__(self, gender, physique, character, job, health, hobby, fear, inventory, info, skill_1, skill_2):
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

    def unlock_gender(self):
        open_list['gender'] = self.gender
        print(self.gender)

    def unlock_physique(self):
        open_list['physique'] = self.physique
        print(self.physique)

    def unlock_character(self):
        open_list['character'] = self.character
        print(self.character)

    def unlock_job(self):
        open_list['job'] = self.job
        print(self.job)

    def unlock_health(self):
        open_list['health'] = self.health
        print(self.health)

    def unlock_hobby(self):
        open_list['hobby'] = self.hobby
        print(self.hobby)

    def unlock_fear(self):
        open_list['fear'] = self.fear
        print(self.fear)

    def unlock_inventory(self):
        open_list['inventory'] = self.inventory
        print(self.inventory)

    def unlock_info(self):
        open_list['info'] = self.info
        print(self.info)

    def unlock_skill_1(self):
        open_list['skill_1'] = self.skill_1
        print(self.skill_1)

    def unlock_skill_2(self):
        open_list['skill_2'] = self.skill_2
        print(self.skill_2)


player_1 = {'gender': 'male', 'physique': 'delicate', 'character': 'nasty', 'job': 'dentist',
            'health': 'perfectly healthy', 'hobby': 'painting', 'fear': 'fear of pain', 'inventory': 'hammer',
            'info': 'idol for teen', 'skill_1': 'change any characteristic of yourself', 'skill_2': 'heal any player'}

open_list = {'gender': '',
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

player_1 = Player(player_1['gender'], player_1['physique'], player_1['character'], player_1['job'], player_1['health'],
                  player_1['hobby'], player_1['fear'], player_1['inventory'], player_1['info'], player_1['skill_1'],
                  player_1['skill_2'])
while True:
    choice = input(f'\n'
                   f'gender : {open_list.get("gender", " ")} \n'
                   f'physique : {open_list.get("physique", " ")} \n'
                   f'character : {open_list.get("character", " ")}\n'
                   f'job : {open_list.get("job", " ")}\n'
                   f'health : {open_list.get("health", " ")}\n'
                   f'hobby : {open_list.get("hobby", " ")}\n'
                   f'fear : {open_list.get("fear", " ")}\n'
                   f'inventory : {open_list.get("inventory", " ")}\n'
                   f'info : {open_list.get("info", " ")}\n'
                   f'skill_1 : {open_list.get("skill_1", " ")}\n'
                   f'skill_2 : {open_list.get("skill_2", " ")}\n'
                   'Введіть те що ви хочете відкрити: ')

    if choice == 'gender':
        player_1.unlock_gender()

    if choice == 'physique':
        player_1.unlock_physique()

    if choice == 'character':
        player_1.unlock_character()

    if choice == 'job':
        player_1.unlock_job()

    if choice == 'health':
        player_1.unlock_health()

    if choice == 'hobby':
        player_1.unlock_hobby()

    if choice == 'fear':
        player_1.unlock_fear()

    if choice == 'inventory':
        player_1.unlock_inventory()

    if choice == 'info':
        player_1.unlock_info()

    if choice == 'skill_1':
        player_1.unlock_skill_1()

    if choice == 'skill_2':
        player_1.unlock_skill_2()

    else:
        print('error in name')
