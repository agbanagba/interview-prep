Remove the outermost parenthesis give a parentheses string  
https://leetcode.com/problems/remove-outermost-parentheses/

Example

    1.  Input = "(()())(())"
        Output = "()()()"

    2.  Input = "()()"
        Output = ""
        

Assumptions/Questions:
1. A valid parenthesis string can be empty ('') which should give ''
2. An empty string '' is a valid parenthesis string

Approach:
We want to decompose the parenthesis string into primitive decompositions and take out
the outermost parenthesis of each primitive and return what's left.

Naive Solution/First Solution:
Go through the parenthesis string and look for individual primitive decompositions
then return without 0 and n-1 of each primitive

How do we identify a primitive decomposition?
A primitive decomposition is one that starts with an open brace '(' and can exist in two states  
    a. When there is no preceding item with an immediate close brace
    b. A closing brace ')' behind the open bra

a. A preceding open brace signifies the current one is not a primitive