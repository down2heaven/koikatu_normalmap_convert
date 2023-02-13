from PIL import Image, ImageColor
import os
def convert(path):
    normal_map=Image.open(path)                                                 #导入输入路径下的KK的法线贴图
    floder=os.path.dirname(path)
    name=os.path.basename(path)
    wid=normal_map.size[0]
    hei=normal_map.size[1]                                                      #读取宽高
    normal_map_gray=normal_map.convert('L')                                     #转换灰度图
    for w in range(wid):
      print("已进行",w,"列，共",wid,"列，已完成占比为：",w/wid)
      for h in range(hei):
         gray=normal_map_gray.getpixel((w,h))                                   #灰度
         alpha=normal_map.getpixel((w,h))[3]                                    #透明度
         normal_map.putpixel((w,h),(alpha,gray-59,255))                         #转换为正常的法线贴图
    a=os.path.exists(floder+'\converted')                                       #判断是否存在converted文件夹
    savepath=floder+'\converted'+'\\'
    if a:
        normal_map.save(savepath+name)
    else:
        os.mkdir(floder+'\\converted')
        normal_map.save(savepath+name)                                           #如果不存在该文件夹，则在输入路径中新建一个名叫converted的文件夹，并将结果保存在其中，存在则直接保存
    print(name,"已转换完成，保存在",savepath+name)
    return 0
print('''
请选择操作模式:
    若输入1，则本程序将会处理用户输入的单张图片
    若输入2，本程序将处理输入文件夹下所有图片（jpg和png）

无论何种模式，本程序都将在输入路径中新建一个名叫converted的文件夹，并将结果保存在其中
    ''')
mode=input("请输入1、2中的一个")
if mode=='1':
    inputpath=input("输入法线贴图路径：")
    convert(inputpath)
elif mode=='2':
    inputpath=input("输入文件夹路径：")
    list=os.listdir(inputpath)
    pic_num=0
    for filename in list:
       if filename.endswith('jpg') or filename.endswith('png'):
        pic_num=pic_num+1
    i=1
    for filename in list:
       if filename.endswith('jpg') or filename.endswith('png'):                 #遍历文件夹内所有jpg和png文件
          filepath=inputpath+'\\'+filename
          convert(filepath)
          print(filename,"处理完毕,","第",i,"张，共",pic_num,"张")
          i=i+1

