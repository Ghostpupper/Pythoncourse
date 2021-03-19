message = input('input your message:')
message = message.lower()
message = message.replace(' ','')
message= list(message)
result = True
for i in range(int(len(message)/2)):
    if message[i] == message[len(message) - i - 1]:
        continue
    else:
        result = False
        break

if result:
    print("its a palindrome")
else:
    print('its not a palindrome')