string = input("Input: ")
newstring = ""
    
for i in string:
    if i not in "aeiouAEIOU":
        newstring = newstring + i
    string = newstring    

print(newstring)