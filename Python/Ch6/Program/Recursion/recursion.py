"""
Recursion

    When a function calls itself again and again repeatedly, it's calls recursion

"""

# print n to 1 backwards

def print_backward(n):
    if(n == 0):
        return
    print(n)
    print_backward(n-1)

print_backward(100)