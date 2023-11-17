def max_count(members):
    # Get the key with the maximum list length
    count = {}
    for m in members:
        cat = m.category
        if cat in count:
            count[cat] += 1
        else:
            count[cat] = 0

    return max(count, key=count.get)


def inner_category(members, category):
    return [m for m in members if m.category == category]


def outter_category(members, category):
    return [m for m in members if m.category != category]
