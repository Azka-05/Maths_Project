#test option 3

from src.programA import ascii_dump_lines

def test_ascii_dump_lines():
    lines,length = ascii_dump_lines("A")

    assert "0x1000 : 0x41" in lines
    assert "0x1001 : 0x00" in lines
    assert length == 1

def test_ascii_dumo_word():
    lines, length = ascii_dump_lines("Hi")

    assert "0x1000 : 0x48" in lines
    assert "0x1001 : 0x69" in lines
    assert length == 2