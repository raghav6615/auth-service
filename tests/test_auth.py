import unittest
import auth_config
from auth_service import AuthService


class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth = AuthService()

    def test_token_lifetime(self):
        expected_seconds = auth_config.SESSION_EXPIRY_HOURS * 3600
        self.assertEqual(self.auth.get_token_lifetime_seconds(), expected_seconds)

    def test_lockout_trigger(self):
        username = "testuser"
        for _ in range(auth_config.MAX_LOGIN_ATTEMPTS - 1):
            self.auth.record_failed_attempt(username)
            self.assertFalse(self.auth.is_locked(username))

        self.auth.record_failed_attempt(username)
        self.assertTrue(self.auth.is_locked(username))


if __name__ == "__main__":
    unittest.main()
