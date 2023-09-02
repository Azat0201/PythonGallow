FILE_NAME_WORDS = r'words.txt'
FILE_NAME_APPENDED_WORDS = r'appended words.txt'

with open(FILE_NAME_APPENDED_WORDS, 'r', encoding='utf8') as words_file:
    title = words_file.readline()


def clear_appended_words_file():
    with open(FILE_NAME_APPENDED_WORDS, 'w', encoding='utf8') as file:
        file.write(title)


def sort_words_file():
    with open(FILE_NAME_WORDS, 'r', encoding='utf-8') as file:
        words = [word for word in sorted(file.readlines())]

    with open(FILE_NAME_WORDS, 'w', encoding='utf-8') as file:
        file.write(''.join(words))


def sort_appended_words_file():
    with open(FILE_NAME_APPENDED_WORDS, 'r', encoding='utf-8') as file:
        words = [word for word in sorted(file.readlines()[1:])]

    with open(FILE_NAME_APPENDED_WORDS, 'w', encoding='utf-8') as file:
        file.write(title + ''.join(words))



def append_words_to_file():
    with open(FILE_NAME_WORDS, 'a', encoding='utf-8') as file, \
            open(FILE_NAME_APPENDED_WORDS, 'r', encoding='utf-8') as appended_words_file:
        words = appended_words_file.readlines()[1:]
        file.write(''.join(words))
    clear_appended_words_file()
    sort_words_file()


def print_words_file():
    with open(FILE_NAME_WORDS, 'r', encoding='utf-8') as file:
        print(file.read())


def print_appended_words_file():
    with open(FILE_NAME_APPENDED_WORDS, 'r', encoding='utf-8') as file:
        print(file.read())


COMMANDS = (clear_appended_words_file, sort_words_file, sort_appended_words_file, append_words_to_file, print_words_file, print_appended_words_file)

while True:
    COMMANDS[int(input('Command: '))]()
