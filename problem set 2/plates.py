def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    found_digit = False
    for i, c in enumerate(s):
        if not c.isalnum():
            return False
        
        if c.isdigit():
            if c == '0' and (i == 2 or (i > 2 and not s[i-1].isdigit())):
                return False
            found_digit = True

        elif found_digit:
            return False

    return True

main()
