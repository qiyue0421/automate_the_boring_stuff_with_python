import re, os, shutil

dateRegex = re.compile(r"""
    ^(.*?)                   # 前面可能出现一些字符，使用非贪心匹配
    ((0|1)?\d)-              # 月份
    ((0|1|2|3)?\d)-          # 日期
    ((18|19|20)\d\d)         # 年份
    (.*?)$
""", re.VERBOSE)

for amerFilename in os.listdir('.'):
    # search()方法返回match对象
    mo = dateRegex.search(amerFilename)
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
