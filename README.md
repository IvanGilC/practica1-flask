# Práctica 1: desarrollo y despliegue de una aplicación con Flask y AWS

---

## Miembros del grupo

- Ivan Gil Cañizares
- Marco Beruet Morelli

---

## Descripción de la aplicación
Esta aplicación es una herramienta web sencilla desarrollada con el framework **Flask**. Su objetivo principal es permitir la interacción con el usuario mediante un formulario HTML donde se pueden introducir los nombres de los integrantes de un grupo.

La aplicación procesa esta información y la muestra de forma dinámica en la página. Además, cuenta con un sistema de **persistencia de datos** utilizando una base de datos **SQLite**, lo que permite que la información de los integrantes se mantenga guardada incluso si se reinicia el servidor. También incluye la gestión de contenido estático, como imágenes, y una estructura organizada que separa la lógica de la aplicación de la presentación.

---

## Instrucciones para ejecutar la aplicación en local

Para poner en marcha la aplicación en tu entorno local, sigue estos pasos:

### 1. Preparación del entorno
* **Crear el entorno virtual:** Dentro de la carpeta del proyecto, genera un entorno virtual de Python para aislar las dependencias.
    ```
    python3 -m venv venv
    ```
* **Activar el entorno virtual:**
    ```
    source venv/bin/activate
    ```
* **Instalar Flask:** Con el entorno activo, instala el framework necesario[cite: 13].
    ```
    pip install flask
    ```

### 2. Inicialización de la Base de Datos
* Asegúrate de tener el archivo `database.py` configurado para crear la base de datos SQLite (`grup.db`) al iniciar la aplicación.

### 3. Ejecución del servidor
* **Lanzar la aplicación:** Ejecuta el archivo principal de Python.
    ```
    python3 app.py
    ```
* **Acceder a la web:** Abre un navegador y dirígete a la dirección local. Por defecto, la aplicación escucha en el puerto **8000**.
    ```
    [http://127.0.0.1:8000](http://127.0.0.1:8000)
    ```

### 4. Uso de la aplicación
* Introduce los nombres de los integrantes en el formulario y pulsa el botón de enviar para ver cómo se actualiza la lista dinámicamente y se almacena en la base de datos.
