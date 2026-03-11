#test option 2

from src.programA import option2_little_endian #import function for option 2

def test_pack_zero(): #testing packing the number 0
    result = option2_little_endian(0, 100) #using number 0
    assert result["unpacked"] == 0#check the unpacked value is correct

def test_pack_one(): #testing packing the number 1
    result = option2_little_endian(1, 100) #using number 1
    assert result["unpacked"] == 1#check the unpacked value is correct

def test_pack_255(): #testing packing the number 255 (maximum value for a byte)
    result = option2_little_endian(255, 100) #using number 255
    assert result["unpacked"] == 255#check the unpacked value is correct

def test_pack_256(): #testing packing the number 256 (first value that requires two bytes)
    result = option2_little_endian(256, 100) #using number 256
    assert result["unpacked"] == 256#check the unpacked value is correct

def test_pack_max(): #testing packing the number 65535 (maximum value for two bytes)
    result = option2_little_endian(65535, 100) #using number 65535
    assert result["unpacked"] == 65535#check the unpacked value is correct


def test_memory_write_read(): #testing that the value is correctly written to and read from memory
    result = option2_little_endian(258, 200) #using number 258
    assert result["read_low"] == result["low"]#check the low byte read from memory is correct
    assert result["read_high"] == result["high"]#check the high byte read from memory is correct
