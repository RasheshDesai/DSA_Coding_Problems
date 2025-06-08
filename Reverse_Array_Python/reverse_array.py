

# def reverse_array(arr):
    
#    k = arr[::-1]  
#    print("Reversed array:", k)
#    return k

# reverse_array("My Name is Rashesh Desai")


def reverse_array(s):
    l = list(s)
    l.reverse()
    return "".join(l)

print(reverse_array("My Name is Rashesh Desai"))    
