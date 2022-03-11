#!/usr/bin/env python
import datetime # Importo las funciones de datetime para saber que anio es hoy
print ("Este programa le permite calcular los impuestos de un auto.")

#Consulto el anio en el momento que se use el programa
#Voy a tomar el dia de hoy desde la libreria datetime importada arriba
hoy = datetime.datetime.now() # en la variable hoy se guardara la fecha de hoy completar
anio_actual = hoy.year # de la variable hoy que contiene la fecha completa del dia de hoy saco unicamente el anio

# voy a tomar el valor del anio y verificar que sea un numero, pero esta vez no voy hacer ninguna funcion. Lo voy hacer directamente a medida que ingresen los datos
while True:
    anio = input ("Ingrese el anio de su auto: ")
    try:
        anio = int(anio)
        if 1886 <= int(anio) <= anio_actual: #Verifico que el anio ingresado del auto no sea mayor al actual y tampoco que sea demasiado antiguo. Recordemos que el primer auto se invento en 1886
            break
        else:
            print ("Ingrese un anio correcto")
    except:
        print ("Ingrese un anio correcto")

while True:
    tipo = input("Ingrese de que tipo es el auto, P: particulares, T: taxi, R: Remis : ")
    if tipo == "P" or tipo == "T" or tipo == "R": #Verifico que sea correcto el ingreso del usuario
        break
    else:
        print ("Ingrese correctamente el tipo de vehiculo")


#Calculo la antiguedad del auto
antiguedad = anio_actual - anio

#Calculo de impuestos
costo_impuesto = 0
if tipo == "P" or tipo == "T": #Consulto que tipo de vehiculo es. En caso de no ser P o T no ingresa de este if y ya se que es un Remis
    if antiguedad < 10: #Si su antiguedad es menor a 10 anios ingresa en esta if, de lo contrario salta directamente al elif
        if tipo == "P": # Si ingresa aca se que es menor su antiguedad es menor a 10 anios y ademas es particular
            costo_impuesto = 200
        else: #Si no ingreso en el if anterior, quiere decir que si o si es un taxi.
            costo_impuesto = 200 + 150
    elif 10 <= antiguedad <= 20: # Aca verifico que la aniguedad este entre 10 y 20 anios
        if tipo == "P":
            costo_impuesto = 150
        else:
            costo_impuesto = 150 + 150
    else: # Si se ejecuta este else, se que el vehiculo tiene mas de 20 anios
        print ("Vehiculo con antiguedad superior a 20 anios no paga impuestos")
        costo_impuesto = 0
else: # Si se ejecuta este else, se que es un Remis
    costo_impuesto = 100 * antiguedad

#Muestro en consola el resultado

print ("El costo de impuestos para su vehiculo es de: {}".format(costo_impuesto))
