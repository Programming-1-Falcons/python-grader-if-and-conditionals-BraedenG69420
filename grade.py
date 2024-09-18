grade = int(input("type your percent:"))
if 0 <= grade <= 50:
    print("You got F")
elif 51 <= grade <= 60:
    print("You got D")
elif 61 <= grade <= 77:
    print("You got C")
elif 76 <= grade <= 88:
    print("You got B")
elif 89 <= grade <= 100:
    print("You got A")