import csv

# f=open('Seoul temperature.csv', 'r', encoding='cp949')
f=open('Seoul temperature.csv')

data=csv.reader(f)
print(data)

# for row in data:
#     print(row)

header = next(data)
print(header)

max_temp=-100
max_data=''

for row in data:
    try :
        row[-1] = float(row[-1])
        if row[-1] > max_temp:
            max_temp = row[-1]
            max_data = row[0]
        print(row)
    except :
        print(row)

print(max_temp)
print(max_data)

f.close()
