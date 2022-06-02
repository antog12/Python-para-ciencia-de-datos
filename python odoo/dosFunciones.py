# dos funciones para calular en la 1 la cantidad de segundos en un timepo dado en horas,minutos y segundos
# la segunda funcion lo mismo pero al revés.

from tkinter import N


def convertir (segundos):
    segundos= segundos % (24*3600)
    hora= segundos // 3600
    segundos %= 3600
    minutos= segundos // 60
    segundos % 60

    return "%d:%02d:%02d" % (hora, minutos, segundos) # "%d:%02d:%02d" es el formato que le damos al resultado

n=12345

print(convertir(n))


def pasarAsegundos(horas, minutos, segundos):
    return horas*3600 + minutos+60+ segundos

