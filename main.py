users: list = [
    {'Name': 'Dominik', 'posts': 1, 'city': 'Poznań'},
    {'Name': 'Dominik', 'posts': 3, 'city': 'Warszawa'},
    {'Name': 'Szymon z wąsem', 'posts': 6, 'city': 'Inowrocław'},
    {'Name': 'Szymon', 'posts': 7, 'city': 'Białogard'},
    {'Name': 'Żerom', 'posts': 9, 'city': 'Tarnobrzeg'},
    {'Name': 'Michał', 'posts': 12, 'city': 'Kluczbork'},
    {'Name': 'Dominik', 'posts': 1000, 'city': 'Siedlce'},
    {'Name': 'Kinga', 'posts': 3, 'city': 'Gdynia'},
    {'Name': 'Amelia', 'posts': 11, 'city': 'Toruń'},
    {'Name': 'Karolina', 'posts': 5, 'city': 'Mława'},
]

print (f'Witaj! {users[0]['Name']}!')
for user in users[1:]:
     print (f'Twój znajomy {user['Name']}, {user['city']}, opublikował {user ['posts']} postów')

# for idx, _ in enumerate(users[1:]):
#     print(f'Twój znajmowy {users[idx]}, opublikował {postów[idx]} postów')
