def sort_words(text):
    words = text.split("-")
    words.sort()
    return "-".join(words)


text = "banana-apple-orange-grape"

result = sort_words(text)

print(result)