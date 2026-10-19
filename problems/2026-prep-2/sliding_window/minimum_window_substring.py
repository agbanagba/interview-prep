
# LC 76 - Hard
def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    need = [0] * 128
    for ch in t:
        need[ord(ch)] += 1

    missing = len(t)
    left = 0 
    best_start, best_len = 0, float('inf')

    for right in range(len(s)):
        ch = s[right]
        if need[ord(ch)] > 0:
            missing -= 1

        need[ord(ch)] -= 1

        while missing == 0:
            if right- left + 1 < best_len:
                best_start, best_len = left, right - left + 1

            need[ord(s[left])] += 1
            if need[ord(s[left])] > 0:
                missing += 1
            left += 1

    return "" if best_len == float('inf') else s[best_start:best_start + best_len]
