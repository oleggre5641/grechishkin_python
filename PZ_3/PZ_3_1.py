# Даны три целых числа: A, B, C.
# Проверить истинность высказывания: «Число B находится между числами A и C».

a = input("Введите первое число: ")
b = input("Введите второе число: ")
c = input("Введите третье число: ")

while type(a) != int: # обработка исключений
  try:
    a = int(a)
  except ValueError:
    print("Вы неправильно ввели первое число!")
    a = input("Введите первое число: ")
while type(b) != int: # обработка исключений
  try:
    b = int(b)
  except ValueError:
    print("Вы неправильно ввели второе число!")
    b = input("Введите второе число: ")
while type(c) != int: # обработка исключений
  try:
    c = int(c)
  except ValueError:
    print("Вы неправильно ввели третье число!")
    c = input("Введите третье число: ")


if (a < b < c) or (c < b < a): # проверка истинности высказывания
  print(f"Число {b} находится между числами {a} и {c}")
else:
  print(f"Число {b} не находится между числами {a} и {c}")
