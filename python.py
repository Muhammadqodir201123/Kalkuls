a = int(input("Enter number 1 "))
b = int(input("Enter second number "))
c = 0
d = input("+,-,*,/")

if d == "*":
    c = a * b
    print(c)

elif d == "/":
    c = a / b 
    print(c)

elif d == "+":
    c = a + b
    print(c)

elif d == "-":
    c = a - b
    print(c)

else:
    print("Learn math")