from format_error import FormatError

class Entry:
    def __init__(self, price, code, ntires, size, obs):
        try:
            self.price = float(price);
            self.price_iva = (self.price * 0.23) + self.price
            self.price = str(self.price)
            self.price_iva = str(self.price_iva)
        except:
            raise FormatError("Preço mal formatado use . em vez de ,")

        try:
            self.code = int(code)
            self.code = str(code)
        except:
            raise FormatError("Código deve ser um numero")

        try:
            self.ntires = int(ntires);
            self.ntires = str(self.ntires)
        except:
            raise FormatError("Numero de Pneus deve ser um numero")

        self.size = size
        self.obs = obs

    def __str__(self):
        return f"Preço: {self.price}€,\nPreço IVA: {self.price_iva}\nCódigo: {self.code},\nNumero Pneus: {self.ntires},\nObs: {self.obs}"

    def __repr__(self):
        return str(self)
