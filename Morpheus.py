import random

class Pill:
    def __init__(self, color, hand):
        self.color = color
        self.hand = hand

def refillArray():
    f_array = []
    for i in range(0, 7):
        f_array.append(Pill("blue", "left"))

    for i in range(0, 3):
        f_array.append(Pill("red", "left"))

    for i in range(0, 5):
        f_array.append(Pill("blue", "right"))

    for i in range(0, 8):
        f_array.append(Pill("red", "right"))

    return f_array

left = 0
right = 0

while left + right < 100000:
    array = refillArray()
    while True:
        index = random.randint(0, len(array)-1)
        pill = array[index]
        if pill.color == "red":
            break
    if pill.hand == "right":
        right += 1
    else:
        left += 1

print "Left: " + str(left) + ", " + str(float(left)*100/(left + right))  + "%. Right: " + str(right) + ", " + str(float(right)*100/(left + right)) + "%"


