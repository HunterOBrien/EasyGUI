import random
import easygui

word = "Elephant"
choice_number = 0
for i in range(20):
    choice_number += 1
    letter = easygui.buttonbox(random.choice(word), choice_number, choices=["Ok"])
