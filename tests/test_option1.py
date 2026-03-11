#test for option 1
from src.programA import convert #importing the conver function from the main program to test it

def test_convert(): #testing a decimal conversion
    hex_val, bin_val, signed = convert(10) #convert 10
    assert hex_val == "A" #check the hexadecimal value is correct
    assert bin_val == "0000000000001010" #check the binary value is correct
    assert signed == 10 #check the signed value is correct

def test_convert_signed(): #testing 16-bit signed conversion
    hex_val, bin_val, signed = convert(65535) #convert 65535 (maximum bit value)
    assert hex_val == "FFFF" #check the hexadecimal value is correct
    assert bin_val == "1111111111111111" #check the binary value is correct
    assert signed == -1 #check if signed value is correct

def test_binary_length(): #testing the binary output is always 16 bits long
    hex_val, bin_val, signed = convert(5) #convert 5
    assert len(bin_val) == 16 #check the binary string is 16 characters long

def test_signed_32768(): #testing the signed value of 32768 (first value that is negative in 16-bit signed)
    hex_val, bin_val, signed = convert(32768) #convert 32768
    assert signed == -32768 #check the signed value is correct