f = open("input", 'r')
nums = f.readlines()

def bubble_sort(nums):
    nums = [int(i) for i in nums]
    n = len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]

    return nums



def median(nums):
    nums = [int(i) for i in nums]
    len_nums = len(nums)
    sorted_nums = bubble_sort(nums)
    if len_nums%2==0:
        median = (sorted_nums[int(len_nums/2)-1] + sorted_nums[int(len_nums/2)]) / 2
    else:
        median = sorted_nums[(len_nums//2)]

    return median

def quant():
    lower = []
    upper = []
    sorted_numbers = bubble_sort(nums)
    for i in (sorted_numbers):
        if(i<median(nums)):
            lower.append(i)
        else:
            upper.append(i)

    if len(sorted_numbers)%2!=0:
        upper.remove(median(nums))

    quant_25 = median(lower)
    quant_50 = median(nums)
    quant_75 = median(upper)

    return quant_25,quant_50,quant_75


if __name__=='__main__':
    print(quant())


