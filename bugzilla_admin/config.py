"""Configuration management for Bugzilla Admin Client"""

import os
import json
from pathlib import Path
from typing import Optional, Dict, Any
from dataclasses import dataclass, asdict
from cryptography.fernet import Fernet
import base64
import hashlib


@dataclass
class ServerConfig:
    """Bugzilla server configuration"""
    url: str
    timeout: int = 30
    verify_ssl: bool = True
    proxy: Optional[str] = None


@dataclass
class UIConfig:
    """UI configuration"""
    theme: str = "light"  # light or dark
    window_width: int = 1400
    window_height: int = 900
    sidebar_width: int = 250
    auto_refresh_interval: int = 300  # seconds
    show_notifications: bool = True


class ConfigManager:
    """Manages application configuration"""

    def __init__(self):
        """Initialize configuration manager"""
        self.config_dir = Path.home() / ".bugzilla_admin"
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.credentials_file = self.config_dir / "credentials.enc"
        self._cipher = self._init_cipher()
        self.server_config: Optional[ServerConfig] = None
        self.ui_config = UIConfig()
        self._load_config()

    def _init_cipher(self) -> Fernet:
        """Initialize encryption cipher for credentials"""
        key_file = self.config_dir / ".key"
        if key_file.exists():
            with open(key_file, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, "wb") as f:
                f.write(key)
        return Fernet(key)

    def _load_config(self) -> None:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r") as f:
                    data = json.load(f)
                    if "server" in data:
                        self.server_config = ServerConfig(**data["server"])
                    if "ui" in data:
                        ui_data = data["ui"]
                        self.ui_config = UIConfig(**ui_data)
            except Exception as e:
                print(f"Error loading config: {e}")

    def save_config(self) -> None:
        """Save configuration to file"""
        try:
            data = {
                "server": asdict(self.server_config) if self.server_config else None,
                "ui": asdict(self.ui_config),
            }
            with open(self.config_file, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")

    def save_credentials(
        self, username: str, password: str, api_token: Optional[str] = None
    ) -> None:
        """Save encrypted credentials"""
        try:
            creds = {
                "username": username,
                "password": password,
                "api_token": api_token,
            }
            encrypted = self._cipher.encrypt(json.dumps(creds).encode())
            with open(self.credentials_file, "wb") as f:
                f.write(encrypted)
        except Exception as e:
            print(f"Error saving credentials: {e}")

    def load_credentials(self) -> Optional[Dict[str, str]]:
        """Load encrypted credentials"""
        if not self.credentials_file.exists():
            return None
        try:
            with open(self.credentials_file, "rb") as f:
                encrypted = f.read()
            decrypted = self._cipher.decrypt(encrypted)
            return json.loads(decrypted.decode())
        except Exception as e:
            print(f"Error loading credentials: {e}")
            return None

    def clear_credentials(self) -> None:
        """Clear stored credentials"""
        if self.credentials_file.exists():
            self.credentials_file.unlink()

    def get_recent_servers(self) -> list:
        """Get list of recent server connections"""
        recent_file = self.config_dir / "recent_servers.json"
        if recent_file.exists():
            try:
                with open(recent_file, "r") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def add_recent_server(self, url: str) -> None:
        """Add server to recent list"""
        recent_file = self.config_dir / "recent_servers.json"
        recent = self.get_recent_servers()
        if url in recent:
            recent.remove(url)
        recent.insert(0, url)
        recent = recent[:10]  # Keep last 10
        try:
            with open(recent_file, "w") as f:
                json.dump(recent, f, indent=2)
        except Exception as e:
            print(f"Error saving recent servers: {e}")


# Global configuration instance
config_manager = ConfigManager()
