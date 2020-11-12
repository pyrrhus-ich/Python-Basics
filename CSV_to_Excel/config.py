importFolder = "/home/ich/importFiles"
import os

startfile = os.listdir(importFolder)

file = importFolder + '/' + startfile[0]
print(file)

