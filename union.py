for x in range(1, 4381):
    
    try:
        nombre =  str(x) +str('.xml')
        archivo = open(nombre, "r") 
        contenido = archivo.read()
            
        print contenido
        print x
    except Exception as e:
        pass