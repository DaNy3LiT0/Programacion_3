chunk_size = 30
with open('lib.txt','r') as f:
    chunk = f.read(chunk_size)
    print(chunk)
    posicion = f.tell()
    print(f"Actual posición del puntero de archivo: {posicion}")