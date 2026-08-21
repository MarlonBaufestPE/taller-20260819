import hashlib
import hmac
import os
from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt

from app.config import (
    ACCESS_TOKEN_EXPIRE_SECONDS,
    ALGORITHM,
    REFRESH_TOKEN_EXPIRE_SECONDS,
    SECRET_KEY,
    VALID_PASSWORD,
    VALID_USERNAME,
)

_PASSWORD_SALT: bytes = os.urandom(16)


def _hash_password(password: str, salt: bytes) -> str:
    return hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=2**14,
        r=8,
        p=1,
    ).hex()


HASHED_PASSWORD: str = _hash_password(VALID_PASSWORD, _PASSWORD_SALT)


def verify_password(plain_password: str) -> bool:
    candidate = _hash_password(plain_password, _PASSWORD_SALT)
    return hmac.compare_digest(candidate, HASHED_PASSWORD)


def authenticate_user(username: str, password: str) -> bool:
    if username != VALID_USERNAME:
        return False
    return verify_password(password)


def create_access_token(data: dict, expires_delta: Optional[int] = None) -> str:
    to_encode = data.copy()
    expire_seconds = expires_delta if expires_delta is not None else ACCESS_TOKEN_EXPIRE_SECONDS
    expire = datetime.now(timezone.utc) + timedelta(seconds=expire_seconds)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(seconds=REFRESH_TOKEN_EXPIRE_SECONDS)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
