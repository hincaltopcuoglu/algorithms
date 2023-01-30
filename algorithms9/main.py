## find all product of numbers between 1 to 11

for i in range(1,11):
    if i==1:
        product = 1
    else:
        product = product * i
        i += 1
        if i == 11:
            print(product,i)