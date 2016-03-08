__author__ = 'CamiloDiaz_DavidDelgado_IvanClaro'

from archivar import Archivo
from ClassSeno import Seno
from ClassCuadrada import Cuadrada
from ClassTriangular import Triangular
from ClassSierra import Sierra
import pyaudio


def main():
    menu = input("Que tipo de onda desea generar?: 1) Onda Seno 2) Onda Cuadrada 3) Onda Tringular 4) Onda de Sierra ")


    if menu ==  1:

        frecuencia = input("Ingrese la frecuencia: ")
        sampleo = input("Ingrese la frecuencia de muestreo: ")
        tiempo = input("Ingrese el tiempo de audio en segundos: ")
        bits = input ("Ingrese el numero de bits: ")
        nombre = raw_input("Ingrese el nombre que tendra el archivo: ")

        wave = Seno(frecuencia, sampleo, tiempo, bits, nombre)
        datos = wave.generar()


        archivo = Archivo(frecuencia, sampleo, tiempo, bits, nombre)
        archivo.archivar(datos)

    if menu == 2:

        frecuencia = input("Ingrese la frecuencia: ")
        sampleo = input("Ingrese la frecuencia de muestreo: ")
        tiempo = input("Ingrese el tiempo de audio en segundos: ")
        bits = input("Ingrese el numero de bits: ")
        nombre = raw_input("Ingrese el nombre que tendra el archivo: ")

        wave = Cuadrada(frecuencia, sampleo, tiempo, bits, nombre)
        datos = wave.generar()


        archivo = Archivo(frecuencia, sampleo, tiempo, bits, nombre)
        archivo.archivar(datos)

    if menu == 3:
        frecuencia = input("Ingrese la frecuencia: ")
        sampleo = input("Ingrese la frecuencia de muestreo: ")
        tiempo = input("Ingrese el tiempo de audio en segundos: ")
        bits = input("Ingrese el numero de bits: ")
        nombre = raw_input("Ingrese el nombre que tendra el archivo: ")

        wave = Triangular(frecuencia, sampleo, tiempo, bits, nombre)
        datos = wave.generar()


        archivo = Archivo(frecuencia, sampleo, tiempo, bits, nombre)
        archivo.archivar(datos)

    if menu == 4:
        frecuencia = input("Ingrese la frecuencia: ")
        sampleo = input("Ingrese la frecuencia de muestreo: ")
        tiempo = input("Ingrese el tiempo de audio en segundos: ")
        bits = input("Ingrese el numero de bits: ")
        nombre = raw_input("Ingrese el nombre que tendra el archivo: ")

        wave = Sierra(frecuencia, sampleo, tiempo, bits, nombre)
        datos = wave.generar()


        archivo = Archivo(frecuencia, sampleo, tiempo, bits, nombre)
        archivo.archivar(datos)

if __name__ == "__main__":
    main()