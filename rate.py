Rub = float(input("Введите количество рублей: "))
print("Выберите валюту для конвертации:")
print("1. Доллары")
print("2. Евро")
print("3. Юани")

Dollar = 100  
Euro = 105    
Yuan = 15     

choise = int(input("Введите номер валюты: "))

if choise == 1:
    result = Rub / Dollar
    print(f"Вы получите {result:.2f} долларов.")
elif choise == 2:
    result = Rub / Euro
    print(f"Вы получите {result:.2f} евро.")
elif choise == 3:
    result = Rub / Yuan
    print(f"Вы получите {result:.2f} юаней.")
else:
    print("Некорректный выбор валюты.")