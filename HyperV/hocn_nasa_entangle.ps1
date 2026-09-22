# HOCN x NASA Core Entanglement Setup
Write-Host "Initializing Entanglement Matrix..." -ForegroundColor Cyan

$rootPath = "C:\Robdoerootauthority\HyperV"
$hocnPath = "$rootPath\HOCN"
$licenseRepo = "https://github.com/robdoeAiagency101/Licences.git"

# 1. Align Git Tracking & Add Remote
Set-Location $rootPath
if (!(git remote | Select-String "origin")) {
    git remote add origin $licenseRepo
    Write-Host "[] Linked to Remote Licenses Repo: $licenseRepo" -ForegroundColor Green
}

# 2. Check and Enforce Deterministic Paths
Write-Host "Verifying stack layout..." -ForegroundColor Yellow
$requiredPaths = @("HOCN\contracts", "HOCN\data", "HOCN\HOCN.Core", "HOCN\logic")
foreach ($path in $requiredPaths) {
    if (Test-Path "$rootPath\$path") {
        Write-Host "  [] Path Verified: $path" -ForegroundColor Green
    } else {
        New-Item -ItemType Directory -Path "$rootPath\$path" -Force | Out-Null
        Write-Host "  [+] Created Missing Node: $path" -ForegroundColor Magenta
    }
}

# 3. Synchronize Photon Engine Environment
if (Test-Path "$hocnPath\gvm_photon_engine.py") {
    Write-Host "[] Photon Engine Core active inside HOCN target matrix." -ForegroundColor Green
}

Write-Host "Entanglement Matrix fully synchronized. Operational." -ForegroundColor Cyan
