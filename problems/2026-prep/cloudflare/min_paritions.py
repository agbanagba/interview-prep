def determineMinPartitionsRequired(partitions: list[int], partitionsUsed: list[int]) -> int:

    total_data = sum(partitionsUsed)
    if total_data == 0:
        return 0
    
    partitions.sort(reverse=True)
    
    capacity_used = 0
    needed = 0
    for capacity in partitions:
        capacity_used += capacity
        needed += 1

        if capacity_used >= total_data:
            break

    return needed