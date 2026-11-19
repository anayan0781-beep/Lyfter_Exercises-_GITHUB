def sort_words(text):
    words = text.split("-")
    words.sort()
    return "-".join(words)


text = "python-variable-funcion-computadora-monitor"

result = sort_words(text)

print(result)