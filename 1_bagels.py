import random

NUM_DIGIT = 3
MAX_GUESSES = 10


def main():
    print('''Баранка дедуктивная логическая игра.
Правила:
Я загадываю {}-значное число без повторов.
Попробуй угадать их. 

Что я говорю:       Что имею ввиду:
Пико                Цифра верна, но не на той позиции
Ферми               Цифра верна и на нужной позиции
Баранка             Неверная цифра

Например: загаданное число 248 и твоя догадка 843, ключ будте – Ферми Пико.'''.format(NUM_DIGIT))

    while True:
        secretNum = getSecretNum()
        print("Я загадал число!")
        print("у тебя {} попыток чтобы угадать это число".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Продолжаем итерации до правильной догадки
            while len(guess) != NUM_DIGIT or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("Попытки закончились!")
                print("Правильный ответ был {}.".format(secretNum))

        # Спрашиваем игрока, хочет ли он сыграть еще раз
        print("Играем еще? (y/n)")
        if not input('> ').lower().startswith('y'):
            break
    print("Спасибо за игру!")


def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGIT):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Возвращает строку с подсказками пико, ферми, баранка
    для полученной пары на входе из догадки и секретного числа"""
    # if guess == secretNum:
    #     return "Ты угадал!!!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на том месте
            clues.append('Ферми')
        elif guess[i] in secretNum:
            # Правильная цифра не на том месте
            clues.append('Пико')
    if len(clues) == 0:
        return 'Баранка'
    else:
        # Сортируем подсказки в алфавитном порядке,
        # чтобы исходный порядок ничего не выдавал.
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()

#  Вопросы
# 1. Что будет, если изменить константу NUM_DIGITS?
# Ответ: Изменится количество угадываемых цифр.

# 2. Что будет, если изменить константу MAX_GUESSES?
# Ответ: Изменится количество попыток угадывания.

# 3. Что будет, если задать значение NUM_DIGITS больше 10?
# Ответ: Ошибка - нет нужного индекса

# 4. Что будет,если secretNum=getSecretNum() в строке 30 заменить на secretNum = '123'?
# Ответ: Загадываемое число всегда будет '123'

# 5. Какое сообщение об ошибке вы получите, если удалите или закомментируете numGuesses = 1 в строке 34?
# Ответ: Переменная вызывается перед ее созданием

# 6. Что будет, если вы удалите или закомментируете random.shuffle(numbers) в строке 62?
# Ответ: Числа всегда будут по порядку 01234567889

# 7. Что будет, если вы удалите или закомментируете if guess == secretNum:
# в строке 74 и return 'You got it!' в строке 75?
# Ответ: Нельзя будет увидеть информацию о том что выиграл. (Ферми, Ферми, Ферми)...

# 8. Что будет, если вы закомментируете numGuesses += 1 в строке 44?
# Ответ: Попытки будут бесконечными
