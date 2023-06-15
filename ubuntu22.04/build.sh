#!bin/bash/
pyinstaller -F leave.py
pyinstaller -F on.py
mv ./dist/leave ~/leave
mv ./dist/on ~/on
echo "alias byebye='~/leave $1 $2 $3'" >> ~/.bashrc

rm -rf build/ dist/
rm *.spec