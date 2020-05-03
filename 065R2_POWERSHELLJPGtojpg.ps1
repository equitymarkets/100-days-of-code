#Problem was case-sensitivity in ".JPG" files. The only thing that worked for me was to do this twice-once to ".BAK" then to ".jpg".

Get-ChildItem *.JPG | Rename-Item -NewName { $_.Name -replace '.JPG', '.BAK' }
Get-ChildItem *.BAK | Rename-Item -NewName { $_.Name -replace '.BAK', '.jpg' }
