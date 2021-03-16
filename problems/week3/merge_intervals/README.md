Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of
the non-overlapping intervals that cover all the intervals in the input.

https://leetcode.com/problems/merge-intervals/

Questions.

1. What is an overlap?
2. is each interval in ascending order?

Approach:

1. sort the intervals based on the start values and use a stack data structure. When we do that we know we are comparing
   the end values of what's already in the stack and what we get.
2. compare the end value of the interval with the max end with the start value of the interval with the min end.
3. If (2) above is true i.e. max_end_end > min_end_start, there is an overlap, and we merge and put into the stack else
   we just append the current interval.

Time Complexity - The complexity of the sort is O(nlogn) and that overshadows that of the rest of the algorithm. \
Space Complexity - For sorting, it's O(logn) and using a stack to hold our result, that can grow to O(n) in a worst case
where there is no overlap. So it's O(n)
