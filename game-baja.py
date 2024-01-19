# game-baja
class Game:
    def __init__(self, title, console, players, genre, ESRB, release_year):
        self.title = title
        self.console = console
        self.players = players
        self.genre = genre
        self.ESRB = ESRB
        self.release_year = release_year

    def __repr__(self):
        print(self.title)

# Template  ---  title = Game(title_str, console_lst, players_lst, genre_lst, ESRB_str, release_year_int)
# Nintendo Switch games
zelda_botw = Game('Legend of Zelda: Breath of the Wild', ['Nintendo Switch'], ['Single-player'], ['Action/Adventure', 'Role Playing Game', 'Open World', 'Fantasy'], 'E10', 2017)
mario_kart_8 = Game('Mario Kart 8', ['Nintendo Switch'], ['Multiplayer'], ['Racing', 'Fantasy'], 'E', 2014)
animal_crossing_NH = Game('Animal Crossing: New Horizons', ['Nintendo Switch'], ['Single-player', 'Multiplayer'], ['Fantasy', 'Simulation'], 'E', 2020)
hades = Game('Hades', ['Nintendo Switch', 'PlayStation 4', 'PlayStation 5', 'Xbox One', 'Xbox Series X/S', 'PC'], ['Single-player'], ['Action/Adventure', 'Roguelike'], 'M', 2020)
mario_odyssey = Game('Super Mario Odyssey', ['Nintendo Switch'], ['Single-player'], ['Action/Adventure', 'Fantasy', 'Platformer'], 'E', 2017)
mario_party = Game('Super Mario Party', ['Nintendo Switch'], ['Multiplayer'], ['Fantasy', 'Party'], 'E', 2018)

# PlayStation games
god_of_war_2018 = Game('God of War', ['PlayStation 4', 'PlayStation 5'], ['Single-player'], ['Action/Adventure', 'Fantasy'], 'M', 2018)
god_of_war_ragnarok = Game('God of War: Ragnarok', ['PlayStation 4', 'PlayStation 5'], ['Single-player'], ['Action/Adventure', 'Fantasy'], 'M', 2022)
nioh = Game('Nioh', ['PlayStation 4', 'PlayStation 5', 'PC'], ['Single-player'], ['Action/Adventure', 'Fantasy', 'Soulslike'], 'M', 2017)
nioh_2 = Game('Nioh 2', ['PlayStation 4', 'PlayStation 5', 'PC'], ['Single-player'], ['Action/Adventure', 'Fantasy', 'Soulslike'], 'M', 2021)
elden_ring = Game('Elden Ring', ['PlayStation 4', 'PlayStation 5', 'Xbox One', 'Xbox Series X/S', 'PC'], ['Single-player'], ['Action/Adventure', 'Role Playing Game', 'Open World', 'Fantasy', 'Soulslike'], 'M', 2022)
borderlands_3 = Game('Borderlands 3', ['PlayStation 4', 'PlayStation 5', 'Xbox One', 'Xbox Series X/S', 'PC'], ['Single-player', 'Multiplayer'], ['Shooter', 'Sci-Fi'], 'M', 2019)
divinity_OS2 = Game('Divinity: Original Sin 2', ['Nintendo Switch', 'PlayStation 4', 'Xbox One', 'PC'], ['Single-player', 'Multiplayer'], ['Role Playing Game', 'Fantasy'], 'M', 2017)
outer_worlds = Game('The Outer Worlds', ['Nintendo Switch', 'PlayStation 4', 'PlayStation 5', 'Xbox One', 'Xbox Series X/S', 'PC'], ['Single-player'], ['Shooter', 'Role Playing Game', 'Sci-Fi'], 'M', 2019)
horizon = Game('Horizon Zero Dawn', ['PlayStation 4', 'PC'], ['Single-player'], ['Action/Adventure', 'Role Playing Game', 'Sci-Fi'], 'T', 2017)
horizon_2 = Game('Horizon: Forbidden West', ['PlayStation 4', 'PlayStation 5'], ['Single-player'], ['Action/Adventure', 'Role Playing Game', 'Sci-Fi'], 'T', 2022)
ghost_of_tsushima = Game('Ghost of Tsushima', ['PlayStation 4', 'PlayStation 5'], ['Single-player'], ['Action/Adventure'], 'M', 2020)
ufc_3 = Game('UFC 3', ['PlayStation 4', 'Xbox One'], ['Single-player', 'Multiplayer'], ['Sports', 'Fighting'], 'T', 2018)
ufc_4 = Game('UFC 4', ['PlayStation 4', 'Xbox One'], ['Single-player', 'Multiplayer'], ['Sports', 'Fighting'], 'T', 2020)
tekken_7 = Game('Tekken 7', ['PlayStation 4', 'Xbox One', 'PC'], ['Single-player', 'Multiplayer'], ['Fighting'], 'T', 2016)
uncharted = Game('Uncharted: Drake\'s Fortune', ['PlayStation 4'], ['Single-player'], ['Action/Adventure', 'Shooter'], 'T', 2007)
uncharted_2 = Game('Uncharted 2: Among Thieves', ['PlayStation 4'], ['Single-player'], ['Action/Adventure', 'Shooter'], 'T', 2009)
uncharted_3 = Game('Uncharted 3: Drake\'s Deception', ['PlayStation 4'], ['Single-player'], ['Action/Adventure', 'Shooter'], 'T', 2011)
uncharted_4 = Game('Uncharted 4: A Thief\'s End', ['PlayStation 4', 'PlayStation 5'], ['Single-player'], ['Action/Adventure', 'Shooter'], 'T', 2016)
returnal = Game('Returnal', ['PlayStation 5', 'PC'], ['Single-player'], ['Shooter', 'Sci-Fi' 'Roguelike'], 'T', 2021)

# Xbox games
halo_infinite = Game('Halo: Infinite', ['Xbox One, Xbox Series X/S'], ['Single-player', 'Multiplayer'], ['Shooter', 'Sci-Fi'], 'T', 2021)
apex_legends = Game('Apex Legends', ['Nintendo Switch', 'PlayStation 4', 'PlayStation 5', 'Xbox One', 'Xbox Series X/S', 'PC'], ['Multiplayer'], ['Shooter', 'Battle Royale'], 'T', 2019)
dark_souls_3 = Game('Dark Souls 3', ['PlayStation 4', 'Xbox One', 'PC'], ['Single-player'], ['Action/Adventure', 'Fantasy', 'Soulslike'], 'M', 2016)
sekiro = Game('Sekiro: Shadows Die Twice', ['PlayStation 4', 'Xbox One', 'PC'], ['Single-player'],['Action/Adventure', 'Fantasy', 'Soulslike'], 'M', 2019)

# PC games
minecraft = Game('Minecraft', ['PlayStation 4', 'Xbox One', 'PC'], ['Single-player', 'Multiplayer'], ['Sandbox'], 'E', 2011)
starcraft_2 = Game('Starcraft 2', ['PC'], ['Single-player', 'Multiplayer'], ['Real Time Strategy', 'Sci-Fi'], 'M', 2010)
fortnite = Game('Fortnite', ['Nintendo Switch', 'PlayStation 4', 'PlayStation 5', 'Xbox One', 'Xbox Series X/S', 'PC'], ['Multiplayer'], ['Shooter', 'Battle Royale'], 'T', 2017)
overwatch = Game('Overwatch', ['Nintendo Switch', 'PlayStation 4', 'Xbox One', 'PC'], ['Multiplayer'], ['Shooter'], 'T', 2016)
overwatch_2 = Game('Overwatch 2', ['Nintendo Switch', 'PlayStation 4', 'PlayStation 5', 'Xbox One', 'Xbox Series X/S', 'PC'], ['Multiplayer'], ['Shooter'], 'T', 2022)

collection = [zelda_botw, mario_kart_8, animal_crossing_NH, hades, mario_odyssey, mario_party, god_of_war_2018, god_of_war_ragnarok, nioh, nioh_2, elden_ring, borderlands_3, divinity_OS2,
outer_worlds, horizon, horizon_2, ghost_of_tsushima, ufc_3, ufc_4, tekken_7,uncharted, uncharted_2, uncharted_3, uncharted_4, returnal, halo_infinite, apex_legends, dark_souls_3, sekiro,
minecraft, starcraft_2, fortnite, overwatch, overwatch_2]

coll = [zelda_botw]

title = '''
 ********************************************************
 GGGGG  AAAAA  M    M  EEEEE   BBBBB  AAAAA  JJJJJ  AAAAA
 G      A   A  MM  MM  E       B   B  A   A    J    A   A
 G  GG  AAAAA  M MM M  EEEE    BBBB   AAAAA    J    AAAAA
 G   G  A   A  M    M  E       B   B  A   A    J    A   A
 GGGGG  A   A  M    M  EEEEE   BBBBB  A   A  JJJ    A   A
 ********************************************************
 \n
 '''
greeting = ('Hello, I am Game-Baja, a chatbot designed to help you find video games suited to your personal preferences. Let\'s begin by getting to know each other better...\n')

print(title)
print(greeting)

begin = input('First let\'s make sure that your keyboard is working. Please press Y and then enter to continue. Or press N and then enter to quit the program. ')

if begin.lower() == 'y':
    print('\nGreat!')
elif begin.lower() == 'n':
    print('It was nice to meet you, I\'m here to help if you need anything else!\n')
else:
    while begin.lower() != 'y' and begin.lower() != 'n':
        print('You entered something other than Y or N.')
        begin = input('Please press Y or N and then hit enter. ')
        if begin == 'Y':
            print('Great!')
            break

user_name = input('\nFirst things first, what is your name? ')
print('\nNice to meet you {name}! You can call me GB.'.format(name = user_name))

console_num = int(input('''\nSo {name}, what console are you currently playing on? Please choose the number of associated console below:
1. Nintendo Switch
2. PlayStation 4
3. PlayStation 5
4. Xbox One
5. XBOX Series X/S
6. PC
7. Other
Input number here: '''.format(name = user_name)))

if console_num == 5:
    print('I\'m sorry, I do not have any games for that console in my database yet.')
else:
    console_str = ''

    console_dict = {
    1 : 'Nintendo Switch',
    2 : 'PlayStation 4',
    3 : 'PlayStation 5',
    4 : 'Xbox One',
    5 : 'XBOX Series X/S',
    6 : 'PC'
    }

    for key, val in console_dict.items():
        if key == console_num:
            console_str = val

    print('That\'s great, I love the {console}!'.format(console = console_str))

genre_num_str = input('''\nWe have plenty of games in our database for {console}. Why don\'t we start to narrow the list down a little by choosing some styles of games you enjoy?\n
Please select one or more genres from the list below by inputting the numbers of the associated genres (separate numbers by a comma for multiple selections):
1. Action/Adventure
2. Shooters (FPS and TPS)
3. Role Playing Games (RPGs, ARPGs and JRPGs)
4. Real-time Strategy (RTS)
5. Sports
6. Puzzles
7. Survival/Horror
8. Racing
9. Fantasy
10. Sci-Fi
11. Open-world
12. Sandbox
13. Simulation
14. Soulslike
15. Roguelike
16. Platformer
17. Party
18. Battle Royale
19. Fighting
Please input the number(s) here: '''.format(console = console_str))

genre_num_list = genre_num_str.split(',')

genre_dict = {
1 : 'Action/Adventure',
2 : 'Shooter',
3 : 'Role Playing Game',
4 : 'Real-time Strategy',
5 : 'Sports',
6 : 'Puzzles',
7 : 'Survival/Horror',
8 : 'Racing',
9 : 'Fantasy',
10 : 'Sci-Fi',
11 : 'Open World',
12 : 'Sandbox',
13 : 'Simulation',
14 : 'Soulslike',
15 : 'Roguelike',
16 : 'Platformer',
17 : 'Party',
18 : 'Battle Royale',
19 : 'Fighting'
}

genre_list = ""

for genre_num in genre_num_list:
    for key, val in genre_dict.items():
        if int(genre_num) == key:
            genre_list += val
            genre_list += ', '

# def game_list(genres, games):
#     suggestions = []
#     for genre in genres:
#         for game in games:
#             if genre in game.genre:
#                 suggestions.append(game.title)

    # return suggestions
print('\nGreat! We recommend the following game(s)...\n')
good_genre = []
for game in collection:
    for item in game.genre:
        if item in genre_list and game not in good_genre:
            good_genre.append(game)

good_player = []
# for game in good_genre
counter = 1
for game in good_genre:
    for item in game.console:
        if item == console_str:
            print(str(counter) +') ' + game.title + "\n")
            counter += 1
