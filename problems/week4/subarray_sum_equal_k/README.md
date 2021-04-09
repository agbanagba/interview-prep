Given an array of integers nums and an integer k, return the total number of
**continuous subarrays** whose sum equals to k

Questions:
1. Does the array contain negative numbers? For this we'll assume it does to make it interesting
2. 


Brute Force Approach:
We want to check every continuous block subarray starting first starting at i = 0 and add from i to m where m <=n and n
being the size of the array until array at i <= target k. Then move on to i = 1 and repeat the process
This process continues until i = n -1

This approach exceeds the time limit on leetcode.

Time Complexity - O(n^2)
Space Complexity - O(n)


More efficient approach:
