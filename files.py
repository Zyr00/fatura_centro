import csv

class File:

    fields = []

    @staticmethod
    def save(filename, bills):
        print(filename)

        bill_formated = []
        for i in bills:
            for j in i.entries:
                bill_formated.append([])

        with open(filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(bill_formated)

