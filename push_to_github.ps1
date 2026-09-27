# PowerShell script to push auth-service branches to GitHub and prepare PR
param (
    [string]$RemoteUrl
)

if (-not $RemoteUrl) {
    Write-Host "Please enter your GitHub repository URL (e.g., https://github.com/<your-username>/auth-service.git):" -ForegroundColor Cyan
    $RemoteUrl = Read-Host "Remote URL"
}

if (-not $RemoteUrl) {
    Write-Host "Error: Remote URL cannot be empty." -ForegroundColor Red
    exit 1
}

# Check if origin already exists
$existingRemote = git remote get-url origin 2>$null
if ($existingRemote) {
    Write-Host "Updating existing origin remote..." -ForegroundColor Yellow
    git remote set-url origin $RemoteUrl
} else {
    Write-Host "Adding origin remote..." -ForegroundColor Yellow
    git remote add origin $RemoteUrl
}

Write-Host "Pushing 'main' branch..." -ForegroundColor Green
git push -u origin main

Write-Host "Pushing 'feat/sec-104-auth-policy' branch..." -ForegroundColor Green
git push -u origin feat/sec-104-auth-policy

Write-Host ""
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "SUCCESS! Both branches are pushed to GitHub." -ForegroundColor Green
Write-Host "Next steps on GitHub:" -ForegroundColor Yellow
Write-Host "1. Open your repository on GitHub."
Write-Host "2. Click 'Compare & pull request' for 'feat/sec-104-auth-policy'."
Write-Host "3. Set Title: feat(auth): update session timeout and lockout limits"
Write-Host "4. Set Description: Implements security policy SEC-104 requirements."
Write-Host "5. Click 'Create pull request'."
Write-Host "=================================================================" -ForegroundColor Cyan
