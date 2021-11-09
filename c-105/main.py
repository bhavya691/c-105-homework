import csv
import math
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data = file_data[0]
total = 0
for n in file_data:
    total+=int(n)
mean = total/len(file_data)
sqlist = []
for n in file_data:
    a = int(n)-mean
    a = a ** 2
    sqlist.append(a)
sum = 0
for i in sqlist:
    sum+=i
result = sum/(len(sqlist)-1)
stdev = math.sqrt(result)
print(stdev)