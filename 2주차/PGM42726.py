numbers = [3, 30, 34, 5, 9]
numbers = [str(i) for i in numbers]

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        for k in (range(len(numbers[i])) if len(numbers[i])<len(numbers[j]) else range(len(numbers[j]))):
            if int(numbers[i][0]) < int(numbers[j][0]):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                break



print(''.join(numbers))