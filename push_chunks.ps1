$folders = Get-ChildItem "data" -Directory

foreach ($folder in $folders) {
    Write-Host "Processing folder: $($folder.Name)"
    git add "data/$($folder.Name)/"
    
    # Check if anything was staged
    $status = git status --porcelain
    if ($status) {
        git commit -m "Add data/$($folder.Name)"
        Write-Host "Pushing $($folder.Name)..."
        git push
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Successfully pushed $($folder.Name)"
        } else {
            Write-Host "Failed to push $($folder.Name)" -ForegroundColor Red
            exit 1
        }
    } else {
        Write-Host "No changes in $($folder.Name)"
    }
}
