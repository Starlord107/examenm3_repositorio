libros = {}
prestamos={}
fechas={}
incidencias={}
alumnos={}
incidencias_libros={}
import datetime as f
from datetime import  timedelta
from datetime import  date
def add_llibre(codi, titol, autor, genere, numerodepaginas):

    if codi in libros:
        print("Este libro ya esta registrado")
    else:
        if not numerodepaginas.isdigit or int(numerodepaginas) <=0:
            print("error no pueden haver paginas negaticas o con letras")
        else:
            libros[codi] = {
                "titol": titol,
                "autor": autor,
                "genere": genere,
                "numerodepaginas": int(numerodepaginas),
                "alquilado": False

            }
            print(f"el libro {titol} ha sido añadido")


def list_llibres():
    if not libros:
        print("No hay libros registrados")

    salida = ""  # Inicializamos la cadena de salida

    # Iterar sobre cada libro y agregar sus detalles al string de salida
    for codi, info in libros.items():
        alquilado = "ESTAT: en préstec" if info["alquilado"] else "ESTAT: disponible"
        salida += f"{codi} : {info['titol']} , {info['autor']} - {alquilado}\n"

    print(salida)


def startPrestec(codi,nombre_alumnes,data_prestec):
    if codi not in libros:
        print("este libro no existe en la biblioteca")

    else:
        if codi  in prestamos:
            print("Este libro ya esta registrado")



        else:



            datafinal=f.datetime.strptime(data_prestec,"%d/%m/%Y")

            prestamos[codi]={
                "alumno":nombre_alumnes,
                "data":datafinal,
                "alquilado":True,
                "incidencia":False
            }
            fechadevolucion=datafinal + timedelta(days=15)
            if prestamos[codi]["alquilado"] ==True:
                libros[codi]["alquilado"]=True
                if  libros[codi]["alquilado"]==True:
                    fechas[codi]={
                        "data_prestec":data_prestec,
                        "fechadevolucion": fechadevolucion


                    }
                    print (f"Préstec registrat. El llibre s’ha de retornar:{fechadevolucion} ")



def endPrestec(codi,dataretorn):
    if codi not in libros:
        print("error aquest llibre no esta registrat")


    elif codi in libros and libros[codi]["alquilado"]==False:
        print("aquest llibre no esta  llogat ")

    else:
        format_data="%d/%m/%Y"

        datafinal2=f.datetime.strptime(dataretorn,format_data)

        if prestamos[codi]["data"] > datafinal2:
                print("error no pot tenir una data inferior a la de prestec, no pots tornar un llibre abans de llogarlo")



        elif fechas[codi]["fechadevolucion"] < datafinal2:
                prestamos[codi]["incidencia"]=True
                prestamos[codi]["alquilado"]=False
                libros[codi]["alquilado"]=False
                fechas[codi]["data_incidencia"]=datafinal2

                print("El llibre s'ha retornat amb retard.Incidencia registrada\nEl llibre ha quedat disponible")

        else:
            print("Llibre retornat sense cap incidencia")
            prestamos[codi]["incidencia"] = False
            prestamos[codi]["alquilado"] = False
            libros[codi]["alquilado"] = False



def listPrestecs():
    if not prestamos:
        print("No hay ningún libro en préstamos")
    else:
        hoy = f.datetime.today()

        salida1 = ""

        # Iterar sobre prestamos
        for codi_prestamo, valor_prestamo in prestamos.items():
            # Verificar si el prestamo está en libros y fechas
            if codi_prestamo in libros and codi_prestamo in fechas:
                libro = libros[codi_prestamo]
                nombre = libro["titol"]
                nombre_alumno = valor_prestamo["alumno"]

                # Obtener fechas del prestamo y devolución
                fechainicio1 = fechas[codi_prestamo]["data_prestec"]
                fechafinal2 = fechas[codi_prestamo]["fechadevolucion"]

                # Determinar el estado del préstamo
                estado = ""

                if fechafinal2 < hoy:
                    estado = "Fora de termini"
                else:
                    estado = "en termini"

                salida1 += f"Libro: {nombre}, Alumno: {nombre_alumno}, Inicio: {fechainicio1}, Fecha fin: {fechafinal2} ({estado})\n"

        print(salida1)



def listGenere(genere):
    salida_genere=""
    if libros=={}:
        print("No ni ha llibres registrats")

    else:
        for codi_libro,valor_libro in libros.items():
            if genere==valor_libro["genere"]:
                nombre_libro=valor_libro["titol"]
                autor_libro=valor_libro["autor"]
                estado_libro=""
                if valor_libro["alquilado"]:
                    estado_libro="disponible"
                else:
                    estado_libro="Alquilado no disponible"

                salida_genere += f"{codi_libro}: {nombre_libro},{autor_libro}-Estado:{estado_libro}\n"
        print(salida_genere)

def maxLlibre ():
    if not  libros:
        print("no hi han llibres registrats")
    else:
        libro_maximo = ""
        nrpags = 0
        for clave,valor_libros in libros.items():
            if valor_libros["numerodepaginas"] > nrpags:
                nrpags = valor_libros["numerodepaginas"]
                titulodenombres = valor_libros["titol"]








    print(f"El llibre amb mes pagines de la biblioteca es :{titulodenombres} amb {nrpags}")



def stats():
    if not libros:
        print("no hi han llibres registrats")

    else:
        n_total=len(libros)


        n_total_incidencias=0
        for clave in prestamos:
            for values in prestamos[clave]:
                if values=="incidencias":
                    incidencias==True
        n_total_incidencias +=1
        n_total_paginas=0
        for clave in libros:
            for value in libros[clave]:

                if value == "numerodepaginas":
                    n_total_paginas += libros[clave]["numerodepaginas"]

            media=n_total_paginas/n_total
        print(f"Numero de llibres registrats : {n_total}\nNumero d'incidencies registrades:{n_total_incidencias}\nMitjana de pagines per llibre :{media}")



def info(alumno):
    tiene_prestamos = False
    tiene_incidencias = False
    salida_libro = ""
    salida_incidencia = ""
    nombre_alumno = alumno.lower()

    for codi, prestamo in prestamos.items():
        if nombre_alumno == prestamo["alumno"].lower():
            # Verificar si el libro sigue estando en préstamo
            if libros[codi]["alquilado"]:
                tiene_prestamos = True
                titol_alumno = libros[codi]["titol"]
                autor_alumno = libros[codi]["autor"]
                fechainici_alumno = fechas[codi]["data_prestec"]
                fechafinal_alumno = fechas[codi]["fechadevolucion"]
                salida_libro += f"Llibre: {codi} - {titol_alumno}, Autor: {autor_alumno}, Alumne: {nombre_alumno}, Data inici: {fechainici_alumno}, Data fi: {fechafinal_alumno}\n"

            # Verificar incidencias, incluso para libros ya devueltos
            if prestamos[codi]["incidencia"]:
                tiene_incidencias = True
                nombre_incidencia = libros[codi]["titol"]
                data_inici_incidencia=fechas[codi]["data_prestec"]
                data_fi_inici=fechas[codi]["fechadevolucion"]
                data_fora_de_termini = fechas[codi].get("data_incidencia", "No disponible")
                salida_incidencia += f"Incidencia - Llibre: {codi} - {nombre_incidencia}, , Alumne: {nombre_alumno}, Data inici: {data_inici_incidencia}, Data fi: {data_fi_inici}, Data fora de termini: {data_fora_de_termini}\n"

    if not tiene_prestamos and not tiene_incidencias:
        print("L'alumne indicat no te cap llibre en préstec ni incidències")
    else:
        if tiene_prestamos:
            print("Llibres en préstec:\n" + salida_libro)
        if tiene_incidencias:
            print("Incidències:\n" + salida_incidencia)
