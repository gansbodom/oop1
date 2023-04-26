lst = ['./sorted/1.txt', './sorted/2.txt', './sorted/3.txt']

for file in lst:
    print(file)
    print(sum(1 for line in open(file, 'r')))