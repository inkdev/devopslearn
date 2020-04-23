def dict_swap(dic):
    sw_dict = {}
    for key, val in iter(dic.items()):
        sw_dict[val] = key
    return sw_dict
