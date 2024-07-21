file = open("example.txt", "w")
file.write("This is an example.")
file = open("example.txt", "r")
content = file.read()
print(content)

file.close()