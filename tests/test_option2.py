#test option 2

from src.programA import option2_little_endian #import function for option 2

def test_option2_little_endian(): #testing the little-endian packing function
    result = option2_little_endian(258, 100) #using number 258

    assert result["low"] == 2#check the low byte is correct 
    assert result["high"] == 1#check the high byte is correct
    assert result["unpacked"] == 258#check the unpacked value is correct