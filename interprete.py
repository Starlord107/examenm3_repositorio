import biblioteca as c

def comandos_basicos(comandos):
    partes = comandos.split('-')
    if partes[0].lower() == "addllibre".lower() and len(partes) == 6:
        codi = partes[1]
        titol = partes[2]
        autor = partes[3]
        genere = partes[4]
        numerodepaginas = partes[5]
       # codi, titol, autor, genere, numerodepaginas = partes[1:]

        c.add_llibre(codi, titol, autor, genere, numerodepaginas)
    elif partes[0].lower()=="listLlibres".lower():

        c.list_llibres()

    elif partes[0].lower()=="startPrestec".lower()and len(partes)==4:

        codi=partes[1]
        nombre_alumnes=partes[2]
        data_prestec=partes[3]

        c.startPrestec(codi,nombre_alumnes,data_prestec)

    elif partes[0].lower()=="endPrestec".lower()and len (partes)==3:
        codi=partes[1]
        dataretorn=partes[2]
        c.endPrestec(codi,dataretorn)

    elif partes[0].lower()=="listPrestecs".lower():
        c.listPrestecs()

    elif partes[0].lower()=="listGenere".lower() and len(partes)==2:
        genere=partes[1]
        c.listGenere(genere)

    elif partes[0].lower()=="maxLlibre".lower():
        c.maxLlibre()

    elif partes[0].lower()=="stats".lower():
        c.stats()

    elif partes[0].lower()=="info".lower() and len(partes)==2:
        nombre_alumno=partes[1].lower()
        c.info(nombre_alumno)
    else:
        print("Error: nº d'arguments incorrecte")

