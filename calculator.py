def add (a, b):
    return (a + b)
def sub (a, b):
    return (a - b)
def mult (a, b):
    return (a*b)
def div (a, b):
    return (a/b)
try: 
    print('select operation')
    print('1.add')
    print('2.subtract')
    print('3.multiply')
    print('4.divide')
    choice = int(input('enter your choice:'))
    num1 = float(input('enter 1st number:'))
    num2 = float(input('enter 2nd number:'))
    if choice == 1:
        print('addition is', add(num1, num2))
    elif choice == 2:
        print('subraction is', sub(num1, num2))
    elif choice == 3:
        print('multiplication is', mult(num1, num2))
   

    elif choice == 4:
        try:
            print('division is', div(num1, num2))
        except ZeroDivisionError:
            print('cant divide by 0')
    else:
        print('invalid option')
except ValueError:
    print('please enter valid numbers')
except ZeroDivisionError:
    print('cant divide by 0')


