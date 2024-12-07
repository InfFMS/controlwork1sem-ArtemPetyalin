def finder():
    nums = []

    def div_finder(arr, a):

        for i in range(2, a):

            if a % i == 0:
                arr.append(i)
        return len(arr)

    for i in range(174457, 174506):

        if div_finder([], i) == 2:
            nums.append(i)

    print(nums)
    return nums


finder()