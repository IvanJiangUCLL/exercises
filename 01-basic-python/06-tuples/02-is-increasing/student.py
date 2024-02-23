# Write your code here
def is_increasing(ns):
    ms = ns[1:]  # Drop the first element of ns
    pairs = zip(ns, ms)  # Pair up the elements of ns and ms
    for (x, y) in pairs:
        if x > y:
            return False
    return True
