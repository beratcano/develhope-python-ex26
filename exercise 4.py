import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print("Number 1(", number1, ")'s absolute value is greater than Number 2(", number2, ")'s absolute value")
elif abs(number2) > abs(number1):
    print("Number 2(", number2, ")'s absolute value is greater than Number 1(", number2, ")'s absolute value")
else:
    print("Number 1(",number1,")'s absolute value equals to Number 2(", number2, ")'s absolute value")
