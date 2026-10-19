
# We do the naive thing which is remove an index, pair the rest
# find the cost and compare to current min
def minimizePairingCostNaive(arr: list[int]) -> int:
    min_cost = float('inf')

    best_oidx = -1
    for i in range(len(arr)):
        remaining = arr[:i] + arr[i + 1:]
        remaining.sort()
        current_cost = 0

        for j in range(0, len(remaining), 2):
            current_cost += remaining[j + 1] - remaining[j]

        if current_cost < min_cost:
            min_cost = current_cost
            best_oidx = i

    return best_oidx


# We could instead have an O(N) solution where we slide out a value of current idx
# from current cost as we traverse the array. 
def minimizePairingCost(arr: list[int]) -> int:
    if len(arr) == 1:
        return 0

    sorted_arr = sorted([(val, i) for i, val in enumerate(arr)])
    current_cost = 0

    for i in range(1, len(arr), 2):
        current_cost += sorted_arr[i + 1][0] - sorted_arr[i][0]

    min_cost = current_cost
    best_oidx = sorted_arr[0][1]

    for i in range(len(arr) - 1):
        diff = sorted_arr[i + 1][0] - sorted_arr[i][0]

        if i % 2 == 0:
            current_cost += diff
        else:
            current_cost -= diff

        if current_cost < min_cost:
            min_cost = current_cost
            best_oidx = sorted_arr[i + 1][1]
        elif current_cost == min_cost:
            best_oidx = min(best_oidx, sorted_arr[i + 1][1])

    return best_oidx