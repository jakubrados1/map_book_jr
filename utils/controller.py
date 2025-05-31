def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['Location']} opublikował {user['posts']} postów')

def add_user(users_data: list) -> None:
     new_name: str = input('Podaj imie nowego znajomego: ')
     new_location: str = input('Podaj miejsce zamieszkania nowego znajomego: ')
     new_posts: int = int(input('Podaj liczbę postów znajomego: '))
     users_data.append({'name': new_name, 'Location': new_location, 'posts': new_posts})

def remove_user(users_data: list) -> None:
    u_name: str = input('Wpisz kogo chcesz usunąć: ')
    for user in users_data:
        if user['name'] == u_name:
            users_data.remove(user)

def update_user(user_data: list) -> None:
    user_name: str = input('Wpisz kogo chcesz zmodyfikować: ')
    for user in user_data:
        if user['name'] == user_name:
            user['name'] = input('Podaj nowe imie: ')
            user['Location'] = input('Podaj nową lokalizację: ')
            user['posts'] = input('Podaj nową liczbę postów: ')
