# find median of given array

import numpy as np

def median():
    f = open("input", 'r')
    nums = f.readlines()
    nums = [int(i) for i in nums]
    len_nums = len(nums)
    sorted_nums = np.sort(nums)
    print(sorted_nums)
    if len_nums%2==0:
        median = (sorted_nums[int(len_nums/2)-1] + sorted_nums[int(len_nums/2)]) / 2
    else:
        median = sorted_nums[(len_nums//2)]

    return(median)

if __name__=='__main__':
    print(median())
