import pytest
import httpx
from fastapi import FastAPI
from httpx import AsyncClient
from app import app  # assuming your FastAPI app is defined in app.py or similar

@pytest.mark.asyncio
async def test_registration():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Отправляем POST-запрос для создания нового пользователя
        new_user_data = {
            "username": "testuser",
            "password": "testpass",
            "email": "testuser@example.com",
            "phone": "1234567890"
        }
        response = await client.post("/register", json=new_user_data)
        assert response.status_code == 200
        
        user_info = response.json()
        assert user_info["username"] == "testirovchik"
        assert "id" in user_info
        assert user_info["email"] == "tests@example.com"
        assert user_info["phone"] == "1234567890"


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="http://test") as client:
        login_data = {"username": "testuser", "password": "testpass"}
        response = await client.post("/login", data=login_data)
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_profile_view():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/profile")
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_profile_edit():
    async with AsyncClient(app=app, base_url="http://test") as client:
        updated_profile_data = {"username": "newusername", "email": "newemail@example.com"}
        response = await client.put("/profile", json=updated_profile_data)
        assert response.status_code == 200
      
