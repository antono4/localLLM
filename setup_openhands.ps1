# OpenHands SDK Setup untuk Windows (PowerShell)
# Otomatis menggunakan uv jika tersedia

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "🚀 OpenHands SDK Setup" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Fungsi untuk install packages
function Install-Packages {
    param([string]$Method)
    
    Write-Host "📦 Menginstall packages..." -ForegroundColor Yellow
    Write-Host ""
    
    $Packages = "openhands-sdk openhands-tools openhands-workspace"
    
    switch ($Method) {
        "uv" {
            Write-Host "✅ uv ditemukan! Menggunakan uv..." -ForegroundColor Green
            uv pip install $Packages
        }
        "pip" {
            Write-Host "📝 Menggunakan pip..." -ForegroundColor Yellow
            pip install --upgrade $Packages
        }
    }
    
    Write-Host ""
    Write-Host "============================================" -ForegroundColor Cyan
    Write-Host "📋 Informasi Install" -ForegroundColor Cyan
    Write-Host "============================================" -ForegroundColor Cyan
    
    pip show openhands-sdk 2>$null | Select-String -Pattern "^(Name|Version):"
    pip show openhands-workspace 2>$null | Select-String -Pattern "^(Name|Version):"
}

# Cek Python version
Write-Host "🐍 Python version:" -ForegroundColor Yellow
python --version
Write-Host ""

# Cek uv
$UseUv = $false
if (Get-Command uv -ErrorAction SilentlyContinue) {
    $UseUv = $true
    Write-Host "✅ uv tersedia" -ForegroundColor Green
} else {
    Write-Host "📝 uv tidak ditemukan, akan menggunakan pip" -ForegroundColor Yellow
}

# Cek apakah packages sudah ada
$Installed = pip show openhands-sdk 2>$null
if ($Installed) {
    Write-Host "📌 openhands-sdk sudah terinstall:" -ForegroundColor Yellow
    $Installed | Select-String "Version:"
    Write-Host ""
    
    $Upgrade = Read-Host "Upgrade? (y/N)"
    if ($Upgrade -eq "y" -or $Upgrade -eq "Y") {
        Install-Packages -Method $(if($UseUv){"uv"}else{"pip"})
    }
} else {
    Write-Host "📦 openhands-sdk belum terinstall" -ForegroundColor Yellow
    Install-Packages -Method $(if($UseUv){"uv"}else{"pip"})
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "✅ Setup selesai!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📝 Untuk menjalankan:" -ForegroundColor Yellow
Write-Host '   $env:OPENHANDS_CLOUD_API_KEY="sk-oh-your-key"'
Write-Host "   python contoh_openhands_cloud.py"
Write-Host ""
