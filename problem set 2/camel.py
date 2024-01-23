camel = input("Type here the variable name in camel case: ")
snake = ""

for i in camel:
    if(i.isupper()):
        snake += "_" + i.lower()
    else:
        snake += i

print(snake)