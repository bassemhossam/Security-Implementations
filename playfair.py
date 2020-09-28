
key = input()
message = input()
message = message.replace("J", "I")
key = key.replace("J", "I")

input_list = []
key_matrix = []
ciphertext=""
for char in key:
    if char not in input_list:
        input_list.append(char)
for k in range(26):
    if chr(k+65) not in input_list and chr(k+65) != 'J':
        input_list.append(chr(k+65))

if len(message) == 1:
    if message == "X":
        message = message+"Q"
    else:
        message = message+"X"

index = 0
'''
while index < len(message) - 1:
    if (message[index] == message[index + 1]):
        if message[index] == "X":
            addedchar = "Q"
        else:
            addedchar = "X"
        message = message[0:index + 1] + addedchar + message[index + 1:]

    index += 1
    

'''
for i in range(5):
    row = []
    for j in range(5):
        row.append(input_list[0])
        input_list = input_list[1:]
    key_matrix.append(row)



def search(x):
    for q in range(5):
        if x in key_matrix[q]:
            return [q, key_matrix[q].index(x)]


while len(message)>0:
    if len(message) == 1:
        if message == "X":
            message = message + "Q"
        else:
            message = message + "X"

    char1 = message[0]
    char2 = message[1]
    if char1 == char2:
        flag = True
        if char1 == "X":
            char2 = "Q"
        else:
            char2 = "X"
    else:
        flag = False

    [row1, col1] = search(char1)
    [row2, col2] = search(char2)

    if col1 == col2:
        outrow1 = (row1+1)%5
        outrow2 = (row2+1)%5
        outcol1 = outcol2 = col1

    elif row1 == row2:
        outcol1 = (col1+1) % 5
        outcol2 = (col2+1) % 5
        outrow1 = outrow2 = row1
    else:
        outrow1 = row1
        outcol1 = col2
        outrow2 = row2
        outcol2 = col1
    ciphertext += key_matrix[outrow1][outcol1]+key_matrix[outrow2][outcol2]
    if flag:
        message = message[1:]
    else:
        message = message[2:]

print(ciphertext)
