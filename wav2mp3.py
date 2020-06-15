import os

rootDir = 'C:/Users/yeyu6/Documents/MuMu共享文件夹/bgm'

for lists in os.listdir(rootDir):
    path = os.path.join(rootDir, lists)
    if os.path.isfile(path):
        FileType = os.path.splitext(path)[-1]
        if FileType == '.wav':
            fileName = path[:-4]
            decode = os.popen('ffmpeg.exe -i ' + fileName + '.wav -f mp3 -acodec libmp3lame -y ' + fileName + '.mp3')
            print(decode.read())
            delete = os.popen('Remove-Item ' + fileName + '.wav')
            print(delete.read())
