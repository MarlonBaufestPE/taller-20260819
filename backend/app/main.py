from fastapi import FastAPI, HTTPException, status
from jose import JWTError
from pydantic import BaseModel

from app.auth import (
    authenticate_user,
    create_access_token,
    create_refresh_token,
    decode_token,
)
from app.config import ACCESS_TOKEN_EXPIRE_SECONDS

app = FastAPI(title="JWT Auth API", version="1.0.0")


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = ACCESS_TOKEN_EXPIRE_SECONDS


class RefreshRequest(BaseModel):
    refresh_token: str


@app.post("/token", response_model=TokenResponse)
def login(request: LoginRequest):
    if not authenticate_user(request.username, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    access_token = create_access_token({"sub": request.username})
    refresh_token = create_refresh_token({"sub": request.username})
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@app.post("/refresh", response_model=TokenResponse)
def refresh_token(request: RefreshRequest):
    try:
        payload = decode_token(request.refresh_token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )
    if payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is not a refresh token",
        )
    username: str = payload.get("sub", "")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing subject",
        )
    access_token = create_access_token({"sub": username})
    new_refresh_token = create_refresh_token({"sub": username})
    return TokenResponse(access_token=access_token, refresh_token=new_refresh_token)
