payment = 0.0

tickets = int(input("Сколько билетов вы хотите приобрести : "))

for i in range(tickets):
    age = int(input("Введите возраст "+str(i+1)+"-го посетителя : "))
    if age < 18:
        payment += 0
    elif age >= 18 and age <= 25:
        payment += 990
    elif age > 25:
        payment += 1390

if tickets > 3:
    payment *= 0.9

print("Общая стоимость билетов : ", payment)