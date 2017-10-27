# 100 Doors Problem
#
# There are 100 doors numbered 1-100 and are all closed
# You make 100 passes by the doors starting with the first door
# The first pass, you visit every door and switch the doors' state (if the door is closed you open it and vice versa)
# The second pass, you visit and switch the state of any door whose number is divisible by 2
# The third pass, you visit and switch the state of any door whose number is divisible by 3
# You keep going until you only visit and switch the 100th door
# Which doors are open after 100 passes?

door_list = []
doors_open = []
size = 100

for n in range(size):
    door_list.append(False)

for y in range(size):
    for z in range(size):
        if ( (z+1) % (y+1) == 0):
            door_list[z] = not door_list[z]

for i, j in enumerate(door_list):
    if j is True:
        doors_open.append(i+1)

print(doors_open)
