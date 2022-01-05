from format_error import FormatError

class Entry:
    def __init__(self, price, code, ntires, size, obs):
        try:
            price_as_float = float(price);
            # self.price = (price_as_float * 0.23) + price_as_float
            self.price = str(price_as_float)
        except:
            raise FormatError("Preço mal formatado use . em vez de ,")

        try:
            int_as_code = int(code);
            self.code = str(int_as_code)
        except:
            raise FormatError("Código deve ser um numero")

        try:
            int_as_ntires = int(ntires);
            self.ntires = str(int_as_ntires)
        except:
            raise FormatError("Numero de Pneus deve ser um numero")

        self.size = size
        self.obs = obs

    def __str__(self):
        return f"Preço: {self.price}€, Código: {self.code}, Numero Pneus: {self.ntires} Obs: {self.obs}"

    def __repr__(self):
        return str(self)
