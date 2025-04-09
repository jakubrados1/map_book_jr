users:list = [
    {'name': 'Julia', 'Location': 'Ząbki', 'posts': 10},
    {'name': 'Julia', 'Location': 'Sokółka', 'posts': 20},
    {'name': 'Klaudia', 'Location': 'Warszawa', 'posts': 15},
    {'name': 'Marcin', 'Location': 'Grudziądz', 'posts': 1000},
    {'name': 'Mateusz', 'Location': 'Lublin', 'posts': 10},
]






def get_user_info(users_data: list)->None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['Location']} opublikował {user['posts']} postów')


print(f'Witaj {users[0]['name']}')
get_user_info(users[1:])