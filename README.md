# taller-20260819
Ejemplo practico de uso de GitHub Copilot Agent Coding

## Backend — JWT Auth API (FastAPI + Python)

Aplicación Web API construida con **FastAPI** que implementa autenticación mediante **JWT (JSON Web Tokens)**.

### Características
- Endpoint `POST /token`: recibe `username` y `password`, devuelve un access token (expira en 300 s) y un refresh token.
- Endpoint `POST /refresh`: recibe un refresh token válido y devuelve un nuevo par de tokens.
- Gestión de dependencias con **Poetry**.
- Contenerización con **Docker** y **docker-compose**.
- Pruebas unitarias con **pytest**.

---

## Requisitos

- [Docker](https://www.docker.com/) y [docker-compose](https://docs.docker.com/compose/) — para despliegue con contenedores.
- [Poetry](https://python-poetry.org/) — para desarrollo local.
- Python 3.11+

---

## Ejecución con Docker

```bash
cd backend
docker-compose up --build
```

La API quedará disponible en `http://localhost:8000`.

Para producción, cambia la variable de entorno `SECRET_KEY` en `docker-compose.yml` por un valor seguro y aleatorio.

---

## Ejecución local (sin Docker)

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

---

## Endpoints

### `POST /token`

Obtiene un par de tokens JWT enviando credenciales.

**Request body:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response:**
```json
{
  "access_token": "<jwt>",
  "refresh_token": "<jwt>",
  "token_type": "bearer",
  "expires_in": 300
}
```

**Ejemplo con curl:**
```bash
curl -X POST http://localhost:8000/token \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

---

### `POST /refresh`

Renueva el par de tokens usando un refresh token vigente.

**Request body:**
```json
{
  "refresh_token": "<jwt>"
}
```

**Response:** igual que `/token`.

**Ejemplo con curl:**
```bash
curl -X POST http://localhost:8000/refresh \
  -H "Content-Type: application/json" \
  -d '{"refresh_token": "<tu_refresh_token>"}'
```

---

## Documentación interactiva

Una vez levantada la API, visita:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Pruebas unitarias

```bash
cd backend
poetry install
poetry run pytest
```

---

## Variables de entorno

| Variable | Descripción | Default |
|---|---|---|
| `SECRET_KEY` | Clave secreta para firmar los JWT | `supersecretkey1234567890abcdef1234567890` |

> ⚠️ En producción, utiliza un valor largo, aleatorio y secreto para `SECRET_KEY`.

---

## Frontend — Cliente Web React

Aplicación web construida con **React** y **Vite** que implementa una página de login y una página de bienvenida protegida, conectada al backend JWT.

### Características
- **Página de login** (`/login`): formulario con usuario y contraseña. Llama al endpoint `POST /token` del backend, guarda el `access_token` y el `refresh_token` en `sessionStorage`.
- **Página de bienvenida** (`/welcome`): protegida — redirige a `/login` si no hay sesión activa. Muestra el nombre del usuario y permite cerrar sesión.
- Diseño basado en el estándar **PlayStation Design System** definido en `DESIGN.md` (colores, tipografía, botones, inputs).
- Escrito en **React** con **React Router v7** para navegación.

### Requisitos

- [Node.js](https://nodejs.org/) 18+ y npm 9+

### Ejecución local (desarrollo)

1. Primero levanta el backend (ver sección anterior).
2. En otra terminal:

```bash
cd frontend
npm install
npm run dev
```

La aplicación quedará disponible en `http://localhost:5173`.

> **Nota:** La variable de entorno `VITE_API_BASE_URL` indica la URL base del backend (por defecto `http://localhost:8000`). Crea un archivo `frontend/.env` copiando `frontend/.env.example` y ajusta si es necesario.

### Build para producción

```bash
cd frontend
npm run build
```

Los artefactos generados se guardan en `frontend/dist/`.

### Credenciales por defecto

| Campo | Valor |
|-------|-------|
| Usuario | `admin` |
| Contraseña | `admin123` |

> Las credenciales se configuran en el backend mediante las variables de entorno `VALID_USERNAME` y `VALID_PASSWORD`.
