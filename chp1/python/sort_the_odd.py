def sort_odd(array):
    odd_nums = []
    i = 0
    j = 0

    for num in array:
        if num % 2 != 0:
            odd_nums.append(num)
            j += 1
        else:
            pass
    
    odd_nums.sort()

    while i < len(array):
        if array[i] % 2 != 2:
            array[i] = odd_nums[j]
            j += 1
        else:
            pass
        i += 1
    return array