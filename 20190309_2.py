import openpyxl
import pprint

print('Opening workbook...')

# 打开excel文件，获取工作表
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

countyData = {}

print('Reading rows...')

# 迭代每个有数据的行
for row in range(2, sheet.max_row + 1):
    # 每行数据包括洲名、县名、人口数据
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # 确保州简称的存在，不存在则设为state变量的值
    countyData.setdefault(state, {})

    # 确保县名称的存在，不存在设为county变量的值
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # 针对当前的县，增加tracts、pop的值
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('Writing results...')
resultFile = open('census2019.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
