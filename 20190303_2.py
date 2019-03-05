import zipfile, os


def backupToZip(folder):
    num = 1

    # 确保folder是绝对路径
    folder = os.path.abspath(folder)

    # 创建一个循环，检查备份ZIP文件的名称是否已经存在,存在则换个名字；不存在则跳出循环并使用该文件名
    while True:
        # 设置备份文件名，例如：backupfile_1.zip
        zipFilename = os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists(zipFilename):
            break
        num += 1

    # 创建ZipFile对象
    print('Starting backup...')
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # 遍历目录树并添加到ZIP文件
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))

        # 加入当前目录
        backupZip.write(foldername)

        # 加入目录中的文件
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            # 判断是否是以前生成的备份文件，如果是则跳过这个文件
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Backup Done.')


backupDir = 'E:\\Game'
backupToZip(backupDir)
