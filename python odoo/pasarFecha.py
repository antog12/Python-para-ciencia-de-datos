#pasar un fecha(año, mes y dia y tengo que decir si es valido)

def validarFecha(anyo, mes , dia):
    #con diccionario
    meses={"enero": 31, "febrero" :28, "marzo": 31, "abril": 30, "mayo":31, "junio":30,
     "julio":31, "agosto":31, "septiembre": 30,
      "octubre":31, "noviembre":30, "diciembre":31}
    
    #como un array
    mesesArray=[31,28,31,30,31,30,31,31,30,31,30,31]
    valida=False
    if(mes>0 and mes<13 and dia>0 and dia<=mesesArray[mes-1]):#menos 1 es pq empieza en 0
        valida=True
    return valida

print(validarFecha(2000,12,31))
