#-*- coding: utf-8 -*-
import random
print("Добро пожаловать, меня зовут Угадай-ка!")
print("\nВы должны загадать натуральное число от 1 до 100")
print("А я при вашей помощи должен его отгадать")
print("Подсказывайте мне словами: \"больше\" или \"меньше\"")
print("Когда я отгадаю, просто скажите мне \"да\", а если не число не верное, то скажите \"нет\" ")
print("Только не обманывайте меня! :)")
input("\nЕсли Вы загадали число, то просто нажмите Enter!")
num = random.randint(1, 100)
count = 0
maximum = 100
minimum = 1
while True:
	if minimum == maximum:
		print("Или это число ", minimum, ", или вы держите меня за дурака и я отказываюсь с Вами играть!")
		break
	count += 1
	print("\nЭто число ", num, "?")
	temp = input("Да или нет? ", )
	if temp == "да" or temp == "Да" or temp == "ДА":
		print("Ура! Мне потребовалось ", count, " попыток!")
		break
	elif temp == "Нет" or temp == "НЕТ" or temp == "нет":
		var = input("Это число больше или меньше? ", )
		if var == "больше" or var == "Больше" or var == "БОЛЬШЕ":
			minimum = num
			num = random.randint(minimum, maximum)
			continue
		elif var == "Меньше" or var == "меньше" or var == "МЕНЬШЕ":
			maximum = num
			num = random.randint(minimum, maximum)
			continue
input("\nНажмите Enter для выхода.")
