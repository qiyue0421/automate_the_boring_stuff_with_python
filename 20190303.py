import os

"""
total = 0
for filename in os.listdir('C:\\Windows'):
    total += os.path.getsize(os.path.join('C:\\Windows', filename))

print(os.listdir('G:\\WeGame'))
print(total)
"""
import random


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

savedir = 'F:\\python\\Test paper\\'

# 循环，35份试卷
for quizNum in range(35):
    # 以‘写模式’打开试卷和答案文件，这里自动创建了该文件
    quizFile = open(savedir + 'capitalsquiz%s.txt' % (quizNum+1), 'w')
    answerKeyFile = open(savedir + 'capitalsquiz_answers%s.txt' % (quizNum+1), 'w')

    quizFile.write('Name:\n\nData:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    # 循环，50个问题
    for questionNum in range(50):
        # 正确答案通过字典键值对获取
        correctAnswer = capitals[states[questionNum]]

        # 获取错误答案列表，并删除其中的正确答案,选出随机的三个答案
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)

        # 获取四个选项，其中一个正确答案三个错误答案
        answerOptions = wrongAnswers + [correctAnswer]

        # 打乱选项的排序
        random.shuffle(answerOptions)

        # 循环，创建试题，每个试题四个选项
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum+1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # 将试题的答案写入答案文件，index()方法用来获取列表值的下标
        answerKeyFile.write('%s. %s\n' % (questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
