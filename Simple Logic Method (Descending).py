numbers = [4, 1, 3, 2]

sorted_list = []

while numbers:
    max_val = numbers[0]
    for i in numbers:
        if i > max_val:
            max_val = i

    sorted_list.append(max_val)
    numbers.remove(max_val)

print("Descending order:", sorted_list)
