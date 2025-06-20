def addTwoNumbers(l1, l2):
    new_list = []
    i=0
    carry = 0
    while i < len(l1) and i < len(l2) or carry:
        num1 = l1[i] if i < len(l1) else 0
        num2 = l2[i] if i < len(l2) else 0
        total = num1 + num2 + carry
        carry = total // 10
        new_list.append(total % 10)
        i+=1
    return new_list

print(addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
