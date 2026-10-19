
def numDecodings(self, s: str) -> int:
    def helper(idx, memo={}):

        if idx in memo:
            return memo[idx]

        if idx == len(s):
            return 1

        if s[idx] == '0':
            return 0

        if idx == len(s) - 1:
            return 1

        ans = helper(idx + 1)
        if int(s[idx:idx + 2]) <= 26:
            ans += helper(idx + 2)

        memo[idx] = ans
        return ans



# https://leetcode.com/problems/decode-ways-ii/
# Works but TLE in Leetcode.
def num_decodings(s):
    def helper(idx, string, memo={}):
        if idx in memo:
            return memo[idx]

        if idx == len(string):
            return 1

        if string[idx] == '0':
            return 0

        if idx == len(string) - 1 and string[idx] != '*':
            return 1

        ans = 0
        if s[idx] == '*':
            for i in range(1, 10):
                ans += helper(idx + 1, string[:idx] + str(i) + string[idx + 1:])  # we have replaced the * here
        else:
            ans += helper(idx + 1, string)

        if idx != len(string) - 1:
            sub_str = string[idx:idx + 2]
            if '**' in sub_str:
                # we know here we use a nested loop
                for replacement in [f'{i}{j}' for i in range(1, 10) for j in range(1, 10)]:
                    if int(replacement) <= 26:
                        ans += helper(idx + 2, string[:idx] + replacement + string[idx + 2:])
            elif '*' in sub_str:
                for i in range(1, 10):
                    replacement = f'{sub_str[0]}{i}' if sub_str[1] == '*' else f'{i}{sub_str[1]}'
                    if int(replacement) <= 26:
                        ans += helper(idx + 2, string[:idx] + replacement + string[idx + 2:])
            else:
                if int(sub_str) <= 26:
                    ans += helper(idx + 2, string)

        memo[idx] = ans
        return ans

    return helper(0, s) % (pow(10, 9) + 7)


def num_decodingsII_Efficient(s: str) -> int:

    memo = {}
    def helper(idx):
        if idx == len(s):
            return 1
    
        if s[idx] == '0':
            return 0
        
        if idx in memo:
            return memo[idx]
        
        ans = 0
        if s[idx] == '*':
            ans += 9 * helper(idx + 1)
        else:
            ans += helper(idx + 1)

        if idx != len(s) - 1: # you could also check that idx + 1 < len(s)
            ch1 = s[idx]
            ch2 = s[idx + 1]

            if ch1 == '*' and ch2 == '*':
                ans += 15 * helper(idx + 2)
            elif ch1 == '*' and ch2 != '*':
                
                # this case is *N, this is 1 way if N is > 6 e.g, 17, 27 does not map. So * can only be 1
                if int(ch2) > 6:
                    ans += 1 * helper(idx + 2)
                else:
                    ans += 2 * helper(idx + 2)

            elif ch1 != "*" and ch2 == '*':
                # this case is N*. 
                if ch1 == '1':
                    ans += 9 * helper(idx + 2)
                elif ch1 == '2':
                    ans += 6 * helper(idx + 2)
            else:
                # two standard digits
                if 10 <= int(ch1 + ch2) <= 26:
                    ans += 1 * helper(idx + 2)


        ans = ans % (pow(10, 9) + 7)
        memo[idx] = ans
        return ans
    return helper(0)
    


if __name__ == '__main__':
    print(num_decodings('*'))
    print(num_decodings('*1'))
    print(num_decodings('2*'))
    print(num_decodings('1**9'))
    print(num_decodings('*10*1'))
    print(num_decodings("904"))
    print(num_decodings("*********"))
