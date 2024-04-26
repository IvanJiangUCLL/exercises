def split_in_two(ns):
    half = len(ns) // 2
    left = ns[:half]
    right = ns[half:]
    return (left, right)


def merge_sorted(left, right):
    ns = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ns.append(left[i])
            i += 1
        else:
            ns.append(right[j])
            j += 1
    ns.extend(left[i:])
    ns.extend(right[j:])
    return ns


def merge_sort(ns):
    if len(ns) <= 1:
        return ns
    left, right = split_in_two(ns)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge_sorted(sorted_left, sorted_right)
