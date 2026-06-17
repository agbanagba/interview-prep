
# Time complexity is O(logn) - we are red
# Same solution for isPowerofTwo and isPowerofThree. 
# There is an O(1) solution that uses bitwise operators but may not be required in an interview.
def isPowerofFour(n: int) -> bool:

    if n <= 0:
        return False
    
    while n % 4 == 0:
        n //= 4
    return n == 1