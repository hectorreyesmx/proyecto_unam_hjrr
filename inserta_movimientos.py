from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define la cadena de conexi�n a la base de datos PostgreSQL
DATABASE_URL = "postgresql://admin:admin@172.31.5.140:5432/personas_registradas"

# Crea el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Define la base para la creaci�n de modelos
Base = declarative_base()

# Define la tabla
class Usuario(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True)
    persona_id = Column(Integer)
    tipo_movimiento = Column(String)
    fecha_movimiento = Column(Date)
    observaciones = Column(String)

# Crea las tablas en la base de datos (si no existen)
Base.metadata.create_all(engine)

# Crea una sesi�n para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Crea un nuevo usuario
##nuevo_usuario = Usuario(nombre="Juan Perez", correo="juan.perez@example.com")
nuevo_usuario = Usuario(persona_id=6, tipo_movimiento="Alta de persona PY", fecha_movimiento="2025-06-19", observaciones="Desde srcipt de PYthon")

# Agrega el usuario a la sesi�n
session.add(nuevo_usuario)

# Confirma la transacci�n para guardar los cambios en la base de datos
session.commit()

# Cierra la sesi�n
session.close()

print("MOVimiento insertado correctamente.")

