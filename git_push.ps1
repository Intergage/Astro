$files = Read-Host -Prompt 'File / Files to add_> '
$commit = Read-host -Prompt 'Commit comment_> '

git add $files
git commit -m $commit
git push -u AstroAPI master
