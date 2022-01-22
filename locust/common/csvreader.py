import csv


class CSVReader:
    def __init__(self, file):
        try:
            file = open(file)
        except TypeError:
            pass
        self.file = file
        self.reader = csv.reader(file)

    def __next__(self):
        try:
            return next(self.reader)
        except StopIteration:
            self.file.seek(0, 0)
            return next(self.reader)
