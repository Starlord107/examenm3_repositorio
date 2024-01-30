import biblioteca as c




def longitud_valida(comandos,longitud):
    partes=comandos.split("-")
    return len(partes)==longitud
def comandos_basicos(comandos):
    partes = comandos.split('-')
    accion=partes[0].lower()

    if accion == "addllibre".lower() and longitud_valida(comandos,6):

        codi = partes[1]
        titol = partes[2]
        autor = partes[3]
        genere = partes[4]
        numerodepaginas = partes[5]
       # codi, titol, autor, genere, numerodepaginas = partes[1:]

        c.add_llibre(codi, titol, autor, genere, numerodepaginas)





    elif accion=="listLlibres".lower():

        c.list_llibres()

    elif accion=="startPrestec".lower()and longitud_valida(comandos,4):

        codi=partes[1]
        nombre_alumnes=partes[2]
        data_prestec=partes[3]

        c.startPrestec(codi,nombre_alumnes,data_prestec)


    elif accion=="endPrestec".lower()and longitud_valida(comandos,3):
        codi=partes[1]
        dataretorn=partes[2]
        c.endPrestec(codi,dataretorn)









    elif accion=="listPrestecs".lower():
        c.listPrestecs()

    elif accion=="listGenere".lower() and longitud_valida(comandos,2):
        genere=partes[1]
        c.listGenere(genere)

    elif accion=="maxLlibre".lower():
        c.maxLlibre()

    elif accion=="stats".lower():
        c.stats()

    elif accion=="info".lower() and longitud_valida(comandos,2):
        nombre_alumno=partes[1].lower()
        c.info(nombre_alumno)
    else:
        print("Error: nº d'arguments incorrecte")


