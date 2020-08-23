def check_if_palindrome(num):
    if(num/10 == 0):
         return True
    num = [int(x) for x in str(num)]
    count = 0
    while(True):
        if(count < (len(num)/2 + len(num)%2)):
            if(num[count] == num[(len(num)-1)-count]):
                count+=1
            else:
                return False
        else:
            return True

result = check_if_palindrome(1212)
result2 = check_if_palindrome(12121)
print("This is the result "+str(result))
print("This is the result "+str(result2))