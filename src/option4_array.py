# option4_array.py
# Array Addressing + Dereference

# simple toy memory
memory = {}

def element_address(base, index, size):
    """
    Calculate address using:
    base + index * size
    """
    return base + index * size


def memory_write(addr, value):
    memory[addr] = value


def memory_read(addr):
    return memory.get(addr, 0)


def array_addressing(base, index, size, mode, value=None):

    address = element_address(base, index, size)
    print(f"ADDRESS = base+ index*size = {address}")

    if mode == "write":   # lowercase
        memory_write(address, value)
        print(f"WRITE size={size} value={value} to ADDRESS {hex(address)}")

    elif mode == "read":
        val = memory_read(address)
        print(f"READ size={size} from ADDRESS {hex(address)} = {val}")