from format_error import FormatError

class Entry:
    def __init__(self, price, code, ntires, size, obs):
        try:
            price_as_float = float(price);
        except:
            raise FormatError("Preço mal formatado use . em vez de ,")
        self.price = (price_as_float * 0.23) + price_as_float
        self.price = str(self.price)

        try:
            int_as_code = int(code);
        except:
            raise FormatError("Código deve ser um numero")
        self.code = code

        try:
            int_as_ntires = int(ntires);
        except:
            raise FormatError("Numero de Pneus deve ser um numero")
        self.ntires = int_as_ntires
        self.ntires = str(self.ntires)

        self.size = size
        self.obs = obs

    def __str__(self):
        return f"Preço: {self.price}€, Código: {self.code}, Numero Pneus: {self.ntires} Obs: {self.obs}"

    def __repr__(self):
        return str(self)
