first_num = float(input('Enter first num: '))
second_num = float(input('Enter second num: '))
operator = input('Enter operator: ')

def calculation(operator):
    match operator:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num
        case '/':
            return first_num / second_num

try:
    result = calculation(operator)
    print(result)
except ZeroDivisionError:
    print(f"Can't divide by zero.")