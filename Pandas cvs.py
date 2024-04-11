import pandas as pd
import re

def buscar_y_filtrar_datos(archivo_csv, columna, palabra_a_buscar, archivo_salida_csv):
    # Cargar datos desde el archivo CSV
    df = pd.read_csv(archivo_csv)

    # Escapar los caracteres especiales de la palabra a buscar
    palabra_a_buscar = re.escape(palabra_a_buscar)

    # Permitir búsqueda con coincidencias parciales
    palabra_a_buscar = palabra_a_buscar.replace(r'\ ', r'(\d+)?')

    # Buscar y filtrar datos
    resultado = df[df[columna].str.contains(palabra_a_buscar, case=False, regex=True)]

    # Guardar el resultado en otro archivo CSV
    resultado.to_csv(archivo_salida_csv, index=False)

def opcion_buscar_y_filtrar():
    # Ingresa el nombre del archivo CSV que deseas filtrar
    archivo_csv = input("Ingrese el nombre del archivo CSV que desea filtrar: ")

    # Ingresa el nombre de la columna donde deseas buscar
    columna_a_buscar = input("Ingrese el nombre de la columna que desea buscar: ")

    # Ingresa la palabra que deseas buscar en la columna
    palabra_a_buscar = input("Ingrese la parte de la palabra que desea buscar: ")

    # Ingresa el nombre del archivo CSV de salida
    archivo_salida_csv = input("Ingrese el nombre del archivo CSV de salida: ")

    buscar_y_filtrar_datos(archivo_csv, columna_a_buscar, palabra_a_buscar, archivo_salida_csv)
    print("Búsqueda y filtrado completados. Resultados guardados en", archivo_salida_csv)

def opcion_excel_csv():
    # Lee el archivo de Excel
    archivo_excel = input("Ingrese el nombre del archivo excel: ")  # Reemplaza esto con el nombre de tu archivo Excel
    df = pd.read_excel(archivo_excel)

    # Guarda los datos en un archivo CSV
    archivo_csv = input("Ingrese el nombre de su nuevo archivo .csv: ") # Reemplaza esto con el nombre que deseas para el archivo CSV
    df.to_csv(archivo_csv, index=False)


def exportar_columnas_personalizado():

    archivo_csv = input("Ingrese el nombre del archivo csv: ")
    archivo_salida_csv = input("Ingrese el nombre del archivo de salida: ")
    # Cargar datos desde el archivo CSV
    df = pd.read_csv(archivo_csv)

    # Obtener la lista de columnas del DataFrame
    columnas_disponibles = df.columns.tolist()

    # Solicitar al usuario la cantidad de columnas a exportar
    num_columnas_exportar = int(input(f"Ingrese la cantidad de columnas que desea exportar (1-{len(columnas_disponibles)}): "))

    if num_columnas_exportar < 1 or num_columnas_exportar > len(columnas_disponibles):
        print("Cantidad inválida de columnas.")
        return

    # Solicitar al usuario los nombres de las columnas a exportar
    columnas_exportar = []
    for i in range(num_columnas_exportar):
        nombre_columna = input(f"Ingrese el nombre de la columna {i + 1}: ")
        if nombre_columna not in columnas_disponibles:
            print("Nombre de columna inválido.")
            return
        columnas_exportar.append(nombre_columna)

    # Extraer solo las columnas seleccionadas y guardar en otro archivo CSV
    df_exportado = df[columnas_exportar]
    df_exportado.to_csv(archivo_salida_csv, index=False)




#------------------------------------------///----------------------------------------------#

def mostrar_menu():
    print("===== Menú =====")
    print("1. Buscar y filtrar datos")
    print("2. Formato de xlsx a csv")
    print("3. csv seleccionar columnas")
    print("4. Opción 4")
    print("5. Opción 5")
    print("6. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desee: ")

        if opcion == '1':
            opcion_buscar_y_filtrar()
        elif opcion == '2':
            print("Opción 2 seleccionada.")
            opcion_excel_csv()
        elif opcion == '3':
            print("Opción 3 seleccionada.")
            exportar_columnas_personalizado()
            
        elif opcion == '4':
            print("Opción 4 seleccionada.")
            # Agrega aquí el código para la opción 4
        elif opcion == '5':
            print("Opción 5 seleccionada.")
            # Agrega aquí el código para la opción 5
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
