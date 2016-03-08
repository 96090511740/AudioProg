__author__ = 'CamiloDiaz_DavidDelgado_IvanClaro'

import struct
import wave
import math

def main():

    menu = input("Que desea calcular?: 1)RMS 2)Valor Pico 3)Leq ")


    if menu ==  1:
        Archivo=wave.open("Audio.wav.wav","rb")
        tamano = Archivo.getnframes()
        bits = Archivo.getsampwidth()

        for	i in range(0,tamano):
            DatosArray = Archivo.readframes(1)
            Datos = struct.unpack('<H',DatosArray)
            sumatoria =	sumatoria	+	int(Datos[0])**2

            ValorRms = math.sqrt(sumatoria/tamano)
            ValorpicoRms = 20*math.log10(ValorRms/(2**bits))

        print (ValorRms)
        print (ValorpicoRms)


    if menu == 2:

        wavearray=[]
        Archivo=wave.open("Audio.wav.wav","rb")
        tamano = Archivo.getnframes()
        bits=Archivo.getsampwidth()
        return wavearray
        Valorpico=max(wavearray)
        ValorpicodBFS =	20*math.log10(float(Valorpico)/(2**bits))

        Valorpico.wavearray.append(ValorpicodBFS)

        print ValorpicodBFS

    if menu == 3:

        leq=[]

        Archivo	=	wave.open("Audio.wav.wav","rb")
        SAMPLINGRATE = Archivo.getframerate()
        T1 = 1.0/SAMPLINGRATE
        tamano=Archivo.getnframes()
        length = tamano / int(SAMPLINGRATE)
        bits=Archivo.getsampwidth()

        for	i	in	range(0,	tamano):
            DatosArray	=	Archivo.readframes(1)

            Datos	=	struct.unpack("<h",	DatosArray)
            sumatoria	= sumatoria+((int(Datos[0])**2)*T1)

        leq.append(20*math.log10((1/length)*(sumatoria)/2**bits))

        print leq


if __name__ == '__main__':
    main()