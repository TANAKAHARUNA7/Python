star_up = 1
space_down = 4

for i in range(5):
    print(" " * space_down, "*" * star_up )
    star_up += 2
    space_down -= 1

star_up = 7
space_down = 1
for i in range(4):
    print(" " * space_down, "*" * star_up)
    star_up -= 2
    space_down += 1