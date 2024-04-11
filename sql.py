import mysql.connector
import json

# Configura las credenciales de la base de datos
config = {
    "host": "srv891.hstgr.io",
    "user": "u395650491_admin",
    "password": "Futuro1234",
    "database": "u395650491_comida"
}

# Conecta a la base de datos
conn = mysql.connector.connect(**config)
print("Conectado")
if conn.is_connected():
    cursor = conn.cursor(dictionary=True)

    # Ejecuta la consulta
    query = "SELECT * FROM menu"
    cursor.execute(query)

    # Obtiene los resultados en formato JSON
    data = cursor.fetchall()
    json_data = json.dumps(data, indent=4)
    print(json_data)

    # Cierra la conexión
    cursor.close()
    conn.close()
else:
    print("No se pudo conectar a la base de datos.")
