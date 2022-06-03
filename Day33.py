#Example of IF-ELSE nested conditionals.
#Note that the input must be converted to INTEGER type, otherwise comparisons won't work properly.

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num1 >= num2:
    if num1 == num2:
        print(num1, 'and', num2, 'are equal')
    else:
        print(num1, 'is greater than', num2)
else:
    print(num1, 'is smaller than', num2)