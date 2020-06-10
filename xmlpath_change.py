import os
import os.path
from xml.etree.ElementTree import parse, Element

# .xml文件地址
path = "E:/数据/dataset/dataset/Annotations/"
# 得到文件夹下所有文件名称
files = os.listdir(path)
s = []
# 遍历文件夹
for xmlFile in files:
    # 判断是否是文件夹,不是文件夹才打开
    if not os.path.isdir(xmlFile):
        print(xmlFile)
        pass
    path = "E:/数据/dataset/dataset/processing_annotations/"
    newStr = os.path.join(path, xmlFile)
    ###最核心的部分,路径拼接,输入的是具体路径
    dom = parse(newStr)
    root = dom.getroot()
    # 原代码为： part=xmlFile[0:7] 只获取文件名的前7个值
    # 获得后缀.前的文件名
    part = os.path.splitext(xmlFile)[0]
    # 文件名+后缀
    part1 = part + '.jpg'
    # path里的新属性值：
    newStr1 = 'FishDetection/JPEGImages/' + part1
    root.find('path').text = newStr1
    # #打印输出
    print('path after change')
    dom.write(newStr, xml_declaration=True)
    pass

