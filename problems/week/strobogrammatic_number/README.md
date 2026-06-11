A strobogrammatic number is a number that looks the same when rotated 180 degrees e.g., 0, 1, 8, 11, 69, 88, 96, 101,
111, 181, 609 etc We are to find a list of numbers of a certain length n

Let's go through single digit numbers < 10\
0, 1 and 8 are strobogrammatic numbers\
6 and 9 are not strobogrammatic but can be used interchangeably so, a number like 609 is strobogrammatic.

Two cases:

1. Single digit numbers or numbers < 10 : 0, 1 and 8 are strobogrammatic
2. Multiple digit numbers : 6 and 9 are inclusive because they mirror each other

Strobogrammatic Number I  - https://leetcode.com/problems/strobogrammatic-number/  
Given a number, check if it's a strobogrammatic number

Clarifications/Assumptions:

1. In a real interview scenario, you might not be told what a strobogrammatic number is and it's worth asking for   
   clarifications. This is defined above though.
2. An empty number string '' is a strobogrammatic number

Input = n: str   
Output = true if strobogrammatic and false otherwise

Approach:
For number to be strobogrammatic, the 180 degrees equivalent of a digit at i must be equal with the digit at n - 1 and
180 deg equivalent at i + 1 must be equal to digit n -2 I can increment i and decrement n and see if that conditions
remains until we get to the middle. But first we a mapping has to be created.

Time Complexity:  O(n) - goes through all digits to check 
Space Complexity: O(1)

Strobogrammatic Number II  -  https://leetcode.com/problems/strobogrammatic-number-ii/  
Clarifications/assumptions here are same as the solution I above.  
Input = n (length)  
Output = List of numbers that have length of n

Naive Approach:  Time Limit Exceeded on Leetcode   
   Go through every number with length n and check if digit contains strobogrammatic numbers if n is 1 and for n > 1 check
   if digits contains the mirror digits.

Efficient Approach:



Strobogrammatic Number III  - https://leetcode.com/problems/strobogrammatic-number-iii/  
