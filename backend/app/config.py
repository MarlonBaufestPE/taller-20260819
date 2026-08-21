import os

_secret_key = os.getenv("SECRET_KEY")
if not _secret_key or len(_secret_key) < 32:
    raise ValueError(
        "SECRET_KEY environment variable must be set and at least 32 characters long."
    )

SECRET_KEY: str = _secret_key
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS: int = 300
REFRESH_TOKEN_EXPIRE_SECONDS: int = 3600

VALID_USERNAME: str = os.getenv("VALID_USERNAME", "admin")
VALID_PASSWORD: str = os.getenv("VALID_PASSWORD", "admin123")
