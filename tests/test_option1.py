#test for option 1
from src.programA import convert

def test_convert():
    hex_val, bin_val, signed = convert(10)
    assert hex_val == "A"
    assert bin_val == "0000000000001010"
    assert signed == 10

def test_convert_signed():
    hex_val, bin_val, signed = convert(65535)
    assert hex_val == "FFFF"
    assert bin_val == "1111111111111111"
    assert signed == -1