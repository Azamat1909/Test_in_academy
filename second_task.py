

def is_substring(sentence, word):
    '''Проверяет является ли строка подстрокой
    предложения и возвращает булевое значение'''
    if word in sentence:
        return True
    else:
        return False


def main():
    '''Основная программа'''
    sentence = input('Enter the sentence: ')
    word = input('Enter word: ')
    if is_substring(sentence, word):
        print('The substring exist in the string')
    else:
        print('The substring not exist in the string')


main()
