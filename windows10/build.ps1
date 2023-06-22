pip install -r ../requirements.txt
pyinstaller -F win_leave.py
pyinstaller -F win_on.py
Move-item -Path .\dist\win_leave.exe -Destination "C:\Users\$env:USERNAME\Desktop\off.exe"
Move-item -Path .\dist\win_on.exe -Destination "C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\on.exe"
Remove-Item .\build\ -Recurse
Remove-Item .\dist\ -Recurse
Remove-Item *.spec