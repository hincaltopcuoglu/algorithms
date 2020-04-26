# read the text file and return smallest integer which not in your text
# for example :
# if your list is [1,2,3] then the output should be 4
# if your list is [1,2,3,4,5,10] then the output should be 6

def solution():
    f = open("text", 'r')
    nums = f.readlines()
    nums = [int(i) for i in nums]
    a=[]
    for i in range(100):
        if (i < max(nums)) & (i > min(nums)) & (i not in nums):
            a.append(i)

    if len(a)==0:
        a.append(max(nums) + 1)

    return(min(a))



if __name__ == '__main__':
    print(solution())
