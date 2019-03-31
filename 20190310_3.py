import threading
import time


def takeANop():
    time.sleep(5)
    print('Wake up!')


threadobj = threading.Thread(target=takeANop)
# 创建新的线程并执行目标函数
threadobj.start()

print('End of program!')

threadobj1 = threading.Thread(target=print, args=['cats', 'dogs', 'pigs'], kwargs={'sep': ' & '})
threadobj1.start()
