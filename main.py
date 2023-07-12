tickets = int(input("Сколько билетов вы хотите приобрести : "))

payment = 0.0

for i in range(tickets):
    age = int(input("Введите возраст "+str(i+1)+"-го посетителя :"))
    if age >= 25:
        payment += 1390
    elif age >= 18:
        payment += 990

if tickets > 3:
    payment *= 0.9

print("Общая стоимость билетов : ", payment)