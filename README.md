# AudioProg
# Importar Librerias
import math
import matplotlib.pylab as plt

#Crear la Clase
class Audio:

    #Arreglo Para los Datos
    wavearray = []

    #Metodo Constructor
    def __init__(self,bits, smprate, frecuencia, duracion):
        self.bitrate = bits
        self.smprate = smprate
        self.frecuencia = frecuencia
        self.samples = duracion * smprate
        self.amplitud = (2**bits)/2
        self.pi = math.pi

    def Generar(self):

        for i in range (0, self.samples):
            muestra = self.amplitud*math.sin((2 * self.pi * self.frecuencia * i)/self.smprate)
            Audio.wavearray.append(muestra)

        return Audio.wavearray

    def Graficar(self,Arreglo):

        plt.plot(Arreglo, color="green", linewidth=1.0, linestyle="-")
        plt.show()
