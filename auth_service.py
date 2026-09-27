"""
Core Authentication Service Logic
"""
import time
from typing import Dict
import auth_config


class AuthService:
    def __init__(self):
        self.failed_attempts: Dict[str, int] = {}
        self.locked_until: Dict[str, float] = {}

    def is_locked(self, username: str) -> bool:
        if username in self.locked_until:
            if time.time() < self.locked_until[username]:
                return True
            else:
                # Lockout expired
                del self.locked_until[username]
                self.failed_attempts[username] = 0
        return False

    def record_failed_attempt(self, username: str) -> None:
        attempts = self.failed_attempts.get(username, 0) + 1
        self.failed_attempts[username] = attempts
        if attempts >= auth_config.MAX_LOGIN_ATTEMPTS:
            self.locked_until[username] = time.time() + (auth_config.LOCKOUT_MINUTES * 60)

    def reset_attempts(self, username: str) -> None:
        self.failed_attempts.pop(username, None)
        self.locked_until.pop(username, None)

    def get_token_lifetime_seconds(self) -> int:
        return auth_config.SESSION_EXPIRY_HOURS * 3600
