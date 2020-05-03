def average():
    f = open("input", 'r')
    nums = f.readlines()
    nums = [int(i) for i in nums]
    g = nums[0]
    for i in range(1,len(nums)):
        g += nums[i]

    avrg = g/len(nums)

    return avrg

if __name__=='__main__':
    print(average())

