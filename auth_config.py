"""
Authentication & Session Configuration Module
Baseline configuration prior to SEC-104 policy update.
"""

# Token session validity period in hours
SESSION_EXPIRY_HOURS = 24

# Maximum consecutive failed login attempts before temporary account lockout
MAX_LOGIN_ATTEMPTS = 3

# Duration in minutes an account remains locked after exceeding max login attempts
LOCKOUT_MINUTES = 15
