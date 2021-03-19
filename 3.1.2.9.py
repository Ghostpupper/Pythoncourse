import time

while (True):
    word = input("You're in a loop, you need to say the secret word in order to get out.\n")
    if word == 'chupacabra' or word == 'Chupacabra': break
    else: print("Wrong!")

    time.sleep(1)

print("Thats correct! You have successfully left the loop")