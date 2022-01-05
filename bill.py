from format_error import FormatError

class Bill:
    def __init__(self, date, supplier, registration, kms, entries):
        try:
            self.date = date.toString('dd/MM/yyyy')
        except Exception as e:
            raise FormatError(f"Data mal formatada {e}")

        try:
            self.supplier = int(supplier)
            self.supplier = str(self.supplier)
        except:
            raise FormatError("Fornecedor mal formatado tem de ser um numero")

        self.registration = registration

        try:
            self.kms = int(kms)
            self.kms = str(self.kms)
        except:
            raise FormatError("KMs mal formatado tem de ser um numero")

        self.entries = list(entries)
        #if len(self.entries) == 0:
        #    raise FormatError("Sem entradas")

    def __str__(self):
        return f"Data {self.date}, Fornecedor {self.supplier}, Matrícula {self.registration}, KMs {self.kms}, numero entradas {len(self.entries)}"

    def __repr__(self):
        return str(self)
