import math

def getExitOrder(x: int, amounts: list[int]) -> list[int]:

    people = []
    for i in range(len(amounts)):
        turns = math.ceil(amounts[i] / x)

        people.append((turns, i + 1))

    people.sort()

    result = []
    for person in people:
        result.append(person[1])
    return result


if __name__ == "__main__":
    amts = [100, 200, 50, 150, 90]
    print(getExitOrder(100, amts))