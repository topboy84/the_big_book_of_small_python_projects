import datetime, random


def getBirthdays(numberOfBirthdays):
    """Возвращаем список дат - datetime.date(2001, 5, 19) для случайных дней рождения"""
    birthdays = []
    for i in range(numberOfBirthdays):
        # Год должен быть одинаковый, год не учитывается, нужны лишь дни
        startOfYear = datetime.date(2001, 1, 1)
        # Получаем случайный день года
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        print(randomNumberOfDays)
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Возвращаем повторяющиеся даты из списка дней рождения"""
    if len(birthdays) == len(set(birthdays)):
        # Через коллекцию проверяем повторы, повторов нет возвращаем None
        return None

    # сравнение все ДР друг с другом
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Возвращаем совпадение


print("Парадокс Дней рождений!")
print("""— утверждение, состоящее в том, что в группе, состоящей из 23 или более человек, 
вероятность совпадения дней рождения (число и месяц) хотя бы у двух людей превышает 50%. 
Например, если в классе 23 ученика или более, то более вероятно то, 
что у какой-то пары одноклассников дни рождения придутся на один день, 
чем то, что у каждого будет свой неповторимый день рождения. 
Впервые эта задача была рассмотрена Рихардом Мизесом в 1939 году.""")

MONTHS = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')

while True:
    print("Сколько сгенерировать дней рождений(макс 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break  # Корректное значение

# Генерация и отображение ДР
print("Тут ", numBdays, 'дней рождения: ')
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Выводим запятую для каждого дня рождения после первого
        print(", ", end="")
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')

# Выясняем, встречаются ли два совпадающих дня рождения.
match = getMatch(birthdays)

# Отображаем результаты:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
    print()
# Производим 100 000 операций имитационного моделирования:
print('Сгенерируем', numBdays, 'случайных ДР 100,000 раз...')
input('Нажми Enter чтобы продолжить...')

print('Давайте проведем еще 100 000 симуляций.')
simMatch = 0  # Число операций моделирования с совпадающими днями рождения.
for i in range(100_000):
    # Отображаем сообщение о ходе выполнения каждые 10 000 операций:
    if i % 10_000 == 0:
        print(i, 'симуляция выполняется...')
    birthdays = getBirthdays(numBdays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 симуляций выполняется...')

# Отображаем результаты имитационного моделирования:
probability = round(simMatch / 100_000 * 100, 2)
print('Из 100 000 симуляций', numBdays, '- количесво выбраных челоек')
print('совпадает день рождения в этой группе', simMatch, 'раз. Это означает')
print('что', numBdays, 'людей имеют', probability, '% шанс чтобы')
print('у них был одинаковый день рождения в их группе.')
print('Это, вероятно, больше, чем вы думаете!')
