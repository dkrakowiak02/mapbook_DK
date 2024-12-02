
def hello(user:str)->None:
    print(f'Witaj! {user}!')

def read_users(users:list)->None:
    for user in users[1:]:
        print(f'Twój znajomy {user['Name']}, {user['city']}, opublikował {user['posts']} postów')

add_user(users)
def add_user(userlist:list)-> None:
    new_Name: str = input('Proszę podać imię nowego znajomego ')
    new_posts: int = int(input ('Prosze podać liczbę postów '))
    new_city: str = input ('Proszę podać miasto ')
    new_user: dict = {'Name': new_Name, 'posts': new_posts, 'city': new_city}
    userlist.append(new_user)
