def main():
    expression = input("Expression: ").strip().split(" ")
    x = float(expression[0])
    y = expression[1]
    z = float(expression[2])

    result = math(x, y, z)
    print(result)

def math(x, y, z):
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z
        case _:
            print("Error")

main()