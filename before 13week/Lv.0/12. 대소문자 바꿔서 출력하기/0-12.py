str = input()
for char in str:
    if char.islower():
        print(char.upper(), end="")
    elif char.isupper():
        print(char.lower(), end="")

