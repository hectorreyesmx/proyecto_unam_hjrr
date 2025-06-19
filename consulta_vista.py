from sqlalchemy import create_engine, text

DB_USER = 'admin'
DB_PASSWORD = 'admin'
DB_HOST = '172.31.5.140'
DB_PORT = '5432'
DB_NAME = 'personas_registradas'

# Crear URL de conexión
DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Crear motor de conexión
engine = create_engine(DATABASE_URL)

# Consulta a la vista
consulta_sql = "SELECT * FROM resumen_movimientos;"

try:
    with engine.connect() as conexion:
        resultado = conexion.execute(text(consulta_sql))

        print("Registros de la vista: resumen_movimientos")
        for fila in resultado:
            print(fila)

except Exception as e:
    print("Error al consultar la vista:", e)
