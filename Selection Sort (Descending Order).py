numbers = [64, 25, 12, 22, 11]

n = len(numbers)

for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        if numbers[j] > numbers[max_index]:
            max_index = j

    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

print("Descending order:", numbers)
