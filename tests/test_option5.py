#test option 5
from src.option5_stack import stack_frame_lines #import stack function

def test_stack_frame_structures():#test the structure of the stack frame is correct
    lines = stack_frame_lines(5, 3)#example values

    assert "bp : RETURN" in lines#check the return address is correct
    assert "bp+2 : a = 5" in lines#check the value of a is correct
    assert "bp+4 : b = 3" in lines#check the value of b is correct

def test_stack_frame_registers():#test that the register values are correct
    lines = stack_frame_lines(5, 3)

    assert "AX = 5" in lines#check the value of AX is correct
    assert "BX = 3" in lines#check the value of BX is correct
    assert "AX (AX+BX) = 8" in lines#check the result of the addition is correct

def test_stack_frame_different_values(): #testing with other numbers to show it also works with different inputs
    lines = stack_frame_lines(2, 4)

    assert "bp+2 : a = 2" in lines#check the value of a is correct
    assert "bp+4 : b = 4" in lines#check the value of b is correct
    assert "AX (AX+BX) = 6" in lines#check the result of the addition is correct