"""Input validators"""

from typing import Optional
import re


class ValidationError(Exception):
    """Custom validation error"""
    pass


class Validators:
    """Collection of input validators"""

    @staticmethod
    def validate_url(url: str) -> bool:
        """Validate URL format"""
        url_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
        return bool(re.match(url_pattern, url))

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, email))

    @staticmethod
    def validate_username(username: str) -> bool:
        """Validate username format"""
        if len(username) < 3 or len(username) > 50:
            return False
        username_pattern = r'^[a-zA-Z0-9_.-]+$'
        return bool(re.match(username_pattern, username))

    @staticmethod
    def validate_password(password: str) -> tuple[bool, str]:
        """Validate password strength"""
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        if not re.search(r'[a-z]', password):
            return False, "Password must contain lowercase letters"
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain uppercase letters"
        if not re.search(r'\d', password):
            return False, "Password must contain digits"
        return True, "Password is valid"

    @staticmethod
    def validate_not_empty(value: str, field_name: str = "Field") -> bool:
        """Validate field is not empty"""
        return bool(value and value.strip())

    @staticmethod
    def validate_length(value: str, min_len: int = 0, max_len: int = 255) -> bool:
        """Validate string length"""
        return min_len <= len(value) <= max_len

    @staticmethod
    def validate_number(value: str) -> bool:
        """Validate if string is a number"""
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_api_token(token: str) -> bool:
        """Validate API token format"""
        return len(token) >= 20 and len(token) <= 255
