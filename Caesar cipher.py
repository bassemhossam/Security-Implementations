Key = input()
Message = input()
Key = int(Key)
EncryptedMessage = ""

for char in Message:
    EncryptedMessage = EncryptedMessage+chr(((ord(char)-65+Key) % 26)+65)
print(EncryptedMessage)
