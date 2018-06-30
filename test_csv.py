import csv
# with open('./static/test.csv') as cs:
#     reader = csv.DictReader(cs)
#     for row in reader:
#         print(row['day01'],row['day01-0'])


write = csv.writer(open('./static/test.csv','a'))
# write.writerow(['day04','day04-1','day04-2'])
data = [range(3) for i in range(3)]
for item in data:
    write.writerows(str(item))


reader = csv.reader(open('./static/test.csv','r'))
for item in reader:
    print(item)
