# def addDigits(num):
#     num = str(num)
#     addition = 0
#     if len(num) > 1:
#         for digit in num:
#             addition += int(digit)
#             if len(str(addition)) > 1:
#                 addition += int(digit)
#             else:
#                 return addition
#         return addition
#     else:
#         return int(num)

 # Output: 1


def addDigits(num):
    num = str(num)
    
    while len(num) > 1:
        addition = 0
        for digit in num:
            addition += int(digit)
        num = str(addition)

    return int(num)
    
print(addDigits(num=39)) 

# num=13
# sum = 0
# num1=str(num)
# for i in range(len(num1)):
      
#       sum+=int(num1[i])
# print(sum) 