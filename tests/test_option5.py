#test option 5
from src.option5_stack import stack_frame_lines

def test_stack_frame_structures():
    lines = stack_frame_lines(5, 3)

    assert "bp : RETURN" in lines
    assert "bp+2 : a = 5" in lines
    assert "bp+4 : b = 3" in lines

def test_stack_frame_registers():
    lines = stack_frame_lines(5, 3)

    assert "AX = 5" in lines
    assert "BX = 3" in lines
    assert "AX (AX+BX) = 8" in lines

def test_stack_frame_different_values(): #testing with other numbers to show it also works with different inputs
    lines = stack_frame_lines(2, 4)

    assert "bp+2 : a = 2" in lines
    assert "bp+4 : b = 4" in lines
    assert "AX (AX+BX) = 6" in lines