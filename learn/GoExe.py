import os

name = input()
os.system("pyinstaller -F " + name + ".py")
