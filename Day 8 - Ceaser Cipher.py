alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(message,shift_position):
    processed_message = ""
    for char in message:
        if char in alphabets:
            shifted_position = (alphabets.index(char))+shift_position
            shifted_position %= len(alphabets)
            processed_message += alphabets[shifted_position]
        else :
            processed_message += char
    print(f'Your message is {processed_message}')

def decrypt(message,shift_position):
    processed_message = ""
    for char in message:
        if char in alphabets:
            shifted_position = (alphabets.index(char)) - shift_position
            shifted_position %= len(alphabets)
            processed_message += alphabets[shifted_position]
        else:
            processed_message += char
    print(f'Your message is {processed_message}')

repeat = True

while repeat:
    direction = input("select encode or decode: ").lower()
    text = input("enter the text: ").lower()
    shift = int(input("enter the number of positions to shift: "))
    if direction == 'encode':
        encrypt(text,shift)
    elif direction == 'decode':
        decrypt(text,shift)
    else :
        print("Invalid Option!")
    repeat = input("Do you want to continue? Yes / No : ").lower()
    if repeat == 'yes':
        repeat = True
    else :
        repeat = False
