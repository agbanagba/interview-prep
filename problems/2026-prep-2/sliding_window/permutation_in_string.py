

def checkInclusion(s1: str, s2: str) -> bool:

    if len(s1) > len(s2):
        return False

    need = [0] * 26
    for ch in s1:
        need[ord(ch) - ord('a')] += 1

    left = 0
    for right in range(len(s2)):
        ch = s2[right]
        idx = ord(ch) - ord('a')
        need[idx] -= 1

        while need[idx] < 0:
            need[ord(s2[left]) - ord('a')] += 1
            left += 1
 
        if right - left + 1 == len(s1):
            return True

    return False

  


if __name__ == "__main__":
    s1 = "abc"
    s2 = "lecaabee"
    print(checkInclusion(s1, s2))