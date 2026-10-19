

# Merge all three arrays into a single array and remove any duplicates.
def merge_arrays(arr1, arr2, arr3):

    merged_set = sorted(set(arr1).union(arr2, arr3))
    return merged_set
