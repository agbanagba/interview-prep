# This works but will throw a time limit exceeded in leetcode
def daily_temps(temps):
    ret = []
    for i in range(len(temps)):

        val = 0
        j = i + 1
        while j < len(temps):
            if temps[j] > temps[i]:
                val = j - i
                break
            j += 1
        ret.append(val)
    return ret


def daily_temps_efficient(T):
    stack = []
    res = [0 for _ in range(len(T))]
    for i, t1 in enumerate(T):
        while stack and t1 > stack[-1][1]:
            j, t2 = stack.pop()
            res[j] = i - j
        stack.append((i, t1))
    return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temps_efficient(temperatures))
