
# This is my attempt and it's not correct. 
def isMatch(s: str, p: str) -> bool:

    memo = {}
    def helper(i, j, prev_rule):
        if i == len(s):
            return True
        
        # I'm not sure what is the false case but we have to figure it out. 
        # I believe the false case is when nothing matches below so current rule is not a . or a * and it does not match with current string at i. 
        # we return  false. 
        if p[j] not in ".*" and s[i] != p[j]:
            return False

        if (i, j, prev_rule) in memo:
            return memo[(i, j, prev_rule)]
        
        if s[i] == p[j] or p[j] == '.':
            ans = helper(i + 1, j + 1, p[j])
        else:
            # at this point, we have a * at j
            # if prev rule is ., we have a match. now we extend i but leave j. 
            # if it's not a ., then it's a letter a-z and we check if it matches s[i]
            if prev_rule == '.' or s[i] == prev_rule:
                ans = helper(i + 1, j, prev_rule)
            else:
                # it's different than prev rule  where prev_rule is a-z. so we need to keep i as we have exhausted match on prev rule.
                # we also pass in an empty string in prev rule as we don't have a prev rule to work with anymore. (We just worked with a *) so the 
                # realistic next rule is either a . or a letter. 
                ans = helper(i, j + 1, "")

        memo[(i, j, prev_rule)] = ans
        return ans

    return helper(0, 0, "")


def isMatch_Correct(s: str, p: str) -> bool:

    memo = {}
    def helper(i, j):
        if j == len(p):
            return i == len(s)
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        match = i < len(s) and (s[i] == p[j] or p[j] == '.') 
        if j + 1 < len(p) and p[j + 1] == '*':
            ans = helper(i, j + 2) or (match and helper(i + 1, j))
        else:
            ans = match and helper(i + 1, j + 1)
        
        memo[(i, j)] = ans
        return ans
    
    return helper(0, 0)


if __name__ == "__main__":
    val = isMatch("ab", ".*")
    print(val)