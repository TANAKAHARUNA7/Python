
# dans = [2, 4, 6, 8]

# for dan in dans:
#     for i in range(1,10):
#         print(f"{dan} X {i} = {dan*i}", end = "   ",)
#     print()  
    
    
# for dan1 in range(2,9):
#     if dan1 % 2 != 0:
#         continue
#     for dan2 in range(1,10):
#         print(f"{dan1} X {dan2} = {dan1*dan2}", end = "    ")
#         if dan2 % 3 == 0:
#             print()
#         print()
        
        
for dan1 in range(2,9,2):
    for dan2 in range(1,10):
        print(f"{dan1} X {dan2} = {dan1*dan2}",end ="\t")
        if dan2 % 3 == 0:
            print()
    print("\n")