
with open('lib.txt','r') as f:
    linea = f.readline()
    print(linea)
    f.seek(10)
    linea = f.readline()
    print(linea)
