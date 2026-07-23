"""Helper utilities"""

from typing import Any, Optional, Dict
from datetime import datetime
import json


def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format datetime object to string"""
    if isinstance(dt, datetime):
        return dt.strftime(format_str)
    return str(dt)


def parse_datetime(date_str: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """Parse datetime string to object"""
    return datetime.strptime(date_str, format_str)


def safe_get(dictionary: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Safely get value from dictionary with nested key support"""
    keys = key.split(".")
    value = dictionary
    for k in keys:
        if isinstance(value, dict):
            value = value.get(k)
            if value is None:
                return default
        else:
            return default
    return value if value is not None else default


def format_json(data: Any, indent: int = 2) -> str:
    """Format data as JSON string"""
    return json.dumps(data, indent=indent, default=str)


def truncate_string(text: str, length: int = 50, suffix: str = "...") -> str:
    """Truncate string to specified length"""
    if len(text) > length:
        return text[:length - len(suffix)] + suffix
    return text


def convert_size(size_bytes: int) -> str:
    """Convert bytes to human readable format"""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"
