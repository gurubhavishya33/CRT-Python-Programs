a=int(input())
op=str(input())
b=int(input())
if op =="+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
elif op == "//":
    print(a//b)
elif op == "%":
    print(a%b)
elif op == "**":
    print(a**b)
else:
    print("Invalid Operator")    