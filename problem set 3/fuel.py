try:
    fraction = input("Fraction: ")
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)

except ValueError:
    print("At least one of the values is not an integer")

except ZeroDivisionError:
    print("Division by zero")

else:
    result = ( x / y ) * 100

    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(result)