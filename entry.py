class Entry:
    def __init__(self, price, code, ntiers, size, obs):
        try:
            price_as_float = float(price);
        except:
            raise FormatError("Preço mal formatado use . em vez de ,")
        self.price = (price_as_float * 0.23) + price_as_float

        try:
            int_as_code = int(price);
        except:
            raise FormatError("Codigo deve ser um numero")
        self.code = code

        try:
            int_as_ntiers = int(ntiers);
        except:
            raise FormatError("Numero de Pneus deve ser um numero")
        self.ntiers = int_as_ntiers

        self.size = size
        self.obs = obs

    def __str__(self):
        return f" {self.price}€, {self.code}"

    def __repr__(self):
            return str(self)
