from collections import defaultdict

import heapq

def print_message(n: int, message: str) -> None:
    if n == 0:
        return
    
    print("\n\n".join([message] * n))
    

def square_and_reverse(nums):
    
    result = []
    for num in reversed(nums):
        result.append(num ** 2)
        
    return result

def fizz_buzz(n: int) -> str:
    
    result = []
    for i in range(1, n + 1):
        is_divisible_by_3 = (i % 3 == 0)
        is_divisible_by_5 = (i % 5 == 0)
        
        if is_divisible_by_3 and is_divisible_by_5:
            result.append("FizzBuzz")
        elif is_divisible_by_3:
            result.append("Fizz")
        elif is_divisible_by_5:
            result.append('Buzz')
        else:
            result.append(str(i))
    
    return ",".join(result)

def word_counter(sentence: str) -> dict[str, int]:
    result = defaultdict(int)
    
    for word in sentence.split():
        result[word] += 1
    return result


def second_unique(nums: list[int]) -> int:
    largest = float('-inf')
    second = float('-inf')
    
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
        
    if second == float('-inf'):
        return None
    
    return second

def second_most_frequent(nums: list[int]) -> int | None:
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1
        
    if len(counter.keys()) <= 1:
        return None
    
    counter_heap = []
    for k, v in counter.items():
        heapq.heappush_max(counter_heap, (v, k))
        
    heapq.heappop_max(counter_heap)
    return counter_heap[0][1]