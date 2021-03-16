def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    stack = [intervals[0]]

    idx = 1
    while idx < len(intervals):

        interval = intervals[idx]
        prev_interval = stack[-1]

        min_interval, max_interval = (interval, prev_interval) if prev_interval[1] >= interval[1] \
            else (prev_interval, interval)
        if min_interval[1] >= max_interval[0]:
            stack.pop()
            app = [min(min_interval[0], max_interval[0]), max(min_interval[1], max_interval[1])]
            stack.append(app)
        else:
            stack.append(interval)

        idx += 1

    return stack


if __name__ == '__main__':
    interval1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    interval2 = [[1, 4], [4, 5]]
    interval3 = [[0, 4], [1, 4]]
    interval4 = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    print(merge(interval4))
