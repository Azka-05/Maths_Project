#this if for little endian pack 

# rough toy memory model for now

memory = {} # address (int) -> byte (0..255)


def memory_write(addr: int, byte: int) -> None:
     """Write a single byte to memory."""
     if not (0 <= byte <= 255):
        raise ValueError("Byte must be between 0 and 255")
        memory[addr] = byte


def memory_read(addr: int) -> int:
    """Read a single byte from memory."""
    return memory.get(addr, 0)



# little-endian helpers

def pack_u16_le(n: int) -> tuple[int, int]:
    """Pack a 16-bit unsigned integer into low/high bytes (little-endian)."""
    if not (0 <= n <= 65535):
        raise ValueError("n must be between 0 and 65535")

    low = n & 0xFF
    high = (n >> 8) & 0xFF
    return low, high


def unpack_u16_le(low: int, high: int) -> int:
    """Unpack low/high bytes into a 16-bit unsigned integer."""
    if not (0 <= low <= 255 and 0 <= high <= 255):
        raise ValueError("Bytes must be between 0 and 255")

    return low + (high << 8)



# the core logic in option 2

def option2_little_endian(n: int, addr: int) -> dict:
    """
    Peform little-endian pack/unpack and memory write/read.
    Returns a dictionary of results for printign or testing.
    """

    low, high = pack_u16_le(n)

    # writing to memory
    memory_write(addr, low)
    memory_write(addr + 1, high)

    # reading back
    read_low = memory_read(addr)
    read_high = memory_read(addr + 1)

    unpacked = unpack_u16_le(read_low, read_high)

    return{
        "low": low,
        "high": high,
        "unpacked": unpacked,
        "addr": addr,
        "read_low": read_low,
        "read_high": read_high,
    }
