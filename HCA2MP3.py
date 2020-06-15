import os

rootDir = 'C:/Users/yeyu6/Documents/MuMu共享文件夹/bgm'

fileList = os.listdir(rootDir)
i = 1

for lists in fileList:
    path = os.path.join(rootDir, lists)
    if os.path.isfile(path):
        FileType = os.path.splitext(path)[-1]
        if FileType == '.hca':
            fileName = path[:-4]

            decrypt = os.popen('.\HCADecoder.v1.21\hca.exe -c -a 01395C51 -b 00000000 ' + path)
            print(decrypt.read())
            decode = os.popen('.\HCADecoder.v1.21\hca.exe ' + path)
            print(decode.read())

            decode = os.popen('ffmpeg.exe -i ' + fileName + '.wav -f mp3 -acodec libmp3lame -y ' + fileName + '.mp3')
            print(decode.read())
            delete = os.popen('Remove-Item ' + fileName + '.wav')
            print(delete.read())

            print('----------------' + str(i) + '/' + str(int(len(fileList)) + 1) + '----------------\n')
            i += 1
