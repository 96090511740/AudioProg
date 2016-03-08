__author__ = 'CamiloDiaz_DavidDelgado_IvanClaro'

import math
from archivar import Archivo
import matplotlib.pylab as plt
import struct
import wave

class Triangular:

        wavearray=[]
        def __init__(self,frecuencia,sampleo,tiempo,bits, nombre):
            self.frecuency = frecuencia
            self.sampler = sampleo
            self.time = tiempo
            self.Bits = bits
            self.tamano =sampleo * tiempo
            self.nombre = nombre

        def generar(self):
            m=2*self.frecuency*(2**self.Bits)
            d=0
            g=((2**self.Bits)/2)

            for i in range(0, self.tamano):


                wave = ((2**self.Bits)/2)*math.sin((2*math.pi*self.frecuency*i)/self.sampler)
                d=d+m
                Triangular.wavearray.append(wave)
                if (abs(wave)==g):
                    m=-1*m

            return Triangular.wavearray

            Archivo=wave.open(self.nombre,"rb")
            tamano = Archivo.getnframes()

            for	i in range(0,tamano):
                DatosArray = Archivo.readframes(1)
                Datos = struct.unpack('<H',DatosArray)
                sumatoria =	sumatoria	+	int(Datos[0])**2

            ValorRms = math.sqrt(sumatoria/tamano)
            ValorpicoRms = 20*math.log10(ValorRms/(2**self.Bits))

            print (ValorRms)
            print (ValorpicoRms)

