Given a non-empty array nums containing only **positive integers**, find if the array can be 
partitioned into two subsets such that sum of elements in both are equal



Approach:
Since it's a non-empty array we are sure that there is something in the input
There are some facts that needs to be stated
1. The sum(elements) / 2 must be an int for there to be equal subsets
2. We need to have at least two elements in the array nums to be able to split
e.g., nums = [1] cannot be split into two equal subsets.
   
With those two assumptions in mind, our approach will be to sum up all
the elements and divide by 2 and check for elements 