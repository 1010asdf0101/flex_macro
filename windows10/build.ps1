pyinstaller -F leave.py
pyinstaller -F on.py
Move-item -Path .\dist\leave -Destination ~\leave
Move-item -Path .\dist\on -Destination "C:\Users\$env:USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
Set-alias byebye "~/leave $args[1] $args[2] $args[3]"

rm -rf build/ dist/
rm *.spec