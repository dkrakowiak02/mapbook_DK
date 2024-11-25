users:list = [
    {'Name': 'Dominik', 'posts': 1, 'city': 'Poznań'},
    {'Name': 'Dominik', 'posts': 3, 'city': 'Warszawa'},
    {'Name': 'Szymon z wąsem', 'posts': 6, 'city': 'Warszawa'},
    {'Name': 'Szymon', 'posts': 7, 'city': 'Białogard'},
    {'Name': 'Patryk', 'posts': 5, 'city': 'Łódź'},

]
print (f'Witaj! {users[0]['Name']}!')
for user in users[1:]:
     print (f'Twój znajomy {user['Name']},{user['city']}, opublikował {user ['posts']} postów')

# for idx, _ in enumerate(users[1:]):
#     print(f'Twój znajmowy {users[idx]}, opublikował {postów[idx]} postów')
