def swap_case(s):
    output=''
    for char in s:
        print(char)
        if (char.isupper()==True):
            output=output+(char.lower())
        elif (char.islower()==True):
            output=output+(char.upper())
        else:
            output+=char
    return output
s=str(input("enter str:"))
print(swap_case(s))
