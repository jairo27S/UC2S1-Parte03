
import os
import sys

def leer_archivo(archivo):
    archivo = open (archivo, "rt",encoding="utf8")
    leer_archivo = archivo.read()
    leer_archivo = leer_archivo.split("\n")
    return leer_archivo

ar_usuario = leer_archivo("login.txt")
ar_clave = leer_archivo("clave.txt")

cont = 0

while cont !=2:
    ususario = input("ingresar usuario :  ")
    clave = input("ingresar clave:  ")

    for usuarioItem in ar_usuario:
            if ususario == usuarioItem:
                for clave_Item in ar_clave:
                    if clave == clave_Item:
                        print("\t Datos ingresados correctamente\n")
                        print("Datos personales \n1.Listar persona\n2.Agregar persona\n2.Salir")
                        cont = 2
                    else:
                        print("\t Datos incorrectos\n")
                        cont +=1
            else:
                print("\t Datos incorrectos\n")
                cont +=1

opcion = input("\nSeleccione una opcion: ")
if opcion =='1':
    print("Listar\n")
    archivo_1 = open("nombre.txt")
    archivo_2 = open("apellido.txt")
    archivo_3 = open("dni.txt")

    a = archivo_1.readlines()
    b = archivo_2.readlines()
    c = archivo_3.readlines()

    d = zip(a,b,c)

    for linea in d:
        print(linea)

elif opcion == "2":
    archivo_1 = open("nombre.txt", "a")
    archivo_2 = open("apellido.txt", "a")
    archivo_3 = open("dni.txt", "a")

    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = input("Ingrese el dni: ")

    archivo_1.write("\n"+nombre)
    archivo_2.write("\n"+apellido)
    archivo_3.write("\n"+dni)

    archivo_1.close()
    archivo_2.close()
    archivo_3.close()
else:
        exit()

