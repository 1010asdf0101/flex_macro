pyinstaller -F leave.py
pyinstaller -F on.py
Move-item -Path .\dist\leave.exe -Destination ~\leave.exe
Move-item -Path .\dist\on.exe -Destination "C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\on.exe"
Remove-Item .\build\
Remove-Item .\dist\
Remove-Item *.spec