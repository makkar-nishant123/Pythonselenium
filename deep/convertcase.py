string = str(input("Enter String: "))


def converstring(word):
    newstring = ""  # type: str
    for i in range(0, len(word)):
        char = word[i]
        if char.islower() == False:
            char = char.lower()
            newstring += char
        else:
            char = char.upper()
            newstring += char
    print (newstring)


converstring(string)
