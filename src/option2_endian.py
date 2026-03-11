#option2_endian.py
# this file contains the logic for option 2 in the menu
# little-endian packing/unpacking and simple memory storage

# simple memory structure using a dictionary
# key = memory address
# value = stored byte (0-255)
memory = {} 


def memory_write(addr: int, byte: int) -> None:
     """Write a single byte to memory."""

     # checking the address is a valid integer and not negative
     if not isinstance(addr, int):
        raise ValueError("Address must be an integer")
     if addr < 0:
        raise ValueError("Address must be non-negative")

    # ensuring value to store fits inside one byte (8 bits)
     if not isinstance(byte, int):
        raise ValueError("Byte must be an integer")
     if not (0 <= byte <= 255):
        raise ValueError("Byte must be between 0 and 255")

    # storing byte at given address in simulated memory
     memory[addr] = byte


def memory_read(addr: int) -> int:
    """Read a single byte from memory. Returns 0 if address is empty"""

    # validating address before reading
    if not isinstance(addr, int):
        raise ValueError("Address must be an integer")
    if addr < 0:
        raise ValueError("Address must be non-negative")
    
    # if address has not been written yet then return 0
    return memory.get(addr, 0)



# little-endian helper functions

def pack_u16_le(n: int) -> tuple[int, int]:
    """Pack a 16-bit unsigned integer into low and high bytes using little-endian order."""

    # making sure number is a valid 16-bit unsigned integer
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if not (0 <= n <= 65535):
        raise ValueError("n must be between 0 and 65535")

    # & 0xFF is extracting the lowest 8 bits (the least significant byte)
    low = n & 0xFF

    # shifting the number right by 8 bits to get the high byte into position
    high = (n >> 8) & 0xFF
    return low, high


def unpack_u16_le(low: int, high: int) -> int:
    """Rebuild a 16-bit unsigned integer from low and high bytes usign little-endian order."""

    # validating both bytes
    if not isinstance(low, int) or not isinstance(high, int):
        raise ValueError("Bytes must be integers")
    if not (0 <= low <= 255 and 0 <= high <= 255):
        raise ValueError("Bytes must be between 0 and 255")

    # reconstructing the original number
    # high byte is shifted left and then combined together with the low byte
    return (high << 8) | low



# the main logic used by menu Option 2

def option2_little_endian(n: int, addr: int) -> dict:
    """
    Perform little-endian pack/unpack and memory write/read.

    Input: 
    n -> 16-bit unsigned integer (0..65535)
    addr -> memory address (integer)

    Returns 
    a dictionary containing the values used during the process.
    """

    # validating the address
    if not isinstance(addr, int):
        raise ValueError("Address must be an integer")
    if addr < 0:
        raise ValueError("Address must be non-negative")

    # step 1- first splitting the number into low and high bytes
    low, high = pack_u16_le(n)

    # step 2- then writing bytes into memory
    # in little-endian the low byte is stored first
    memory_write(addr, low)
    memory_write(addr + 1, high)

    # step 3- reading the values back from memory
    read_low = memory_read(addr)
    read_high = memory_read(addr + 1)

    # step 4- rebuilding the original number from the bytes
    unpacked = unpack_u16_le(read_low, read_high)

    # returning all values so the main program is able to print them
    return {
        "low": low,
        "high": high,
        "unpacked": unpacked,
        "addr": addr,
        "read_low": read_low,
        "read_high": read_high,
    }
