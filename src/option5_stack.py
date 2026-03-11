#stack

def stack_frame_lines(a, b):
    lines=[]
    lines.append("bp : RETURN")
    lines.append(f"bp+2 : a = {a}")
    lines.append(f"bp+4 : b = {b}")
    lines.append(f"AX = {a}")
    lines.append(f"BX = {b}")
    lines.append(f"AX (AX+BX) = {a+b}")
    return lines

