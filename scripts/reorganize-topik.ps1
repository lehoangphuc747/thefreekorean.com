# reorganize-topik.ps1
# Reorganize TOPIK_ALL_OF_THE_YEARS folder with full English naming
# Convention: TOPIK-{level}-{exam}-{type}.{ext}

$ErrorActionPreference = "Continue"
$root = "G:\My Drive\korean\topik\TOPIK_ALL_OF_THE_YEARS"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$mappingFile = Join-Path $scriptDir "topik-mapping.txt"

# ============================================================
# BƯỚC 0: Kiểm tra
# ============================================================
if (-not (Test-Path $root)) {
    Write-Host "ERROR: Folder not found: $root" -ForegroundColor Red
    exit 1
}
if (-not (Test-Path $mappingFile)) {
    Write-Host "ERROR: Mapping file not found: $mappingFile" -ForegroundColor Red
    exit 1
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  TOPIK File Reorganization Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ============================================================
# BƯỚC 1: Tạo thư mục cho mỗi kỳ
# ============================================================
Write-Host "[1/5] Creating exam directories..." -ForegroundColor Yellow
$exams = @("35","36","37","41","52","54","60","61","63","64","66","78","83","88","91","96","102")
foreach ($exam in $exams) {
    $dir = Join-Path $root $exam
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "  Created: $exam/" -ForegroundColor Green
    } else {
        Write-Host "  Exists:  $exam/" -ForegroundColor DarkGray
    }
}

# ============================================================
# BƯỚC 2: Đọc mapping và rename + move
# ============================================================
Write-Host ""
Write-Host "[2/5] Renaming and moving files..." -ForegroundColor Yellow

$lines = Get-Content -LiteralPath $mappingFile -Encoding UTF8
$movedCount = 0
$skipCount = 0
$errorCount = 0

foreach ($line in $lines) {
    $line = $line.Trim()
    if (-not $line -or $line -match '^#') { continue }
    
    $parts = $line -split '\|', 2
    if ($parts.Count -ne 2) { continue }
    
    $oldName = $parts[0].Trim()
    $newRel = $parts[1].Trim()
    
    $oldPath = Join-Path $root $oldName
    $newPath = Join-Path $root $newRel

    if (Test-Path -LiteralPath $oldPath) {
        # Nếu file đích đã tồn tại, thêm suffix
        if (Test-Path -LiteralPath $newPath) {
            $dir = Split-Path $newPath
            $name = [System.IO.Path]::GetFileNameWithoutExtension($newPath)
            $ext = [System.IO.Path]::GetExtension($newPath)
            $newPath = Join-Path $dir "$name-combined$ext"
            Write-Host "  [WARN] Target exists, using: $name-combined$ext" -ForegroundColor DarkYellow
        }
        
        # Tạo thư mục đích nếu chưa có
        $destDir = Split-Path $newPath
        if (-not (Test-Path -LiteralPath $destDir)) {
            New-Item -ItemType Directory -Path $destDir -Force | Out-Null
        }
        
        try {
            Move-Item -LiteralPath $oldPath -Destination $newPath -Force
            Write-Host "  OK: $oldName -> $newRel" -ForegroundColor Green
            $movedCount++
        } catch {
            Write-Host "  ERR: $oldName - $($_.Exception.Message)" -ForegroundColor Red
            $errorCount++
        }
    } else {
        $skipCount++
    }
}

Write-Host "  Moved: $movedCount | Skipped: $skipCount | Errors: $errorCount" -ForegroundColor Cyan

# ============================================================
# BƯỚC 3: Xử lý Audio Folders
# ============================================================
Write-Host ""
Write-Host "[3/5] Processing audio folders..." -ForegroundColor Yellow

$audioMappings = @(
    @{ OldFolder = "TOPIK_2_60_AUDIO"; NewFolder = "60\audio" }
    @{ OldFolder = "TOPIK_2_64_AUDIO"; NewFolder = "64\audio" }
    @{ OldFolder = "TOPIK_2_83_AUDIO"; NewFolder = "83\audio" }
    @{ OldFolder = "TOPIK_2_91_AUDIO"; NewFolder = "91\audio" }
    @{ OldFolder = "TOPIK_1_96_AUDIO"; NewFolder = "96\audio\topik-1" }
    @{ OldFolder = "TOPIK_2_96_AUDIO"; NewFolder = "96\audio\topik-2" }
)

foreach ($am in $audioMappings) {
    $oldDir = Join-Path $root $am.OldFolder
    if (-not (Test-Path -LiteralPath $oldDir)) {
        Write-Host "  Skip: $($am.OldFolder) (not found)" -ForegroundColor DarkGray
        continue
    }

    $newDir = Join-Path $root $am.NewFolder
    if (-not (Test-Path -LiteralPath $newDir)) {
        New-Item -ItemType Directory -Path $newDir -Force | Out-Null
    }

    # Find all audio files recursively, skip macOS ._* files
    $audioFiles = Get-ChildItem -LiteralPath $oldDir -Recurse -File | Where-Object {
        $_.Extension -match '\.(mp3|wma|wav)$' -and $_.Name -notmatch '^\._'
    } | Sort-Object Name

    $counter = 1
    foreach ($f in $audioFiles) {
        $ext = $f.Extension
        $newName = "{0:D2}-track-{1:D2}{2}" -f $counter, $counter, $ext
        $newFilePath = Join-Path $newDir $newName
        
        try {
            Copy-Item -LiteralPath $f.FullName -Destination $newFilePath -Force
            $counter++
        } catch {
            Write-Host "  ERR copying: $($f.Name) - $($_.Exception.Message)" -ForegroundColor Red
        }
    }

    Write-Host "  $($am.OldFolder) -> $($am.NewFolder)/ ($($counter-1) tracks)" -ForegroundColor Green
}

# ============================================================
# BƯỚC 4: Cleanup
# ============================================================
Write-Host ""
Write-Host "[4/5] Cleaning up..." -ForegroundColor Yellow

# Delete duplicate
$dupFile = Join-Path $root "35th TOPIK II Listening Text (1).pdf"
if (Test-Path -LiteralPath $dupFile) {
    Remove-Item -LiteralPath $dupFile -Force
    Write-Host "  Deleted duplicate: 35th TOPIK II Listening Text (1).pdf" -ForegroundColor Red
}

# Delete all desktop.ini recursively
$desktopIni = Get-ChildItem -LiteralPath $root -Recurse -Filter "desktop.ini" -Force
foreach ($di in $desktopIni) {
    Remove-Item -LiteralPath $di.FullName -Force
}
Write-Host "  Deleted $($desktopIni.Count) desktop.ini files" -ForegroundColor Red

# Delete macOS ._ files
$macFiles = Get-ChildItem -LiteralPath $root -Recurse -Filter "._*" -Force
foreach ($mf in $macFiles) {
    Remove-Item -LiteralPath $mf.FullName -Force
}
Write-Host "  Deleted $($macFiles.Count) macOS ._ files" -ForegroundColor Red

# Delete old audio folders (now copied to new locations)
foreach ($am in $audioMappings) {
    $oldDir = Join-Path $root $am.OldFolder
    if (Test-Path -LiteralPath $oldDir) {
        Remove-Item -LiteralPath $oldDir -Recurse -Force
        Write-Host "  Removed old folder: $($am.OldFolder)/" -ForegroundColor Red
    }
}

# Delete .crdownload files
$crFiles = Get-ChildItem -LiteralPath $root -Recurse -Filter "*.crdownload" -Force
foreach ($cf in $crFiles) {
    Remove-Item -LiteralPath $cf.FullName -Force
    Write-Host "  Deleted incomplete download: $($cf.Name)" -ForegroundColor Red
}

# ============================================================
# BƯỚC 5: Report
# ============================================================
Write-Host ""
Write-Host "[5/5] Final Report" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan

foreach ($exam in $exams) {
    $examDir = Join-Path $root $exam
    if (Test-Path -LiteralPath $examDir) {
        $files = Get-ChildItem -LiteralPath $examDir -File
        $dirs = Get-ChildItem -LiteralPath $examDir -Directory
        $fileCount = $files.Count
        $dirInfo = ""
        if ($dirs.Count -gt 0) {
            $subFileCount = (Get-ChildItem -LiteralPath $examDir -Recurse -File).Count - $fileCount
            $dirInfo = " + $($dirs.Count) folders ($subFileCount audio files)"
        }
        Write-Host ("  {0,-4}/ ({1} files{2})" -f $exam, $fileCount, $dirInfo) -ForegroundColor White
        
        foreach ($f in ($files | Sort-Object Name)) {
            Write-Host "    $($f.Name)" -ForegroundColor DarkGray
        }
    }
}

# Check remaining files in root
$rootFiles = Get-ChildItem -LiteralPath $root -File
$rootDirs = Get-ChildItem -LiteralPath $root -Directory
$remainingFiles = $rootFiles | Where-Object { $_.Name -ne "topik-mapping.txt" }
$remainingDirs = $rootDirs | Where-Object { $exams -notcontains $_.Name }

if ($remainingFiles.Count -gt 0 -or $remainingDirs.Count -gt 0) {
    Write-Host ""
    Write-Host "  REMAINING IN ROOT (not moved):" -ForegroundColor Yellow
    foreach ($f in $remainingFiles) {
        Write-Host "    FILE: $($f.Name)" -ForegroundColor Yellow
    }
    foreach ($d in $remainingDirs) {
        Write-Host "    DIR:  $($d.Name)/" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  DONE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
