def addDigits(num):
    num = str(num)
    
    while len(num) > 1:
        addition = 0
        for digit in num:
            addition += int(digit)
        num = str(addition)

    return int(num)
    
print(addDigits(num=39)) 