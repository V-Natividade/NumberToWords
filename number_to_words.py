class NumberToWords:
    def __init__(self, number):
        self.number_list = self.split_numbers(number)
        self.signal = self.signal()
        self.units = {
            "0": "zero",
            "1": "um",
            "2": "dois",
            "3": "três",
            "4": "quatro",
            "5": "cinco",
            "6": "seis",
            "7": "sete",
            "8": "oito",
            "9": "nove",
        }
        self.tens = {
            "10": "dez",
            "11": "onze",
            "12": "doze",
            "13": "treze",
            "14": "catorze",
            "15": "quinze",
            "16": "dezesseis",
            "17": "dezessete",
            "18": "dezoito",
            "19": "dezenove",
            "2": "vinte",
            "3": "trinta",
            "4": "quarenta",
            "5": "cinquenta",
            "6": "sessenta",
            "7": "setenta",
            "8": "oitenta",
            "9": "noventa",
        }
        self.hundreds = {
            "1": "cem",
            "2": "duzentos",
            "3": "trezentos",
            "4": "quatrocentos",
            "5": "quinhentos",
            "6": "seiscentos",
            "7": "setecentos",
            "8": "oitocentos",
            "9": "novecentos",
        }

    def split_numbers(self, number):
        return [i for i in str(number)]

    def signal(self):
        if self.number_list[0] == "-":
            del self.number_list[0]
            return "menos"
        else:
            return ""

    def unit(self, data):
        return self.units.get(data[0])

    def ten(self, data):
        if data[0] == "0":
            return self.unit(data[1])
        elif data[0] == "1":
            return self.tens.get("".join(data))
        else:
            if data[1] == "0":
                return self.tens.get(data[0])
            else:
                return f"{self.tens.get(data[0])} e {self.units.get(data[1])}"

    def hundred(self, data):
        if data[0] == "0":
            return self.ten(data[1:])
        if data[2] == "0" and data[1] == "0":
            return self.hundreds.get(data[0])
        else:
            if data[0] != "1":
                return f"{self.hundreds.get(data[0])} e {self.ten(data[1:])}"
            else:
                return f"cento e {self.ten(data[1:])}"

    def thousand(self, data):
        if data[3] == "0" and data[2] == "0" and data[1] == "0":
            if data[0] == "1":
                return "mil"
            else:
                return f"{self.unit(data[0])} mil"
        else:
            if data[0] == "1":
                return f"mil {self.hundred(data[1:])}"
            else:
                return f"{self.unit(data[0])} mil e {self.hundred(data[1:])}"

    def ten_thousand(self, data):
        if data[4] == "0" and data[3] == "0" and data[2] == "0":
            return f"{self.ten(data[0:2])} mil"
        else:
            return f"{self.ten(data[0:2])} mil e {self.hundred(data[2:])}"

    def convert(self):
        if len(self.number_list) == 1:
            return (f"{self.signal} {self.unit(self.number_list)}").lstrip()

        elif len(self.number_list) == 2:
            return (f"{self.signal} {self.ten(self.number_list)}").lstrip()

        elif len(self.number_list) == 3:
            return (f"{self.signal} {self.hundred(self.number_list)}").lstrip()

        elif len(self.number_list) == 4:
            return (f"{self.signal} {self.thousand(self.number_list)}").lstrip()

        elif len(self.number_list) == 5:
            return (f"{self.signal} {self.ten_thousand(self.number_list)}").lstrip()
        else:
            return "Número fora do intervalo permitido, digite um número entre -99999 a 99999"
