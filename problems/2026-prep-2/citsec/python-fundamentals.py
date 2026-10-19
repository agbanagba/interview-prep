from collections import defaultdict
from typing import List

import heapq

def print_message(n: int, message: str) -> None:
    if n == 0:
        return

    print("\n\n".join([message] * n))


def square_and_reverse(nums):

    return [item ** 2 for item in nums[::-1]]

def fizz_buzz(n: int) -> str:


    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return ",".join(result)

def word_counter(sentence: str) -> dict[str, int]:

    result = defaultdict(int)
    for word in sentence.split():
        result[word] += 1

    return result

def second_most_frequent(nums: List[int]) -> int | None:

    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1

    if len(counter.keys()) <= 1:
        return None

    counter_heap = []
    for key, val in counter.items():
        heapq.heappush_max(counter_heap, (val, key))

    heapq.heappop_max(counter_heap)
    return counter_heap[0][1]

def second_unique(nums: List[int]) -> int | None:
    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    if second == float('inf'):
        return None

    return second
    



if __name__ == "__main__":
    print_message(10, "Tega")
    print(word_counter("the cat sat on the mat"))
    print(second_unique([3, 1, 4, 4, 5, 5, 2]))
