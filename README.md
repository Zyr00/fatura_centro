# Faturação de Viaturas

Este projeto consiste em simplificar o processo de avaliar e desestruturar faturas de mecânicos em que cada
fatura vai ter um específico como a matrícula do carro, os KMs percorridos, vem como a data, cada fatura está
dividida em várias sub despesas como por exemplo mudança de óleo e a mudança de pneus, em que cada uma tem de
ser categorizada juntamente com o seu preço já com o IVA configurado. Tal que no final do mês seja possível
guardar um ficheiro csv com o que foi feito.

# Instalação

## Linux

```sh
git clone https://github.com/Zyr00/<project_name>
cd <project_name>

python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt

python ./main.py
```

# Uso

## Linux

```sh
cd <project_name>
source venv/bin/activate
python ./main.py
```

# Autor

João Cunha
