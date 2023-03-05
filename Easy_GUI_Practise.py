import easygui
import random

easygui.enterbox("HI! What is your name? ")

for i in range(100):
    number = random.randint(0, 5)
    print(number)

words = ["Bat", "Cat", "Mat", "Hat"]
my_word = random.choice(words)
print(my_word)

word = "Stephanie"
letter = random.choice(word)
print(f"The random letter chosen in {word} is {letter}")