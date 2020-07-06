"""This file contains the parser test"""
from app.program.parser import Parser

question = Parser("Salut Grandpy, ca va?? Est-ce que tu sais où se trouve le Louvre?????")


class TestParser:

    def test_parse(self):
        result = question.parse()
        assert result == "louvre"
