import random
NUM_DIGIT = 3

numbers = list('0123456789')
random.shuffle(numbers)
secretNum = ''
for i in range(NUM_DIGIT):
    secretNum += str(numbers[i])
    print(i)