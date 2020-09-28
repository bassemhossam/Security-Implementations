out_size = int(input())
order = input()
order_list = [int(number)for number in order.split()]
input_size = int(input())
hex_in = input()
bin_in = bin(int(hex_in, 16))[2:].zfill(input_size)
bin_out = ""


for i in order_list:
    bin_out = bin_out + bin_in[i-1]

hstr = '%0*X' % ((len(bin_out) + 3) // 4, int(bin_out, 2))
print(hstr)
