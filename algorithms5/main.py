def minx(nums):
    number = nums[0]
    for i in range(1,len(nums)):
        if nums[i]<=number:
            number = nums[i]
        else:
            number

    return number

def sort():
    f = open("input", 'r')
    nums = f.readlines()
    nums = [int(i) for i in nums]
    mylist = []
    for i in range(len(nums)):
        min_n = minx(nums)
        mylist.append(min_n)
        nums.remove(min_n)
    return mylist

if __name__=='__main__':
    print(sort())
