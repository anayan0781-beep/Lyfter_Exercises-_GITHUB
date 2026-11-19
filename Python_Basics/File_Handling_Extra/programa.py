with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

text = " ".join(line.strip() for line in lines)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)