
#algorithm that finds the difference between the value in the hundreds digit of an entered 4-digit integer 
# and the remainder obtained by dividing by 3 with the value in the ones digit of the same number
input = input("Enter your value: ")

def dividends(input):
    val = input
    val = int(val)
    thou = int(val / 1000) * 1000
    hundr = val - thou
    value = int(hundr / 100) * 100
    s = value - int(value / 3) * 3
    ones = val - int(val / 10) * 10
    diff = s - ones
    return(print(diff))


if __name__ == "__main__":
    dividends(input)