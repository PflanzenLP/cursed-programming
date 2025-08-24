text = "default text"
try:
    with open("nonexistent_file.txt") as file:
        text = file.read()
except:
    pass

print(text)