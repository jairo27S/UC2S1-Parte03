
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