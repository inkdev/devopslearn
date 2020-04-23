def multiple_in_range(start, finish):
    result = [num for num in range(start, finish + 1) if num % 7 == 0 and num % 5 != 0]
    return result
