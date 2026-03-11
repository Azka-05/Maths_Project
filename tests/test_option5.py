#test option 5
from src.option5_stack import stack_frame_lines

def test_stack_frame_structures():
    lines = stack_frame_lines(5, 3)

    assert "bp : RETURN" in lines
    assert "bp+2 : a = 5" in lines
    assert "bp+4 : b = 3" in lines

def test_stack_frame_registers():
    lines= stack_frame_lines(5, 3)

    assert "AX = 5" in lines
    assert "BX = 3" in lines
    assert "AX (AX+BX) = 8" in lines