
def hello(user:str)->None:
    print(f'Witaj! {user}!')

def read_users(users:list)->None:
    for user in users[1:]:
        print(f'Twój znajomy {user['Name']}, {user['city']}, opublikował {user['posts']} postów')


def add_user(userlist:list)-> None:
    new_Name: str = input('Proszę podać imię nowego znajomego ')
    new_posts: int = int(input ('Prosze podać liczbę postów '))
    new_city: str = input ('Proszę podać miasto ')
    new_user: dict = {'Name': new_Name, 'posts': new_posts, 'city': new_city}
    userlist.append(new_user)


def remove_user(userlist:list)->None:
    user_to_find: str = input('Podaj imię do usunięcia: ')
    for user in userlist:
        if user['Name'] == user_to_find:
            print(f'usuwam: {user}')
            userlist.remove(user)
