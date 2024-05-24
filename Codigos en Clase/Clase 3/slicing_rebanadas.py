# Slicing (cadenas y listas)
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])

nombre ='Maria de los angeles'
legajo ='45646'
edad = 55
telefono = "3854172879"

futbolistas = dict()

futbolistas = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}
