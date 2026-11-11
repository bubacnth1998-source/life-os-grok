"""
LIFE OS - Security utilities (password hashing + JWT)
Uses PBKDF2-SHA256 (stdlib).
"""
from datetime import datetime, timedelta, timezone
from typing import Optional, Any
from jose import JWTError, jwt
import hashlib
import secrets
from app.core.config import settings


def _hash_password(password: str, salt: str | None = None) -> tuple[str, str]:
    if salt is None:
        salt = secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        120_000,
    )
    return salt, dk.hex()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        salt, stored = hashed_password.split("$", 1)
        _, computed = _hash_password(plain_password, salt)
        return secrets.compare_digest(stored, computed)
    except Exception:
        return False


def get_password_hash(password: str) -> str:
    salt, hashed = _hash_password(password)
    return f"{salt}${hashed}"


def create_access_token(data: dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
