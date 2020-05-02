def sort():
    f = open("input", 'r')
    nums = f.readlines()
    nums = [int(i) for i in nums]
    mylist = []
    for i in range(len(nums)):
        min_n = min(nums)
        mylist.append(min_n)
        nums.remove(min_n)
    return mylist


if __name__=='__main__':
    print(sort())
