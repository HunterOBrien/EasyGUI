import random
import easygui

choice_number = 0
p_one = []
p_two = []

for i in range(1):
    choice_number += 1
    p1_die1 = random.randint(1, 6)
    p1_die2 = random.randint(1, 6)
    p_one.append(p1_die1)
    p_one.append(p1_die2)

for i in range(1):
    choice_number += 1
    p2_die1 = random.randint(1, 6)
    p2_die2 = random.randint(1, 6)
    p_two.append(p2_die1)
    p_two.append(p2_die2)

easygui.msgbox(f"Player One Got {p_one} and a Sum of {sum(p_one)}\n Player Two Got {p_two} and a Sum of {sum(p_two)}")
