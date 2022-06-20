import pytest


@pytest.fixture(scope='session')
def correct_board():
    return ("Aatrox", "Ashe")

@pytest.fixture(scope='session')
def incorrect_board():
    return ("Aatrox", "Ashe", "Jan")

@pytest.fixture(scope='session')
def dragon_board():
    return ("Aatrox", "Ashe", "Aurelion Sol")

@pytest.fixture(scope='session')
def duplicate_board():
    return ("Aatrox", "Aatrox", "Ashe")