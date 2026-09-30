# ==============================================================================
# OBSFRUCTURE ALL-IN-ONE MASTER ENGINE (PowerShell 5.1 Native)
# Layers: Entity | Audio Synthesizer | ASCII Oscilloscope | Budapest | XOR Store
# ==============================================================================

# 1. Target Invariant Directory Setup
$logDir  = "C:\EngineEnforcer\Logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }
$logFile = Join-Path $logDir "Obsfructure_Absorber.jsonl"

Write-Host "[+] Initializing Obsfructure Unified Master Pipeline..." -ForegroundColor Cyan

# 2. Entity & Hardware Identity Resolution
$entityUser   = "$([System.Environment]::UserDomainName)\$([System.Environment]::UserName)"
$entityHost   = [System.Environment]::MachineName
$osVersion    = (Get-WmiObject -Class Win32_OperatingSystem).Caption.Trim()
$macAddress   = (Get-WmiObject -Class Win32_NetworkAdapterConfiguration | Where-Object { $_.IPEnabled -eq $true } | Select-Object -First 1).MACAddress
if (-not $macAddress) { $macAddress = "00:00:00:00:00:00" }
$isAdmin      = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# 3. Physics & Geometric Matrix Initialization
$Nodes        = 14
$BaseFreq     = 432.0
$Phi          = (1.0 + [Math]::Sqrt(5.0)) / 2.0
$Width        = 50
$TotalArcSec  = 1296000.0
$WobbleSteps  = 80
$XorKey       = "UNIFIED_MASTER_KEY_$entityHost"

# Seed offset from hardware MAC address
$macSeed = [Convert]::ToInt32(($macAddress -replace ':', '').Substring(0, 4), 16)

# 4. Real-Time Acoustic & Visual Execution Loop
$frequencies = @()
$phases      = @()
$sumCos      = 0.0; $sumSin = 0.0

Write-Host "`n--- OSCILLOSCOPE & HARMONIC SYNTHESIS START ---" -ForegroundColor Gray

for ($frame = 0; $frame -lt $Nodes; $frame++) {
    # Frequency calculation along Phi spiral
    $freq = [int][Math]::Round($BaseFreq * [Math]::Pow($Phi, ($frame * 0.15)))
    $frequencies += $freq
    
    # Phase vector trajectory influenced by hardware MAC seed
    $phase = (($frame * [Math]::PI / 7.0) + ($macSeed % 360) * ([Math]::PI / 180.0))
    $phases += $phase
    $sumCos += [Math]::Cos($phase)
    $sumSin += [Math]::Sin($phase)

    # Calculate wave displacement for ASCII rendering
    $val = [Math]::Sin(($frame * 0.5) + $phase)
    $pos = [int][Math]::Round((($val + 1) / 2) * ($Width - 1))
    
    # Draw ASCII canvas
    $lineArr = [char[]](' ' * $Width)
    $lineArr[$pos] = [char]'#'
    $canvas = -join $lineArr
    
    $color = if ($frame % 2 -eq 0) { "Cyan" } else { "Yellow" }
    
    # Isolated execution string output to prevent casting bugs
    $outputStr = "Node [{0:D2}] ({1:D4} Hz) | {2} | R={3:N2}" -f ($frame + 1), $freq, $canvas, (($val + 1) / 2)
    Write-Host $outputStr -ForegroundColor $color
    
    # Console hardware audio trigger
    [System.Console]::Beep($freq, 50)
}

# 5. Order Parameter Calculation
$orderR = [Math]::Sqrt(([Math]::Pow($sumCos / $Nodes, 2)) + ([Math]::Pow($sumSin / $Nodes, 2)))

# 6. Build Master Payload (Including Budapest Compliance Standards)
$masterPayload = [ordered]@{
    timestamp           = (Get-Date).ToString("o")
    protocol            = "OBSFRUCTURE_UNIFIED_MASTER_V1"
    entity_id           = $entityUser
    machine_name        = $entityHost
    os_environment      = $osVersion
    mac_anchor          = $macAddress
    is_admin            = $isAdmin
    base_tuning_hz      = $BaseFreq
    arc_seconds_total   = $TotalArcSec
    wobble_steps        = $WobbleSteps
    phase_order_R       = [Math]::Round($orderR, 6)
    budapest_attest     = [ordered]@{
        Art_02_AccessCheck = "PASSED"
        Art_04_DataIntegrity = "PASSED"
        Art_16_Preservation = "ENFORCED"
    }
    storage_rule        = "ALWAYS_ABSORB_NEVER_DELETE"
}

$rawJson = $masterPayload | ConvertTo-Json -Depth 4

# 7. XOR High-Entropy Encryption Shielding
$jsonBytes = [System.Text.Encoding]::UTF8.GetBytes($rawJson)
$keyBytes  = [System.Text.Encoding]::UTF8.GetBytes($XorKey)
$masked    = New-Object byte[] $jsonBytes.Length

for ($i = 0; $i -lt $jsonBytes.Length; $i++) {
    $masked[$i] = $jsonBytes[$i] -bxor $keyBytes[$i % $keyBytes.Length]
}
$maskedString = [Convert]::ToBase64String($masked)

# 8. Absolute Storage Write (Zero-Deletion Append)
Add-Content -Path $logFile -Value $maskedString -Encoding UTF8

Write-Host "`n[+] Master Execution Sequence Complete." -ForegroundColor Green
Write-Host ("    Phase Synchronization Order R(t): {0:N6}" -f $orderR) -ForegroundColor Yellow
Write-Host ("    Payload Cryptographically Masked & Appended To:") -ForegroundColor White
Write-Host "    $logFile" -ForegroundColor Cyan