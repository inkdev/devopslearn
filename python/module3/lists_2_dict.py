def lists_2_dict(lst1, lst2):
    joindict = {key: val for (key, val) in zip(lst1, lst2)}
    return joindict
