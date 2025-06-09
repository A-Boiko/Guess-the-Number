import random

random_number = random.randint(1, 100)
number_of_attempts = 7
print (random_number)
print(f"Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за {number_of_attempts} спроб.")

for i in range(7):
    number = int(input("Введіть ваше припущення: "))
    if number<random_number:
       print("Занадто маленьке!")
    elif number>random_number:
        print("Занадто велике!")
    else:
        print(f"Ви вгадали! Це число {number}.")
        break;
    if i==6:
        print(f"Ви вичерпали всі спроби! Це число {random_number}.")
