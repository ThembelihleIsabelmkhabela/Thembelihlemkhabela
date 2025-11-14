num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("choose an oparator: = +, -, *, /")
oparator= input("Enter oparator:")
if oparator == '+':
    result = num1 + num2
elif oparator =='-':
    result = num1 - num2
elif oparator =='*':
    result = num1 * num2
elif oparator =='/':
    result = num1 / num2
    if num2 !=0:
        result = num1 / num2
print("result:", result)


