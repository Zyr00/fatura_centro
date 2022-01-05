import csv

from PyQt5.QtCore import QDate

from entry import Entry
from bill import Bill

class File:
    file = "cod.csv"

    fields = [
            "Mátricula",
            "Data de reparação",
            "Código",
            "Grupo",
            "Descrição",
            "Preço",
            "Km's",
            "Nº de Pneus",
            "Medida de Pneus",
            "Fornecedor (Código do Fornecedor no SAC)",
            "Observações",
            "Responsável pelo Custo"]

    @staticmethod
    def save(filename, bills, codes):
        bill_formated = []

        try:
            for i in bills:
                for j in i.entries:
                    group_and_des = File.get_from_code(j.code, codes)
                    bill_formated.append([
                        i.registration,
                        i.date,
                        j.code,
                        group_and_des[0],
                        group_and_des[1],
                        j.price,
                        i.kms,
                        j.ntires,
                        j.size,
                        i.supplier,
                        j.obs,
                        "Aces Alto Ave Guimarães"
                        ])

            with open(filename, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(File.fields)
                writer.writerows(bill_formated)
        except Exception as e:
            print(e)
            return False

        return True

    @staticmethod
    def load_bills(filename):
        bills = []
        with open(filename, "r") as rawfile:
            file = csv.DictReader(rawfile)
            for line in file:
                b = Bill(
                    QDate.fromString(line[File.fields[1]], "dd/MM/yyyy"),
                    line[File.fields[9]],
                    line[File.fields[0]],
                    line[File.fields[6]],
                    [])
                e = Entry(
                    (float(line[File.fields[5]]) / 123) * 100,
                    line[File.fields[2]],
                    line[File.fields[7]],
                    line[File.fields[8]],
                    line[File.fields[10]])

                pos = File.find_in_bill(bills, b)
                if pos != -1:
                    bills[pos].entries.append(e)
                else:
                    b.entries.append(e)
                    bills.append(b)

        return bills

    @staticmethod
    def find_in_bill(bills, b):
        for i in range(len(bills)):
            if (b.date == bills[i].date and
                b.kms == bills[i].kms and
                b.supplier == bills[i].supplier and
                b.registration == bills[i].registration):
                return i

        return -1

    @staticmethod
    def load(filename):
        content = []
        with open(filename, "r") as file:
            csvfile = csv.DictReader(file)
            for line in csvfile:
                content.append(dict(line))
        return content

    @staticmethod
    def get_from_code(code, codes):
        for i in codes:
            if i['cod'] == code:
                return (i['grupo'], i['des'])
        return ('', '')
