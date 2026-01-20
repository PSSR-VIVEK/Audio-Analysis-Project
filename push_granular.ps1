$maxSizeMB = 200
$currentBatchSize = 0
$fileCount = 0
$files = Get-ChildItem "data" -Recurse -File

Write-Host "Found $($files.Count) files. Starting batch processing..."

foreach ($file in $files) {
    # Check if file is already tracked/committed (skip if status is clean)
    # Actually simpler: git add everything one by one, and commit when batch size is reached.
    # But wait, git status check is slow for every file.
    
    # We did a reset for processed_audio. others are untracked.
    # Just add the file.
    git add $file.FullName
    
    $currentBatchSize += ($file.Length / 1MB)
    $fileCount++
    
    if ($currentBatchSize -ge $maxSizeMB) {
        Write-Host "Batch limit reached ($([math]::round($currentBatchSize, 2)) MB). Committing and Pushing..."
        git commit -m "Add data batch ($fileCount files)"
        
        # Retry push mechanism
        $maxRetries = 3
        $retry = 0
        $success = $false
        
        while (-not $success -and $retry -lt $maxRetries) {
            git push
            if ($LASTEXITCODE -eq 0) {
                $success = $true
                Write-Host "Batch pushed successfully."
            }
            else {
                $retry++
                Write-Host "Push failed. Retrying in 5 seconds... ($retry/$maxRetries)"
                Start-Sleep -Seconds 5
            }
        }
        
        if (-not $success) {
            Write-Host "Failed to push batch after $maxRetries attempts. Exiting." -ForegroundColor Red
            exit 1
        }
        
        $currentBatchSize = 0
        $fileCount = 0
    }
}

# Final batch
if ($currentBatchSize -gt 0) {
    Write-Host "Pushing final batch..."
    git commit -m "Add remaining data files"
    git push
}

Write-Host "All data pushed successfully!"
