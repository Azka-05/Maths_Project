# conversion from decimal to hex and binary

# option 1 conversion logic

def decimal_to_hex_16bit(n):

    hex_val = format(n, "X")
    bin_val = format(n, "016b")

    if n < 32768:
        signed = n
    else:
        signed = n - 65536

    return hex_val, bin_val, signed