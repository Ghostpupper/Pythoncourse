# Caesar cipher
text = input("Enter your message: ")
while True:
    shiftvalue= input("Enter the shiftvalue: ")
    if shiftvalue.isalnum():
        shiftvalue=int(shiftvalue)
        if shiftvalue > 25:
            print('too high, try again')
            continue
        elif shiftvalue < 1:
            print('too low, try again')
            continue
        break
    else:
        answer = input('Not a valid input. Use standard value? Y/N').upper()
        if answer == 'Y':
            shiftvalue= 1
            break
        else:
            continue

cipher = ''

for char in text:
    if not char.isalpha():
        cipher += char
        continue
    code = ord(char) + shiftvalue
    if char.isupper():
        if code > ord('Z'):
            code = ord('A') + (code - ord('Z') - 1)
        cipher += chr(code)
    elif char.islower():
        if code > ord('z'):
            code = ord('a') + (code - ord('z') - 1)
        cipher += chr(code)

print(cipher)