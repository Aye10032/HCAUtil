import os

rootDir = 'C:/Users/yeyu6/Documents/MuMu共享文件夹/bgm'

for lists in os.listdir(rootDir):
    path = os.path.join(rootDir, lists)
    if os.path.isfile(path):
        decrypt = os.popen('.\HCADecoder.v1.21\hca.exe -c -a 01395C51 -b 00000000 ' + path)
        print(decrypt.read())
        decode = os.popen('.\HCADecoder.v1.21\hca.exe ' + path)
        print(decode.read())
