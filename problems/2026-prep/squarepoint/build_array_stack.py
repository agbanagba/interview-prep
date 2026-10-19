from typing import List

def buildArray(target: List[int], n: int) -> List[str]:

    result = []
    j = 0
    i = 1
    while i < n + 1 and j < len(target):
        # the question here is that are we close to target
        # but before that, do we need to do a pop before push
        # we always do a push
        if i == target[j]:
            result.append("Push")
            i += 1
            j += 1
        else:
            result.append("Push")
            result.append("Pop")
            i += 1

    return result


if __name__ == "__main__":

    target = [1, 2]
    print(buildArray(target, 4))
