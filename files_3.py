import os


class TextFile:
    def __init__(self, name):
        self.name = name
        self.row_count = sum(1 for _ in open(self.name, 'r'))


os.chdir('./sorted')

files = [TextFile('1.txt'),
         TextFile('2.txt'),
         TextFile('3.txt')]

files.sort(key=lambda x: x.row_count)

with open('all.txt', 'w+') as target:
    for i in files:
        target.write(f'{i.name} \n')
        target.write(f'{i.row_count} \n')
        for line in open(i.name, 'r').readlines():
            target.write(line)
        target.write('\n')

target.close()
