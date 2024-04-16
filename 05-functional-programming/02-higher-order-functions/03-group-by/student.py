def group_by(xs, key_function):
    groups = {}
    for x in xs:
        key = key_function(x)
        if key not in groups:
            groups[key] = []
        groups[key].append(x)
    return groups
