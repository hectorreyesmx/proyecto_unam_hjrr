from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configura los parámetros de conexión
DB_USER = 'admin'
DB_PASSWORD = 'admin'
###DB_HOST = '3.144.114.219'  # IP-publica de PstgreSql
DB_HOST = '172.31.5.140'  # IP-privada de PstgreSql
DB_PORT = '5432'
DB_NAME = 'personas_registradas'

# Crea la URL de conexión
DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Crea el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crea una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Prueba la conexión
try:
    connection = engine.connect()
    print("Conexión exitosa a PostgreSQL")
    connection.close()
except Exception as e:
    print("Error al conectar a PostgreSQL:", e)

# Cierra la sesión cuando ya no la necesites
session.close()
