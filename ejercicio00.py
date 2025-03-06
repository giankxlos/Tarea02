palabra = input("Escribe una palabra: ")

encontrada = False
for letra in palabra: 
    if letra == "H": 
        encontrada = True
        break
   
if encontrada: 
    print("SI ENCUENTRA, LA LETRA FUE ENCONTRADA")
else:
    print("NO ENCUENTRA, LA LETRA NO EXISTE EN LA PALABRA")
        

