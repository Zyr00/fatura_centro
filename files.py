import csv

class File:
    file = "cod.csv"

    fields = [
            "Mátricula",
            "Data de reparação",
            "Código",
            "Grupo",
            "Descrição",
            "Km's",
            "Nº de Pneus",
            "Medida de Pneus",
            "Fornecedor (Código do Fornecedor no SAC)",
            "Observações",
            "Responsável pelo Custo"]

    @staticmethod
    def save(filename, bills, codes):
        bill_formated = []
        for i in bills:
            for j in i.entries:
                group_and_des = File.get_from_code(j.code, codes)
                bill_formated.append([
                    i.registration,
                    i.date,
                    j.code,
                    group_and_des[0],
                    group_and_des[1],
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
