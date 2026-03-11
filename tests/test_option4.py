#test option 4

from src.option4_array import element_address #import function for option 4

def test_array_address(): #test the address calculation works correctly
    assert element_address(1000, 3, 2) == 1006 #check the address is correct for element size 2

def test_array_address_size1(): #test the address calculation works correctly for element size 1
    assert element_address(2000, 4, 1) == 2004 #check the address is correct for element size 1