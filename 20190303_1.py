import re, os, shutil

dateRegex = re.compile(r"""
    ^(.*?)                   # 前面可能出现一些字符，使用非贪心匹配
    (([01])?\d)-              # 月份
    (([0123])?\d)-          # 日期
    ((18|19|20)\d\d)         # 年份
    (.*?)$
""", re.VERBOSE)

# 遍历os.listdir()返回的文件名字符串列表
for amerFilename in os.listdir('.'):
    # search()方法返回match对象
    mo = dateRegex.search(amerFilename)

    # 不匹配正则表达式的，使用continue语句跳出循环
    if mo is None:
        continue

    # 用match对象的group()方法进行分组
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # 构成新文件名
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # 获取当前目录的绝对路径
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # 重命名
    print('Renaming "%s" to "%s' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
