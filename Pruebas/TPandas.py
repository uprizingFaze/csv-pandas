import pandas as pd

numeros = pd.Series([1,2,3,4,5,6])
print (numeros)
print ("---------------------------^^^---------------------------")

palabras = pd.Series(["Hola", "Que tal", "Comida"])
print (palabras)
print ("---------------------------^^^---------------------------")

materias = pd.Series({"Calculo":13, "Quimica":15})
print (materias)
print ("---------------------------^^^---------------------------")

print ("Tamaño:",numeros.size)
print ("---------------------------^^^---------------------------")

print ("Nombres filas:", materias.index)
print ("---------------------------^^^---------------------------")

print ("Tipo de datos:", palabras.dtype)
print ("---------------------------^^^---------------------------")

print ("Buscar objeto:")
print (palabras[2:3])
print ("---------------------------^^^---------------------------")

