def bubble_sort():
    f = open("input", 'r')
    nums = f.readlines()
    nums = [int(i) for i in nums]
    n = len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]

    return nums

if __name__=='__main__':
    print(bubble_sort())



