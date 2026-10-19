from collections import defaultdict

# This is the brute force approach
def characterReplacement(s: str, k: int) -> int:
    result = 0
    for i in range(len(s)):
        count, maxf = defaultdict(int), 0
        for j in range(i, len(s)):
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])
            window_size = j - i + 1
            if window_size - maxf <= k:
                result = max(result, window_size)

    return result


def characterReplacementOptimal(s: str, k: int) -> int:

    count = defaultdict(int)
    result = 0

    maxf = 0
    left = 0
    for right in range(len(s)):
        count[s[right]] += 1
        maxf = max(maxf, count[s[right]])

        while (right - left + 1) - maxf > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result
