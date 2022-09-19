import csv
import random

count = 0
names = []
authors = []
numbers = 1
a = 1
tags = []
n = []
p = []
m = 0
search = input()
u = []

with open('books.csv', 'r') as csvfile, open('generator.txt', 'w') as twenty:
    #блок, отвечающий за названия больше 30 символов
    for row in csv.reader(csvfile, delimiter = ';'):
        count+=1
        if len(row[1]) > 30:
            names.append(row[1])
        if (row[6].find('2015') != -1) or (row[6].find('2018')):
            authors.append(row[3])

    #блок, записывающий в файл 20 произвольных произведений
    csvfile.seek(0)
    for row in csv.reader(csvfile, delimiter = ';'):
        a = random.randint(0, 1)
        if row[1].find('Название') == -1:
            if a == 0:
                year = row[6]
                twenty.write(str(numbers) + '.' + row[3] + '. ' + row[1] + ' - ' + year[6 : 10] + '\n')
                numbers += 1
                if numbers == 21:
                    break

    #блок, который выдаёт все уникальные теги
    csvfile.seek(0)
    for row in csv.reader(csvfile, delimiter=';'):
        c = row[12].split('# ')
        tags.append(0)
        for i in range(1, len(c)):
            tags.append('#' + c[i])

    #блок, который преобразует количество выдач из str в int
    csvfile.seek(0)
    for row in csv.reader(csvfile, delimiter=';'):
        if m == 1:
            h = row
            h[8] = int(h[8])
            p.append(h)
        m = 1

    #блок для поиска книг
    csvfile.seek(0)
    for row in csv.reader(csvfile, delimiter = ';'):
        if ((row[3].lower()).find(search.lower()) != -1) and (row[6].find('2015')):
            print(row)
        elif ((row[3].lower()).find(search.lower())) != -1 and (row[6].find('2018')):
            print(row)

print(count)
print(names)
print(authors)
print(set(tags))

#блок, сортирующий книги по популярности
s = sorted(p, key=lambda p: p[8])
for i in range(20):
    print(s[-(i+1)])




