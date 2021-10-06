import glob
import os
from PIL import Image

Ending='Ending'
beforeDir = "beforeDir"
afterDir = "afterDir"
# 缩放后图片宽高，以及文件后缀
img_w = int(input('width:'))
img_h = int(input('heigh:'))
img_type = input('文件后缀：')
if beforeDir == "":
    print('原图片路径正则错误')
    exit(0)
if afterDir == "":
    print('D:新文件目录无效')
    exit(0)
# 判断新文件目录是否存在，不存在则创建
if os.path.isdir(afterDir) == False:
    os.mkdir(afterDir)

def convertImage(file, outdir, width, height, type):
    img = Image.open(file)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        if type != "":
            temp = os.path.join(outdir, os.path.basename(file))
            new_img.save(os.path.splitext(temp)[0] + '.' + type)
        else:
            new_img.save(os.path.join(outdir, os.path.basename(file)))
    except Exception as e:
        print(e)
def start(oldDir, newDir, width, height, type):
    for root, dirs, files in os.walk(oldDir):
        for file in files:

            print(os.path.join(root, file))
            convertImage(os.path.join(root, file), newDir, width, height, type)
            '''
            for i in root:
                img = glob.glob(root)
                # 获取文件路径
                convertImage(img, newDir, width, height, type)
                print(os.path.join(root, file))
                
            '''
def SortImg():
    path = 'afterDir'  # 原始图片位置
    newpath ='Ending'  # 保存图片位置
    c = 1  # 从1开始
    filelists = os.listdir(path)
    for line in filelists:
        img = Image.open(path + '/' + line)
        a = "0" * (6 - len(str(c)))  # 6 是命名的位数,可以修改
        out = a + str(c) + '.jpg'
        img.save(os.path.join(newpath,out))
        c += 1

# 开始执行
start(beforeDir, afterDir, img_w, img_h, img_type)
SortImg()

input('按任意键退出...')
exit(0)