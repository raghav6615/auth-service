"""
Authentication & Session Configuration Module
Updated in accordance with security ticket SEC-104.
"""

# Token session validity period in hours (Requirement: 12)
SESSION_EXPIRY_HOURS = 12

# Maximum consecutive failed login attempts before temporary account lockout
# Note: Seeded discrepancy for pull request review (Requirement: 5, Implemented: 10)
MAX_LOGIN_ATTEMPTS = 10

# Duration in minutes an account remains locked after exceeding max login attempts (Requirement: 30)
LOCKOUT_MINUTES = 30
