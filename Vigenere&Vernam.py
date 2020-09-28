from operator import xor
Key = input()
Message = input()
Vigenere = ""
Vernam = ""
keyindex=0
for char in Message:
    keychar=Key[keyindex]
    Vigenere = Vigenere+chr(((ord(char)-65+ord(keychar)-65) % 26)+65)
    next_ver_char = hex(xor(ord(char), ord(keychar)))[2:].upper()
    if len(next_ver_char) == 1:
        next_ver_char = "0"+next_ver_char
    Vernam = Vernam+next_ver_char
    keyindex=(keyindex+1)%len(Key)
if len(Key)==len(Message):
    isonetime="YES"
else:
    isonetime="NO"
print("Vigenere: "+Vigenere)
print("Vernam: "+Vernam)
print("One-Time Pad: "+isonetime)

