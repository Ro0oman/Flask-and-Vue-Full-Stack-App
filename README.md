# Aplicación de Tareas con Flask y Vue.js

Una aplicación web de lista de tareas (To-Do list) que utiliza Flask para el backend y la renderización de plantillas, y Vue.js para añadir reactividad en el lado del cliente.

## Descripción del Proyecto

Este proyecto es un ejemplo de cómo construir una aplicación web monolítica donde el backend (Flask) se encarga de la lógica de negocio, la interacción con la base de datos y la renderización inicial del HTML. Vue.js se integra directamente en las plantillas de Flask para manejar de forma reactiva las interacciones del usuario (crear, completar, eliminar tareas) sin necesidad de recargar la página.

La aplicación está diseñada para ser desplegada fácilmente en una plataforma serverless como Vercel.

## Stack Tecnológico

*   **Backend:** [Python](https://www.python.org/) con [Flask](https://flask.palletsprojects.com/)
*   **Base de Datos:** [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
*   **Frontend (Reactividad):** [Vue.js](https://vuejs.org/)
*   **Validación de Formularios:** [Flask-WTF](https://flask-wtf.readthedocs.io/)
*   **Despliegue:** [Vercel](https://vercel.com/)

## Instalación y Configuración

Sigue estos pasos para configurar el entorno de desarrollo en tu máquina local.

### Prerrequisitos

*   [Python 3.8+](https://www.python.org/downloads/)
*   [Node.js y npm](https://nodejs.org/)
*   [Git](https://git-scm.com/)

### Pasos 

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd Flask-and-Vue-Full-Stack-App
    ```

2.  **Configura el Backend (Flask):**
    ```bash
    # Navega al directorio raíz (donde está app.py)
    # Crea y activa un entorno virtual
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate

    # Instala las dependencias de Python
    pip install -r requirements.txt
    ```
    *(Nota: Vue.js se carga en el frontend, probablemente a través de una CDN en `index.html`, por lo que no se requiere un paso de compilación con Node.js/npm para el desarrollo local.)*

## Uso (Desarrollo Local)

Para ejecutar la aplicación en tu máquina local, simplemente inicia el servidor de desarrollo de Flask.
Desde el directorio raíz y con el entorno virtual activado:
```bash
flask run
```
Abre tu navegador y ve a `http://127.0.0.1:5000`. El servidor de Flask servirá la página principal y gestionará todas las llamadas a la API desde el frontend de Vue.

## Despliegue en Vercel

Este proyecto está configurado para un despliegue sencillo en Vercel. El fichero `vercel.json` en la raíz del proyecto se encarga de la configuración:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

Este fichero le indica a Vercel que:
1.  Use el builder de Python (`@vercel/python`) para el fichero `app.py`.
2.  Redirija todas las peticiones entrantes (`/(.*)`) a la aplicación Flask (`app.py`).

Para desplegar, simplemente conecta tu repositorio de GitHub/GitLab/Bitbucket a Vercel.

## Endpoints de la API

La aplicación expone los siguientes endpoints que son consumidos por el cliente de Vue.js.

| Método | Endpoint   | Payload (JSON)            | Descripción                                                                                             |
|--------|------------|---------------------------|---------------------------------------------------------------------------------------------------------|
| `GET`  | `/`        | N/A                       | Renderiza la página `index.html`. Si la petición incluye la cabecera `X-Requested-With: XMLHttpRequest`, devuelve una lista de todas las tareas en formato JSON. |
| `POST` | `/create`  | `{ "title": "string" }`   | Crea una nueva tarea. Devuelve el objeto de la tarea recién creada en formato JSON.                     |
| `POST` | `/delete`  | `{ "id": "integer" }`     | Elimina una tarea existente por su ID. Devuelve una confirmación.                                       |
| `POST` | `/complete`| `{ "id": "integer" }`     | Marca una tarea como completada. Devuelve una confirmación.                                             |

## Licencia

*(Considera añadir una licencia a tu proyecto, como la licencia MIT, para que otros sepan cómo pueden usar tu código.)*

Este proyecto está bajo la Licencia MIT. Ver el fichero `LICENSE` para más detalles.