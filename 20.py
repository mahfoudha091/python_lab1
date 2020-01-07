""" 
    Write a Python program to get a string which is n (non-negative integer) 
    copies of a given string
""" 
def larger_string(str,n):
    result = ""
    for i in range(n):
        result = result + str 
    return result
    
#  or 
# def larger_string(str,n):
#     return str * n


print(larger_string("abc",3))
print(larger_string("test",5))

