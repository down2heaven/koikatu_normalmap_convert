from PIL import Image, ImageColor
import os


# 转换函数
def convert(path):
    normal_map = Image.open(path)  # 导入输入路径下的KK的法线贴图
    floder = os.path.dirname(path)
    name = os.path.basename(path)
    wid = normal_map.size[0]
    hei = normal_map.size[1]  # 读取宽高
    normal_map_gray = normal_map.convert('L')  # 转换灰度图
    for w in range(wid):
        print('\r' + "已进行", w, "列，共", wid, "列，已完成", w / wid, end='', flush=True)
        for h in range(hei):
            gray = normal_map_gray.getpixel((w, h))  # 获取灰度图中的灰度
            alpha = normal_map.getpixel((w, h))[3]  # 获取输入图片中的透明度
            normal_map.putpixel((w, h), (alpha, gray - 59, 255))  # 转换为正常的法线贴图
    a = os.path.exists(floder + '\\converted')  # 判断是否存在converted文件夹
    savepath = floder + '\\converted' + '\\'
    if a:
        normal_map.save(savepath + name)
    else:
        os.mkdir(floder + '\\converted')
        normal_map.save(savepath + name)  # 如果不存在该文件夹，则在输入路径中新建一个名叫converted的文件夹，并将结果保存在其中，存在则直接保存
    print(name, "已转换完成，保存在", savepath + name)
    return 0


# opengl转恋活
def reverse_convert(path):
    normal_map = Image.open(path)  # 导入输入路径下的法线贴图
    floder = os.path.dirname(path)
    name = os.path.basename(path)
    wid = normal_map.size[0]
    hei = normal_map.size[1]  # 读取宽高
    normal_map = normal_map.convert('RGBA')  # 转换RGBA
    normal_map_gray = normal_map.convert('LA')  # 转换灰度图
    for w in range(wid):
        print('\r' + "已进行", w, "列，共", wid, "列，已完成", w / wid, end='', flush=True)
        for h in range(hei):
            red, green, blue, alpha = normal_map.getpixel((w, h))  # 获取RGB信息
            normal_map_gray.putpixel((w, h), (green+59, red))
            # 转换为kk法线贴图，作者测试时候使用本程序将恋活导出的法线贴图转换为OpenGL法线贴图之后再转换为恋活用法线贴图，经测试。当灰色通道为green+59时和原来一致，故如此设置
    a = os.path.exists(floder + '\\normal_map_for_kk')  # 判断是否存在normal_map_for_kk文件夹
    savepath = floder + '\\normal_map_for_kk' + '\\'
    if a:
        normal_map_gray.save(savepath + name)
    else:
        os.mkdir(floder + '\\normal_map_for_kk')
        normal_map_gray.save(savepath + name)  # 如果不存在该文件夹，则在输入路径中新建一个名叫converted的文件夹，并将结果保存在其中，存在则直接保存
    print(name, "已转换完成，保存在", savepath + name)
    return 0


print('''
请选择操作模式:
    若输入1，本程序将把用户输入的单张恋活法线贴图转换为普通法线贴图
    若输入2，本程序将处理输入文件夹下所有恋活法线贴图转换为普通法线贴图（jpg和png）
    若输入3，本程序将把已有的单张opengl法线贴图转换为恋活中的使用的法线贴图
    若输入4，本程序将把已有的输入文件夹下的所有opengl法线贴图转换为恋活中的使用的法线贴图

无论何种模式，本程序都将在输入路径中新建一个名叫converted的文件夹，并将结果保存在其中
    ''')
mode = input("请输入1、2、3、4中的一个")
if mode == '1':
    inputpath = input("输入恋活法线贴图路径：")
    convert(inputpath)
elif mode == '2':
    inputpath = input("输入恋活法线贴图文件夹路径：")
    list = os.listdir(inputpath)
    pic_num = 0
    for filename in list:
        if filename.endswith('jpg') or filename.endswith('png'):
            pic_num = pic_num + 1
    i = 1
    for filename in list:
        if filename.endswith('jpg') or filename.endswith('png'):  # 遍历文件夹内所有jpg和png文件
            filepath = inputpath + '\\' + filename
            convert(filepath)
            print(filename, "处理完毕,", "第", i, "张，共", pic_num, "张")
            i = i + 1
elif mode == '3':
    inputpath = input("输入opengl法线贴图路径：")
    reverse_convert(inputpath)
elif mode == '4':
    inputpath = input("输入opengl法线贴图文件夹路径：")
    list = os.listdir(inputpath)
    pic_num = 0
    for filename in list:
        if filename.endswith('jpg') or filename.endswith('png'):
            pic_num = pic_num + 1
    i = 1
    for filename in list:
        if filename.endswith('jpg') or filename.endswith('png'):
            filepath = inputpath + '\\' + filename
            reverse_convert(filepath)
            print(filename, "处理完毕,", "第", i, "张，共", pic_num, "张")
            i = i + 1
