"""Logging configuration and utilities"""

import logging
import logging.handlers
from pathlib import Path
from datetime import datetime
from typing import Optional


class LogManager:
    """Manages application logging"""

    def __init__(self):
        """Initialize log manager"""
        self.log_dir = Path.home() / ".bugzilla_admin" / "logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger("bugzilla_admin")
        self.logger.setLevel(logging.DEBUG)
        self._setup_handlers()
        self.activities = []

    def _setup_handlers(self) -> None:
        """Setup logging handlers"""
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

        # File handler with rotation
        log_file = self.log_dir / "bugzilla_admin.log"
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=10485760, backupCount=5
        )
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def log_activity(
        self, action: str, module: str, details: Optional[str] = None
    ) -> None:
        """Log user activity"""
        timestamp = datetime.now()
        activity = {
            "timestamp": timestamp,
            "action": action,
            "module": module,
            "details": details,
        }
        self.activities.append(activity)
        self.logger.info(f"{module} - {action}: {details}")

    def log_api_request(
        self, method: str, url: str, headers: dict, body: Optional[str] = None
    ) -> None:
        """Log API request"""
        self.logger.debug(f"API Request: {method} {url}")
        self.logger.debug(f"Headers: {headers}")
        if body:
            self.logger.debug(f"Body: {body}")

    def log_api_response(
        self, status_code: int, response_text: str, duration: float
    ) -> None:
        """Log API response"""
        self.logger.debug(f"API Response: {status_code} ({duration:.2f}s)")
        if len(response_text) > 500:
            self.logger.debug(f"Response (truncated): {response_text[:500]}...")
        else:
            self.logger.debug(f"Response: {response_text}")

    def log_error(self, error: Exception, context: Optional[str] = None) -> None:
        """Log error"""
        if context:
            self.logger.error(f"{context}: {str(error)}", exc_info=True)
        else:
            self.logger.error(str(error), exc_info=True)

    def get_recent_activities(self, limit: int = 50) -> list:
        """Get recent activities"""
        return self.activities[-limit:]

    def export_logs(self, filepath: str) -> None:
        """Export logs to file"""
        with open(filepath, "w") as f:
            for activity in self.activities:
                f.write(
                    f"{activity['timestamp']} - {activity['action']} "
                    f"({activity['module']}): {activity['details']}\n"
                )


# Global logger instance
log_manager = LogManager()


def setup_logging() -> None:
    """Setup logging for the application"""
    global log_manager
    log_manager = LogManager()
