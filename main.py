# Задача "Квадрат и прямоугольник"
print ("Квадрат и прямоугольник")
a_square = int(input("Введите значение стороны квадрата, см: "))

perimeter_square = a_square*4
area_square = a_square*a_square

print ("Сторона квадрата, см = ", a_square)
print ("Площадь, см2 = ", area_square)
print ("Периметр, см = ", perimeter_square)


a_rectangle = int(input("Введите значение ширины прямоугольника, см: "))
b_rectangle = int(input("Введите значение высоты прямоугольника, см: "))

perimeter_rectangle = (a_rectangle+b_rectangle)*2
area_rectangle = a_rectangle*a_rectangle

print ("Ширина прямоугольника = ", a_rectangle)
print ("Высота прямоугольника = ", b_rectangle)
print ("Площадь = ", area_square)
print ("Периметр = ", perimeter_square)
print (" ")
# Задача "Финансы"
print ("Финансы")

salary = int(input("Введите значение заработной платы, руб.: "))
percent_mortgage = int(input("Введите значение процента на ипотеку, %: "))
percent_life = int(input("Введите значение процента расходов на жизнь, %: "))

percent_accumulation = 100 - (percent_mortgage + percent_life)

mortgage = salary * 12 * percent_mortgage / 100
accumulation = salary * 12 * percent_accumulation / 100

print ("Зарплата, руб. = ", salary)
print ("Процент на ипотеку, % = ", percent_mortgage)
print ("Траты на жизнь, % = ", percent_life)
print ("Ипотека, руб. = ", mortgage)
print ("Накоплено, руб. = ", accumulation)