from typing import List

def getFactors(self, n: int) -> List[List[int]]:
    

    def backtrack(num, start, path):

        if path:
            result.append(path + [num])

        for i in range(start, int(num ** 0.5) + 1):
            if num % i == 0:
                path.append(i)
                backtrack(num // i, i, path)
                path.pop()

    result = []
    backtrack(n, 2, [])
    return result