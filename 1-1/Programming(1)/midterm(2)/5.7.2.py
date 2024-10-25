row_count = 5
blank_count = 4
star_count = 1


for _ in range(row_count):
    # print for blanks
    for _ in range(blank_count): # loop for blanks
        print(" ", end = "")
        
    # print for "*"    
    for _ in range(star_count): # loop for "*"
        print("*", end="")
        # print "\n"
    print()
    # update for count values
    star_count += 2
    blank_count -= 1