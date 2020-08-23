def count_digits(num):
    if isinstance(num,float):
        num = int(num)
    if num is 0:
        return 0
    return 1 + count_digits(num/10)


print("number of digits is "+str(count_digits(14505.5)))