
with open('messi.txt', 'w') as file:
    file.write("Messi goat")

print("success")

print("\nReading")
with open('messi.txt', 'r') as file:
    content = file.read()
    print(content)
