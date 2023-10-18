num1 = int(input())
num2 = int(input())
operator = input("Enter the operator number in the order of occurance; +, -, *, /: ")

if (operator == '1'):
    print(num1 + num2)
elif (operator == '2'):
    print(num1 - num2)
elif (operator == '3'):
    print(num1 * num2)
elif (operator == '4'):
    print(num1 / num2)
else:
    print("Input number from 1-4")
