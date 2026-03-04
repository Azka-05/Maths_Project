#stack

def stack_frame_lines(a, b):
    lines=[]
    lines.append("bp : RETURN")
    lines.append(f"bp+2 : a = {a}")
    lines.append(f"bp+4 : b = {b}")
    lines.append(f"AX = {a}")
    lines.append(f"BX = {b}")
    lines.append(f"AX (AX+X) = {a+b}")
    return lines

def option5():
    try:
        a = int(input("Enter first integer (a): "))
        b = int(input("Enter second integer (b): "))

        lines = stack_frame_lines(a,b)

        for line in lines:
            print(line)
    except ValueError:
        print("Invalid input. Please enter integers only.")
