def show_menu():
    print("Welcome to the Maths Converter!")
    print("Please select an option:")
    print("1) Convert Decimal to Hexadecimal (16-bit)")
    print("2) Little-endian pack/unpack (16-bit)")
    print("3) ASCII memory dump")
    print("4) Array addressing")
    print("5) Stack frame")
    print("0) Exit")

#def convert(n):

#def ascii
def ascii_dump_lines(s, base=0x1000):
    if len(s) > 10:
        raise ValueError("String must be at most 10 characters")
    memory = {}

    for i, ch in enumerate(s):
        address = base + i
        ascii_value = ord(ch)
        memory[address] = ascii_value

    null_address = base + len(s) 
    memory[null_address] = 0   

    line = []

    for address in range(base, base + len(s) + 1)
        value = memory[address]
        formatted_line = f"0x{address:04x} : 0x{value:02X}"
        lines.append(formatted_line)

    length = 0
    current_address = base

    while memory[current_address] != 0:
        length += 1 
        current_address +=1

    return lines, length        







