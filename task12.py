def M(N):
    divs = []

    for i in range(2, N):

        if N % i == 0:
            divs.append(i)
            print(i)

    if len(divs) > 5:
        return divs[-5]

    else:
        return 0


i = 300000001
nums = []
while len(nums) < 5:

    if M(i) > 0:
        nums.append(i)

    i += 1
    print(i, '- num')
    print(nums)

print(nums)