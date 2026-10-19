from typing import List

# The naive approach is to think about this in pairs of complete parenthesis and add another pair beside or inside. 
# That solution is difficult to write. 
# The good solution is thinking about it as indiviual characters from an empty string. 
# 1. Start from an empty string and ask can I add an open or close parenthesis. 
def generateParenthesis(n: int) -> List[str]:
    
    result = []
    def backtrack(s, open, close):
        
        if len(s) == 2 * n:
            result.append(s)
            return

        if open < n:
            backtrack(s + "(", open + 1, close)

        if close < open:
            backtrack(s + ')', open, close + 1)

    backtrack("", 0, 0)
    return result


# The above approach does not do a pop after the backtrack. Here is an approach that uses a List to 
# highlight the backtrack unchoose model. 

def generateParenthesis_AnotherVersion(n: int) -> List[str]:

    result = []

    def backtrack(slist, open, close):

        if len(slist) == 2 * n:
            result.append("".join(slist))
            return

        if open < n:
            slist.append('(')
            backtrack(slist, open + 1, close)
            slist.pop()

        if close < open:
            slist.append(')')
            backtrack(slist, open, close + 1)
            slist.pop()
        
    backtrack([], 0, 0)
    return result


if __name__ == "__main__":
    print(generateParenthesis(5))