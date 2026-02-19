# Informe sobre el desarrollo y despliegue de una aplicación con Flask y AWS

---

## Miembros del grupo

- Ivan Gil Cañizares
- Marco Beruet Morelli

---

## Python
3.10.12

---

## 1. ¿Qué función tiene el decorador `@app.route("/")` en una aplicación Flask?

En una aplicación desarrollada con **Flask**, el decorador `@app.route("/")` se utiliza para definir una ruta (endpoint) asociada a una función concreta del programa.

Su función principal es:

- Indicar qué código se ejecutará cuando un usuario acceda a una URL específica.
- En el caso de `"/"`, corresponde a la **ruta raíz** del sitio web.
- Vincular una dirección web con la lógica de la aplicación.

---

## 2. ¿Qué diferencia hay entre una petición GET y una petición POST en el contexto de la práctica?

En el desarrollo web, las peticiones **GET** y **POST** son métodos HTTP que permiten la comunicación entre el cliente (navegador) y el servidor.

### 🔹 Petición GET

- Se utiliza para **solicitar información** al servidor.
- Los datos se envían a través de la URL.
- Es visible en la barra del navegador.
- No debe usarse para enviar datos sensibles.
- No modifica el estado del servidor.

En la práctica, se utiliza normalmente para mostrar páginas o formularios.

### 🔹 Petición POST

- Se utiliza para **enviar datos al servidor**.
- Los datos se envían en el cuerpo (body) de la petición.
- No son visibles en la URL.
- Puede modificar el estado del servidor (por ejemplo, guardar datos en la base de datos).

En la práctica, POST se emplea para enviar formularios y almacenar información en la base de datos.

---

## 3. ¿Por qué en esta práctica no se ha subido el archivo `grup.db` al repositorio GitHub?

El archivo `grup.db` es una base de datos local (generalmente SQLite) que contiene información generada durante el desarrollo.

No se ha subido al repositorio de **GitHub** por las siguientes razones:

- **Seguridad:** puede contener datos sensibles o privados.
- **Buenas prácticas:** los archivos generados automáticamente no deben incluirse en el control de versiones.
- **Entornos diferentes:** cada entorno (local, producción, nube) puede tener su propia base de datos.
- **Optimización del repositorio:** evita aumentar innecesariamente el tamaño del proyecto.

Por este motivo, normalmente se incluye este tipo de archivos en el archivo `.gitignore`.

---

## 4. ¿Por qué es necesario configurar la aplicación Flask para que escuche en `0.0.0.0` cuando se despliega en AWS?

Por defecto, una aplicación Flask se ejecuta en `127.0.0.1` (localhost), lo que significa que solo puede accederse desde la propia máquina.

Cuando la aplicación se despliega en **AWS (Amazon Web Services)**, es necesario configurar el servidor para que escuche en `0.0.0.0` porque:

- Permite que la aplicación acepte conexiones desde cualquier interfaz de red.
- Hace posible que usuarios externos accedan mediante la IP pública de la instancia.
- Sin esta configuración, la aplicación no sería accesible desde Internet.

---

## 5. ¿Qué papel tienen los Security Groups en el despliegue de la aplicación en AWS?

En AWS, los **Security Groups** actúan como un **cortafuegos virtual** que controla el tráfico de red de una instancia (por ejemplo, una máquina virtual EC2).

Sus funciones principales son:

- Permitir o denegar tráfico de entrada (inbound rules).
- Controlar el tráfico de salida (outbound rules).
- Definir qué puertos están abiertos (por ejemplo, 22 para SSH o 5000/80 para la aplicación web).
- Restringir el acceso según direcciones IP específicas.

En el despliegue de la aplicación Flask:

- Se debe permitir el puerto donde se ejecuta la aplicación.
- Se debe habilitar el puerto 22 si se necesita acceso remoto por SSH.
- Si no se configuran correctamente, la aplicación no será accesible aunque esté funcionando correctamente.

---

## 6. ¿Por qué se recomienda desarrollar primero la aplicación en local y después desplegarla en la nube?

Desarrollar primero en entorno local es una práctica recomendada por varias razones:

### Facilita la detección de errores

Es más sencillo depurar problemas en un entorno controlado.

### Reduce costes

El uso de servicios en la nube como AWS puede generar costes. Trabajar en local evita gastos innecesarios durante la fase de desarrollo.

### Mayor rapidez en pruebas

Los cambios y pruebas son más rápidos en local que en un servidor remoto.

### Separación de entornos

Permite diferenciar claramente:

- Entorno de desarrollo (local)
- Entorno de producción (nube)

### Mayor estabilidad en producción

Se despliega únicamente una versión ya probada y funcional.

---

# Conclusión

Este informe recoge los conceptos fundamentales relacionados con el desarrollo de aplicaciones web con Flask y su posterior despliegue en AWS. Comprender el funcionamiento de las rutas, los métodos HTTP, la gestión de bases de datos, la configuración de red y las buenas prácticas de desarrollo es esencial para crear aplicaciones seguras, funcionales y preparadas para producción.
