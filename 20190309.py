import os


def findbigfile(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            abs_filename = os.path.join(foldername, filename)
            if os.path.getsize(abs_filename) > 100000000:
                print(abs_filename)

                
findbigfile(folder='c:\\')
