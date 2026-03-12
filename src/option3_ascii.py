#option 3 : ascii memory dump with null terminator and length scan

def ascii_dump_lines(s, base=0x1000):
    #makes sure the string is not longer than 10 characters
    if len(s) > 10:
        raise ValueError("String must be at most 10 characters")
    memory = {}

    #stores the characters as ASCII values in memeory
    for i, ch in enumerate(s):
        address = base + i
        ascii_value = ord(ch)
        memory[address] = ascii_value

    #adds null terminator (0x00)
    null_address = base + len(s) 
    memory[null_address] = 0   

    lines = []

    #create formatted memory dump
    for address in range(base, base + len(s) + 1):
        value = memory[address]
        formatted_line = f"0x{address:04X} : 0x{value:02X}"
        lines.append(formatted_line)

    #scan memory until the terinator to check length
    length = 0
    current_address = base

    while memory[current_address] != 0:
        length += 1 
        current_address +=1

    return lines, length        



 