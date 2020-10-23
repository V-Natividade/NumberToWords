import unittest

from http_server import Server
from number_to_words import NumberToWords


class TesteNumToWords(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(NumberToWords(1).convert(), "um")
        self.assertEqual(NumberToWords(2).convert(), "dois")
        self.assertEqual(NumberToWords(3).convert(), "três")
        self.assertEqual(NumberToWords(4).convert(), "quatro")
        self.assertEqual(NumberToWords(5).convert(), "cinco")
        self.assertEqual(NumberToWords(6).convert(), "seis")
        self.assertEqual(NumberToWords(7).convert(), "sete")
        self.assertEqual(NumberToWords(8).convert(), "oito")
        self.assertEqual(NumberToWords(9).convert(), "nove")

        self.assertEqual(NumberToWords(10).convert(), "dez")
        self.assertEqual(NumberToWords(11).convert(), "onze")
        self.assertEqual(NumberToWords(12).convert(), "doze")
        self.assertEqual(NumberToWords(13).convert(), "treze")
        self.assertEqual(NumberToWords(14).convert(), "catorze")
        self.assertEqual(NumberToWords(15).convert(), "quinze")
        self.assertEqual(NumberToWords(16).convert(), "dezesseis")
        self.assertEqual(NumberToWords(17).convert(), "dezessete")
        self.assertEqual(NumberToWords(18).convert(), "dezoito")
        self.assertEqual(NumberToWords(19).convert(), "dezenove")

        self.assertEqual(NumberToWords(20).convert(), "vinte")
        self.assertEqual(NumberToWords(21).convert(), "vinte e um")
        self.assertEqual(NumberToWords(22).convert(), "vinte e dois")
        self.assertEqual(NumberToWords(35).convert(), "trinta e cinco")
        self.assertEqual(NumberToWords(99).convert(), "noventa e nove")

        self.assertEqual(NumberToWords(100).convert(), "cem")
        self.assertEqual(NumberToWords(101).convert(), "cento e um")
        self.assertEqual(NumberToWords(128).convert(), "cento e vinte e oito")
        self.assertEqual(NumberToWords(713).convert(), "setecentos e treze")

        self.assertEqual(NumberToWords(1000).convert(), "mil")
        self.assertEqual(NumberToWords(1101).convert(), "mil cento e um")
        self.assertEqual(
            NumberToWords(15354).convert(),
            "quinze mil e trezentos e cinquenta e quatro",
        )
        self.assertEqual(
            NumberToWords(67888).convert(),
            "sessenta e sete mil e oitocentos e oitenta e oito",
        )
        self.assertEqual(
            NumberToWords(99999).convert(),
            "noventa e nove mil e novecentos e noventa e nove",
        )
        self.assertEqual(
            NumberToWords(46584).convert(),
            "quarenta e seis mil e quinhentos e oitenta e quatro",
        )

        self.assertEqual(NumberToWords(-1).convert(), "menos um")
        self.assertEqual(NumberToWords(-2).convert(), "menos dois")
        self.assertEqual(NumberToWords(-3).convert(), "menos três")
        self.assertEqual(NumberToWords(-4).convert(), "menos quatro")
        self.assertEqual(NumberToWords(-5).convert(), "menos cinco")
        self.assertEqual(NumberToWords(-6).convert(), "menos seis")
        self.assertEqual(NumberToWords(-7).convert(), "menos sete")
        self.assertEqual(NumberToWords(-8).convert(), "menos oito")
        self.assertEqual(NumberToWords(-9).convert(), "menos nove")

        self.assertEqual(NumberToWords(-10).convert(), "menos dez")
        self.assertEqual(NumberToWords(-11).convert(), "menos onze")
        self.assertEqual(NumberToWords(-12).convert(), "menos doze")
        self.assertEqual(NumberToWords(-13).convert(), "menos treze")
        self.assertEqual(NumberToWords(-14).convert(), "menos catorze")
        self.assertEqual(NumberToWords(-15).convert(), "menos quinze")
        self.assertEqual(NumberToWords(-16).convert(), "menos dezesseis")
        self.assertEqual(NumberToWords(-17).convert(), "menos dezessete")
        self.assertEqual(NumberToWords(-18).convert(), "menos dezoito")
        self.assertEqual(NumberToWords(-19).convert(), "menos dezenove")

        self.assertEqual(NumberToWords(-20).convert(), "menos vinte")
        self.assertEqual(NumberToWords(-21).convert(), "menos vinte e um")
        self.assertEqual(NumberToWords(-22).convert(), "menos vinte e dois")
        self.assertEqual(NumberToWords(-35).convert(), "menos trinta e cinco")
        self.assertEqual(NumberToWords(-99).convert(), "menos noventa e nove")

        self.assertEqual(NumberToWords(-100).convert(), "menos cem")
        self.assertEqual(NumberToWords(-101).convert(), "menos cento e um")
        self.assertEqual(NumberToWords(-128).convert(), "menos cento e vinte e oito")
        self.assertEqual(NumberToWords(-713).convert(), "menos setecentos e treze")

        self.assertEqual(NumberToWords(-1000).convert(), "menos mil")
        self.assertEqual(NumberToWords(-1101).convert(), "menos mil cento e um")
        self.assertEqual(
            NumberToWords(-15354).convert(),
            "menos quinze mil e trezentos e cinquenta e quatro",
        )
        self.assertEqual(
            NumberToWords(-67888).convert(),
            "menos sessenta e sete mil e oitocentos e oitenta e oito",
        )
        self.assertEqual(
            NumberToWords(-99999).convert(),
            "menos noventa e nove mil e novecentos e noventa e nove",
        )
        self.assertEqual(
            NumberToWords(-46584).convert(),
            "menos quarenta e seis mil e quinhentos e oitenta e quatro",
        )
