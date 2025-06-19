from sqlalchemy import create_engine, text

DB_USER = 'admin'
DB_PASSWORD = 'admin'
DB_HOST = '172.31.5.140'
DB_PORT = '5432'
DB_NAME = 'personas_registradas'

VISTA_MATERIALIZADA = 'resumen_movimientos'

# Crea URL de conexión
DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Crea motor de conexión
engine = create_engine(DATABASE_URL)

refresh_sql = f"REFRESH MATERIALIZED VIEW {VISTA_MATERIALIZADA};"

try:
    with engine.connect() as conexion:
        conexion.execute(text(refresh_sql))

        print(f"Vista materializada: '{VISTA_MATERIALIZADA}' actualizada ")

except Exception as e:
    print("Error al Actualizar la vista Materializada:", e)
