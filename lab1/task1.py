numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_missing_el = numbers.index(None)
avg = (sum(numbers[:index_missing_el]) + sum(numbers[(index_missing_el + 1):])) / len(numbers)
numbers[index_missing_el] = avg

print("Измененный список:", numbers)
