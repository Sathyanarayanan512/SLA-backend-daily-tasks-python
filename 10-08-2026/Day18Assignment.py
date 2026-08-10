# no parameter, no return type
def odd_or_even_function():
    num=6
    if num%2==0:
        print("Even")
    else:
        print("Odd")
odd_or_even_function()

# with parameter, no return type
def odd_or_even_function(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
odd_or_even_function(7)

# with parameter, with return type
def odd_or_even_function(num):
    if num%2==0:
        return "Even"
    return "Odd"
d=odd_or_even_function(8)
print(d)

# no parameter, with return type
def odd_or_even_function():
    num=9
    if num%2==0:
        return "Even"
    return "Odd"
d=odd_or_even_function()
print(d)
