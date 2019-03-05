"""import pyperclip, sys


passwd = {'qiyue': 'qiyue',
          'root': 'root',
          'mima': 'mima'}

while True:
    print('enter which one you want know:')
    account = input()
    if account in passwd:
        pyperclip.copy(passwd[account])
        print(account + '\'s passwd is ' + pyperclip.paste())
        break
    else:
        print(account + ' has not passwd')
"""
tableDate=[['apples', 'oranges', 'cherries', 'banana'],
           ['Alice', 'Bob', 'Carol', 'David'],
           ['dogs', 'cats', 'moose', 'goose']]


def findmaxlen(Dates):
    maxlen=0
    for i in range(len(Dates)):
        if len(Dates[i])>maxlen:
            maxlen=len(Dates[i])
    return maxlen


def printTable(List):
    k=len(List)#列表的个数
    v=len(List[0])#列表中元素的个数
    for i in range(v):
        for j in range(k):
            print(List[j][i].rjust(findmaxlen(List[j])),end=' ')
        print()


printTable(tableDate)
