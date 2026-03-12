#option5_stack.py
# stack frame implementation for option 5


def stack_frame_lines(a, b):
    lines=[] #list used to store each line of output

    #simulate the stack frame layout using base pointer offsets
    lines.append("bp : RETURN") #location of the return address
    lines.append(f"bp+2 : a = {a}") #first parameter stored at bp+2
    lines.append(f"bp+4 : b = {b}") #second parameter stored at bp+4

    #simulate a simple register-style view
    lines.append(f"AX = {a}") #value of a placed into register AX
    lines.append(f"BX = {b}") #value of b placed into register BX

    #simulate a basic CPU operation using the registers
    lines.append(f"AX (AX+BX) = {a+b}") #result of adding AX and BX

    return lines #return all lines so they can be printed by the main program

