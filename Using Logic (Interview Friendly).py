numbers = [4, 1, 3, 2]

sorted_list = []

while numbers:
    min_val = numbers[0]
    for i in numbers:
        if i < min_val:
            min_val = i
    sorted_list.append(min_val)
    numbers.remove(min_val)

print("Sorted list:", sorted_list)
