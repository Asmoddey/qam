# читаємо ввод користувачем данних і
# записуємо в змінні 
name_1 = input("Введіть перше ім'я: ")
name_2 = input("Введіть друге ім'я: ")
# отримуємо довжину змінної і присвоюємо у змінну
len_name_1 = len(name_1)
len_name_2 = len(name_2)
# якщо довжина_імені_1 менше довжина_імені_2
if  len_name_1 < len_name_2:
    print(f"найдовше ім'я: {name_2}")
# якщо довжина імен однакова
elif len_name_1 == len_name_2:
    print("імена однакові")
else:
    print(f"найдовше ім'я: {name_1}")