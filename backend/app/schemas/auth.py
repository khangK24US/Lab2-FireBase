from pydantic import BaseModel, EmailStr
from typing import Optional

class SignupRequest(BaseModel):
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class GoogleLoginRequest(BaseModel):
    id_token: str

class AuthResponse(BaseModel):
    email: str
    uid: str
    idToken: Optional[str] = None
    refreshToken: Optional[str] = None