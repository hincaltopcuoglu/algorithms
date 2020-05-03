def minx():
    f = open("input", 'r')
    nums = f.readlines()
    nums = [int(i) for i in nums]
    number = nums[0]
    for i in range(1,len(nums)):
        if nums[i]<=number:
            number = nums[i]
        else:
            number

    return number

if __name__=='__main__':
    print(minx())

