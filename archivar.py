__author__ = 'CamiloDiaz_DavidDelgado_IvanClaro'

import wave
import struct


class Archivo:
    def __init__(self, frecuencia, sampleo, tiempo, bits, nombre):

        self.frecuency = frecuencia
        self.sampler = sampleo
        self.time = tiempo
        self.Bits = bits
        self.tamano =sampleo * tiempo
        self.nombre = nombre

    def archivar(self, datos):
        output = wave.open(self.nombre, 'w')
        Set_Bits = self.Bits/8
        output.setparams((1, Set_Bits, self.frecuency, 0, 'NONE', 'not compressed'))


        values = []
        for i in range(0, len(datos)):

                packed_value = struct.pack('<h', datos[i])

                values.append(packed_value)


        value_str = ''.join(values)
        output.writeframes(value_str)
        output.close()

