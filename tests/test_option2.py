#test option 2

from src.programA import option2_little_endian

def test_option2_little_endian():
    result = option2_little_endian(258, 100)

    assert result["low"] == 2
    assert result["high"] == 1
    assert result["unpacked"] == 258