import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    total = sum(item["score"] * item["weight"] for item in data)
    total = round(total, 3)

    return total


print(task())
