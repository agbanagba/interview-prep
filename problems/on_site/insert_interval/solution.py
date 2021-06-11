# This solution is an O(nlogn) runtime with O(n) space complexity because of the fact
# that we are sorting
def insert_interval(intervals, new_interval):
    intervals.append(new_interval)
    # this is only done when the intervals are not sorted according to their start times
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


def insert_interval_efficient(intervals, new_interval):
    # Let's try getting an O(n) space and time solution

    # Since we know the intervals are already sorted we can do a merge and while doing that merge,
    # we find the perfect spot to compare our new interval

    i, merged = 0, []
    processed, halt = False, False
    while i < len(intervals):

        if intervals[i][0] > new_interval[0] and not processed:
            processed, halt = True, True
            interval = new_interval
        else:
            interval = intervals[i]

        # at some point we pause the increment of i when we find the new_interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

        if halt:
            halt = False
        else:
            i += 1

    # In this case, then new_interval is outside > intervals[-1][0]
    # so all we need to is merge it with
    if not processed:
        if not merged or merged[-1][1] < new_interval[0]:
            merged.append(new_interval)
        else:
            merged[-1][1] = max(merged[-1][1], new_interval[1])
    return merged


if __name__ == '__main__':
    int_vals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_int_vals = [4, 8]

    int_vals2 = [[1, 3], [6, 9]]
    new_int_vals2 = [2, 5]

    int_vals3 = []
    new_int_vals3 = [5, 7]

    int_vals4 = [[1, 5]]
    new_int_vals4 = [2, 7]
    print(insert_interval_efficient(int_vals4, new_int_vals4))
