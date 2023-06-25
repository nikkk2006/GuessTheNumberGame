from random import randint


def endTheWord(attempts):
    end = ""

    if 11 <= attempts % 100 <= 14:
        end = "ок"
    elif attempts % 10 == 1:
        end = "ка"
    elif 2 <= attempts % 10 <= 4:
        end = "ки"
    else:
        end = "ок"

    return end

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

    ending_of_the_word = endTheWord(attempts)
    print(f"Поздравляю, ты угадал число и потратил {attempts} попыт{ending_of_the_word}")


if __name__ == '__main__':
    main()