def swap_max_and_min(lst):
    if len(lst) != len(set(lst)):
        raise ValueError('List contain the same element')
    else:
        mx = max(lst)
        mn = min(lst)
        lst[lst.index(max(lst))] = mn
        lst[lst.index(min(lst))] = mx
    return lst