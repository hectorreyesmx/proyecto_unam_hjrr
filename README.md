
Proyecto con 3 Instancias EC2-Aws que inserta información de personas 
en una BD Postresql en un contenedor Docker.

Los 3 instancias tienen Ubuntu 24.04 y tienen estos datos:

>> app-server (python 3.12.3)
	IP-publica: 52.14.21.82
	IP-privada: 172.31.11.248


>>db-server (postgresql 15)
	IP-pública: 3.135.188.121
	IP-privada: 172.31.5.140

>>dns-server (bind9) 
	IP-publica: 3.147.86.20
	IP-privada: 172.31.6.238


--Conexión a la Base de DAtos.
Inicialmente hay que tener la llave de conexión PPK para conectarse vía Putty 
al servidor Postgresql con la IP-publica: 3.135.188.121
Una vez dentro de la Instancia, comprobaremos el servicio de doker.
Desde la consola ejecutamos ests comandos:

# docker ps   (validar que esté corriendo Postgresql)

# docker start postgres_container  (Para levantar Docker)

# docker exec -it postgres_container psql -U admin personas_registradas   (conexión a BD)


--En el server-app se puede crear un entorno virtual para ejecutar Python, para usar SqlAlchemy:

# python3 -m venv myenv

# source myenv/bin/activate

Posteriormente se pueden ejecutar archivos python, por ejemplo esta consulta:
# python3 /root/consulta_vista.py
# python3 actualiza_vista.py


--En el server-dns se registraron los 3 servidores del proyecto
y se pueden consultar con la siguiente manera:

# ping db.unam.local
# ping dns.unam.local
# ping app.unam.local


