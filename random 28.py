print("Задание", 1)
import random
print(random.randint(1, 100))

print("Задание", 2)
import random

frukts = ['банан', 'яблоко', 'апельсин', 'грейпфрут', 'киви']
print(random.choice(frukts))

print("Задание", 3)
import random

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(spisok)
print(spisok)

print("Задание", 4)
import random

random = random.sample(range(50), 5)
print(random)

print("Задание", 5)
import random
colors = ['красный', 'зеленый', 'синий']
random_colors = [random.choice(colors) for i in range(4)]
print(random_colors)

print("Задание", 7)
import random 
def passw_generator(count_char=8):
    arr = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', "Z", "X", "C", "V", "B", "N", "M", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
passw = []