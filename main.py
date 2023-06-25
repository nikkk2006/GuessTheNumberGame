from random import randint


def main():
    MIN_VALUE = 1
    MAX_VALUE = 100
    random_number = randint(MIN_VALUE, MAX_VALUE)
    user_number = int(input("Введите загаданное число: "))
    attempts = 0

    while user_number != random_number:
        attempts += 1

        if user_number > random_number:
            print(f"Число {user_number} больше загаданного числа")
        elif user_number < random_number:
            print(f"Число {user_number} меньше загаданного числа")
        user_number = int(input("Введите загаданное число: "))

    print(f"Поздравляю, ты угадал число за количество попыток: {attempts}")




if __name__ == '__main__':
    main()