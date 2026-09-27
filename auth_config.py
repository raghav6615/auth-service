"""
Authentication & Session Configuration Module
Updated in accordance with security ticket SEC-104.
"""

# Token session validity period in hours
SESSION_EXPIRY_HOURS = 12

# Maximum consecutive failed login attempts before temporary account lockout
MAX_LOGIN_ATTEMPTS = 10

# Duration in minutes an account remains locked after exceeding max login attempts
LOCKOUT_MINUTES = 30
