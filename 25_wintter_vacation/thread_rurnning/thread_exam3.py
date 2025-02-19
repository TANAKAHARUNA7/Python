from asyncio import sleep
import threading

balance = 0

def deposit():
    global balance
    amount = 10
    for count in range(10):
        balance = balance + amount
        sleep(0.01)
        print(f"Deposit! balance : {balance}")
        
def withdraw():
    global balance
    
    for count in range(10):
        amount = 10
        sleep(0.01)
        balance -= amount 
        print(f"Withdraw!, ")
            

thread_1 = threading.Thread(target=deposit)
thread_2 = threading.Thread(target=withdraw)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f"[balance]: {balance}")
