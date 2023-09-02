from random import choice


COMMANDS_NAME = {
 'помощь': ('выводит доступные команды', 0),
 'правила': ('выводит правила игры', 1),
 'буквы': ('выводит буквы, которые вы вводили в данной игре', 2),
 'слова': ('выводит все слова доступные для загадывания', 3),
 'заново': ('начинает игру заново', 4),
 'добавить': ('добавляет в список слов для загадывание ваше слово', 5),
 'правило добавления': ('выводит правила добавления слов в список для загадывания', 6)
}
FILE_NAME_WORDS = r'words.txt'
FILE_NAME_APPENDED_WORDS = r'appended words.txt'
ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

with open(FILE_NAME_WORDS, encoding='utf-8') as file:
    words_list = [word.strip() for word in file.readlines()]


def get_agreement():
    while True:
        if input('Вы уверены?: ') in ('', 'да', 'yes', 'y', 'д'):
            return True
        return False


def print_commands_list():
    print()
    for command_name, command_data in COMMANDS_NAME.items():
        print(f'{command_name} - {command_data[0]}')
    print()


def print_rule_game():
    print('''
Правила данной игры:
    Будет загадано случайное слово, ваша задача его отгадать.
    Вводите букву, чтобы узнать есть она в слове и где находится в нём
    или вводите слово целиком, чтобы отгадать сразу.
    За каждую неправильную букву или слово будет тратиться 1 попытка.
    Количесвсто попыток ограничено.
    Удачи!
''')


def print_letters_list():
    print()
    if letters_list:
        print('Буквы которые вы ввели:', *letters_list)
    else:
        print('Вы ещё не вводили букв')
    print()


def print_words_list():
    print()
    print('Слова доступные для загадывания:', end='')
    print()
    size = 0
    for word in words_list:
        print(', ' if size else '', end='')
        size += len(word)
        if size > 50:
            size = len(word)
            print()
        print(word, end='')
    print('\n')


def start_over():
    return True


def append_word_in_words_list():
    print()
    print_append_words_rule()
    word = input('Какое слово вы хотите добавить: ').lower()
    if get_agreement():
        with open(FILE_NAME_APPENDED_WORDS, 'a', encoding='utf-8') as words_file:
            words_file.write(word + '\n')
        sort_words_file()
    print()


def print_append_words_rule():
    print('''
Правила добавления слова в список слов доступных для загадывания
слово должно быть:
-в официальном словаре русского языка
-включено в активную лексику русского языка в настоящее время
-именем существительным в начальной форме
-именем нарицательным
-не менее из пяти букв
-полным названием
-разрешено и понятно людям всех возрастных категорий
''')


def sort_words_file():
    with open(FILE_NAME_WORDS, 'r', encoding='utf-8') as words_file:
        title = words_file.readline()
        words = [word for word in sorted(words_file.readlines())[1:]]

    with open(FILE_NAME_WORDS, 'w', encoding='utf-8') as words_file:
        words_file.write(title + ''.join(words))


COMMANDS = (print_commands_list, print_rule_game, print_letters_list, print_words_list, start_over, append_word_in_words_list, print_append_words_rule)

print('''\
Добро Пожаловать на программу "Виселица"
Для помощи введите "помощь"''')

while True:
    gallow = '''
-------------
|/          |
|           O
|          /|\\
|          / \\
|\\
|__\\
'''
    gallow_stage5 = gallow[:71] + gallow[72:]
    gallow_stage4 = gallow_stage5[:69] + gallow_stage5[70:]
    gallow_stage3 = gallow_stage4[:56] + gallow_stage4[57:]
    gallow_stage2 = gallow_stage3[:55] + gallow_stage3[56:]
    gallow_stage1 = gallow_stage2[:54] + gallow_stage2[55:]
    stages_gallow = (gallow_stage1, gallow_stage2, gallow_stage3, gallow_stage4, gallow_stage5)

    word = choice(words_list)
    word_list = list(word)
    letters_list = []
    correct_letters_list = list(' ' * len(word))
    flag_end = False
    count_attempt = 5

    bar_lid = ' _   ' * len(word)


    while True:
        command = None
        flag_guess = False
        bar_in = ''.join([f'|{i}|  ' for i in correct_letters_list])
        bar_bottom = ' -   ' * len(word) + ' ' * 25 + 'Счётчик ошибок:' + str(count_attempt)
        print(gallow, bar_lid, bar_in, bar_bottom, sep='\n')

        while not flag_end:
            command = input('Введите букву, слово целиком или команду: ').lower()
            if command in ALPHABET:
                if command in letters_list:
                    print('Вы уже вводили эту букву')
                    continue
                letters_list.append(command)
                break
            elif command in COMMANDS_NAME:
                flag_end = COMMANDS[COMMANDS_NAME[command][1]]()
            elif command.isalpha():
                break
            else:
                print('Неизвестная команда')

        if not flag_end:
            if command == word:
                correct_letters_list = word_list

            if command in word:
                print('Ты угадал! Осталось ещё немного!')
                correct_letters_list = [command if word_char == command else char for char, word_char in zip(correct_letters_list, word)]
                flag_guess = True

            if correct_letters_list == word_list:
                print('Поздравляю! Ты победил!')
                flag_end = True

            if not (flag_end or flag_guess):
                print('Упс... Ты не угадал')
                count_attempt -= 1
                gallow = stages_gallow[count_attempt]

            if not count_attempt:
                print('Упс... Ты проиграл. В следующий раз повезёт!')
                flag_end = True

        if flag_end:
            bar_in = ''.join([f'|{i}|  ' for i in word_list])
            print(gallow, bar_lid, bar_in, bar_bottom, sep='\n')
            break
