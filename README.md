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
