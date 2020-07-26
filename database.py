class Database:
    def __init__(self):
        file = open('database.txt', 'r+')
        self.conv = [_[:-1] for _ in file]
        file.close()

    def get(self):
        file = open('database.txt', 'r+')
        self.conv = [_[:-1] for _ in file]
        file.close()
        return self.conv

    def add(self, message):
        file = open('database.txt', 'a')
        file.write(str(message)+'\n')
        file.close()

    def remove(self):
        with open('database.txt', 'r') as fin:
            data = fin.read().splitlines(True)
        with open('database.txt', 'w') as fout:
            fout.writelines(data[1:])
