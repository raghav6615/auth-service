# Auth Service

Authentication and session policy management microservice.

## Security Ticket SEC-104 Specification

Our service requires updated security policy parameters:
- **Session Token Expiration**: `SESSION_EXPIRY_HOURS = 12` (tokens expire after 12 hours)
- **Maximum Failed Login Attempts**: `MAX_LOGIN_ATTEMPTS = 5` (lock out account after 5 consecutive failures)
- **Account Lockout Duration**: `LOCKOUT_MINUTES = 30` (temporary lockout lasts 30 minutes)

## Verification
Run unit tests with:
```bash
python -m unittest discover tests
```
