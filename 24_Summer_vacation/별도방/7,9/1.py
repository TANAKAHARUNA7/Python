# import os
# print(os.getcwd())

# with open('kin/example.txt', 'r') as file:
#     content = file.read()
#     print(content)
    
    
# with open('kin/example.txt', 'w') as file:
#     file.write("Hello, World!")
    

# with open('kin/example.txt', 'a') as file:
#     file.write("\nHello again!")
    

with open('kin/example.txt', 'r+') as file:
    content = file.read()
    print('Original Content: ',content)
    file.seek(0) 
    file.write('Updated Content')    
    
    
    
    