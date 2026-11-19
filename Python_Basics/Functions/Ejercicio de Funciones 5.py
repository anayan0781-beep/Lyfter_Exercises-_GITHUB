def count_uppercase_lowercase(text):
    uppercase = 0
    lowercase = 0

    for character in text:
        if character.isupper():
            uppercase += 1
        elif character.islower():
            lowercase += 1

    print("Uppercase letters:", uppercase)
    print("Lowercase letters:", lowercase)


text = "Hello World"
count_uppercase_lowercase(text)