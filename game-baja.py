# game-baja
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
2. PlayStation 5
3. XBOX Series X/Series S
4. PC
5. Other
Input number here: '''.format(name = user_name)))

if console_num == 5:
    print('I\'m sorry, I do not have any games for that console in my database yet.')
else:
    console_str = ''

    console_dict = {
    1 : 'Nintendo Switch',
    2 : 'PlayStation 5',
    3 : 'XBOX Series S/Series S',
    4 : 'PC'
    }

    for key, val in console_dict.items():
        if key == console_num:
            console_str = val

    print('That\'s great, I love the {console}!'.format(console = console_str))

genre_num_str = input('''\nWe have plenty of games in our database for {console}. Why don\'t we start to narrow the list down a little by choosing some styles of games you enjoy?\n
Please select one or more genres from the list below by inputting the numbers of the associated genres (separate numbers by a comma for multiple selections):
1. Action/Adventure
2. Shooters (FPS and TPS)
2. Role Playing Games (RPGs, ARPGs and JRPGs)
3. Real-time Strategy (RTS)
4. Sports
5. Puzzles
6. Survival/Horror
Please input the number(s) here: '''.format(console = console_str))

genre_num_list = genre_num_str.split(',')

genre_dict = {
1 : 'Action/Adventure',
2 : 'Shooters (FPS and TPS)',
2 : 'Role Playing Games (RPGs, ARPGs and JRPGs)',
3 : 'Real-time Strategy (RTS)',
4 : 'Sports',
5 : 'Puzzles',
6 : 'Survival/Horror'
}

genre_list = ""

for genre_num in genre_num_list:
    for key, val in genre_dict.items():
        if genre_num == key:
            genre_list += val
            genre_list += ', '

print(genre_dict)
print(genre_num_list)
print(genre_list)
