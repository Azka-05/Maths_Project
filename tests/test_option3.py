#test option 3

from src.programA import ascii_dump_lines #import ascii dumo function

def test_ascii_dump_lines():#test ascii conversion of a single character
    lines,length = ascii_dump_lines("A") #convert the string A

    assert "0x1000 : 0x41" in lines#check the ascii value of A is correct
    assert "0x1001 : 0x00" in lines#check the null terminator is correct
    assert length == 1#check the length is correct 

def test_ascii_dump_word():#test ascii conversion of a word
    lines, length = ascii_dump_lines("Hi") #convert the string Hi

    assert "0x1000 : 0x48" in lines#check the ascii value of H is correct
    assert "0x1001 : 0x69" in lines#check the ascii value of i is correct
    assert length == 2#check the length is correct