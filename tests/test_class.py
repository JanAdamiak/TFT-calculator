import pytest
import json

from calc_synergies import SynergyCalculator


class TestBoardCorrectness:
    def test_correct_board(self, correct_board):
        SynergyCalculator(correct_board)

    def test_incorrect_board(self, incorrect_board):
        with pytest.raises(BaseException):
            SynergyCalculator(incorrect_board)

    def test_duplicate_boards(self, duplicate_board):
        calc = SynergyCalculator(duplicate_board)
        assert len(calc.units) == 2


class TestDragonUnit:
    def test_not_dragon_board(self, correct_board):
        calc = SynergyCalculator(correct_board)
        assert not calc.dragon_unit

    def test_dragon_board(self, dragon_board):
        calc = SynergyCalculator(dragon_board)
        assert calc.dragon_unit


# class TestSynergies:
