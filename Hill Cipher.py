import math
size = int(math.sqrt(int(input())))
elements = input()
message = input()
key_matrix=[]
cipher_list=[]

input_list = [int(i)for i in elements.split()]
for i in range(size):
    row = []
    for j in range(size):
        row.append(input_list[0])
        input_list = input_list[1:]
    key_matrix.append(row)

ciphertext=""
message_list = [ord(char)-65 for char in message]
if len(message_list) == 0:
    message_list.append(23)
while len(message_list)>0:
    while len(message_list)>0 and len(message_list)<size:
        message_list.append(23)
    block = message_list[0:size]
    for i in range(size):
        cipherchar=0
        for j in range(size):
            cipherchar+=((key_matrix[i][j]*block[j]))
        cipher_list.append(cipherchar%26)
    for i in range(size):
        ciphertext =ciphertext+chr(cipher_list[i]+65)
    cipher_list=[]
    if len(message_list) == size:
        message_list = []
    else:
        message_list = message_list[size:]
print(ciphertext)

