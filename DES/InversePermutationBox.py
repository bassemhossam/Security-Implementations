size = int(input())
order = input()
order_list = [int(number)for number in order.split()]
out_box = ""
for i in range(size):
    if i+1 in order_list:
        if order_list.count(i+1) > 1:
            out_box = "IMPOSSIBLE"
            break
        else:
            out_box += str(order_list.index(i+1)+1)
            if i != size-1:
                out_box += " "
    else:
        out_box = "IMPOSSIBLE"
        break
print(out_box)