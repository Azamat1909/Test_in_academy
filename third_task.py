
def is_pangram(sentence):
    '''Проверяет предложение на панграмность,
    возвращает булевое значение'''
    eng_letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in eng_letters:
        if letter not in sentence:
            return False
    else:
        return True


def main():
    '''Основная программа'''
    sentence = input('Enter the sentence: ').lower()
    print(is_pangram(sentence))


main()
