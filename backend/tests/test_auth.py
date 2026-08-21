import os
import pytest

os.environ.setdefault("SECRET_KEY", "test_secret_key_1234567890abcdef12345678")

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_success():
    response = client.post("/token", json={"username": "admin", "password": "admin123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"
    assert data["expires_in"] == 300


def test_login_wrong_password():
    response = client.post("/token", json={"username": "admin", "password": "wrong"})
    assert response.status_code == 401


def test_login_wrong_username():
    response = client.post("/token", json={"username": "unknown", "password": "admin123"})
    assert response.status_code == 401


def test_refresh_token_success():
    login = client.post("/token", json={"username": "admin", "password": "admin123"})
    refresh_token = login.json()["refresh_token"]

    response = client.post("/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data


def test_refresh_token_invalid():
    response = client.post("/refresh", json={"refresh_token": "invalid.token.value"})
    assert response.status_code == 401


def test_refresh_with_access_token_fails():
    login = client.post("/token", json={"username": "admin", "password": "admin123"})
    access_token = login.json()["access_token"]

    response = client.post("/refresh", json={"refresh_token": access_token})
    assert response.status_code == 401
