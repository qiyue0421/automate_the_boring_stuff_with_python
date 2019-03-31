import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press "cc" to quit.')
input()
print('Started.')
starttime = time.time()
lasttime = starttime
lapNum = 1

try:
    while True:
        input_text = input()
        if input_text == 'cc':
            raise Exception('Done.')
        # 循环一圈的时间
        lapTime = round(time.time() - lasttime, 2)
        # 总循环时间
        totalTime = round(time.time() - starttime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime))
        lapNum += 1
        lasttime = time.time()
except Exception as err:
    print(err)
