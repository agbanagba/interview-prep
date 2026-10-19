from typing import List

# Scenario 1:
#   Two pointers left and right after sorting can share a boat
#   => Is the boat at capacity -> Advance both left and right pointers and continue
#   => is the boat not at capacity -> Advance left pointer until boat reaches or exceeds capacity. 

# Scenario 2:
#   Two pointers cannot share a boat. total of both exceeds capacity/limit
#       increment counter
#       advance right pointer inwards as it's in it's own boat.

# My solution here depends on using two numbers. In scenario 2, one number is used
# scenario 1 on the other hand requires two numbers. 
def numRescueBoats(people: List[int], limit: int) -> int:

    people.sort()

    boats = 0
    left, right = 0, len(people) - 1

    while left <= right:
        total = people[left] + people[right]
        if total <= limit:
            left += 1
        boats += 1
        right -= 1

    return boats


if __name__ == "__main__":
    people = [3, 2, 2, 1]
    limit = 3
    print(numRescueBoats(people, limit))