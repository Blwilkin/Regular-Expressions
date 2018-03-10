def Phone(text):
    if len(text) != 3:
        return False
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False
    return True
print(Phone('345'))

message = 'Call me at 356.'
for i in range(len(message)):
    chunk = message[i:i+3]
    if Phone(chunk):
        print('Phoney ' + chunk)
print('Yes')