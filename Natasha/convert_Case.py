def swapcase(char):
    if (char.islower()):
        char = char.upper()
    else:
        char = char.lower()
    return char
str = str(input())
for index in range(0,len(str)):
    print (swapcase(str[index]),end="")
