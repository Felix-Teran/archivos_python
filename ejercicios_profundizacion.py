#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.4"

import csv


def ej1():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 2

    '''
    Realizar un programa que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    with open ('propiedades.csv') as csvfile:
        alquileres = list(csv.DictReader(csvfile))

    alquiler_pesos = 0
    valor_alquileres = []
    max_alquiler = []
    min_alquiler = []
    for i in range(len(alquileres)):
        columnas = alquileres[i]
        for k,v in columnas.items():
            if (k == "ambientes") and (v == "2"):
                for k,v in columnas.items():
                    if (k == 'moneda') and (v == 'ARS'):
                        alquiler_pesos += 1
                        for k,v in columnas.items():
                            if (k == 'precio'):
                                valor_alquileres.append(float(v))
                                max_alquiler.append(float(v))
                                min_alquiler.append(float(v))

    prom_alquiler = sum(valor_alquileres) / alquiler_pesos
    print("La cantidad de alquileres en pesos son:", alquiler_pesos)
    print("El promedio de valores de alquileres es: {0:.2f}".format(prom_alquiler))
    print("El alquiler maximo es de:", max(max_alquiler))
    print("El alquiler minimo es de:", min(min_alquiler))

def ej2():
    print('Proyecto final!')
    '''
    El manejo de archivos seguramente sea una herramienta que
    utilizará en el proyecto de este curso.
    Para la clase que viene traiga pensando la idea de proyecto
    para discutir en clase y publique su idea en el campus
    para que los docentes puedan mandurar la idea antes de llegada
    la clase.
    '''


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    # ej2()
