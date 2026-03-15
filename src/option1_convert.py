# option1_convert.py
# conversion from decimal to hex and binary

#this function converts a decimal number into hexadecimal.
def decimal_to_hex_16bit(n):
    # format(n, '04X') is used to convert the decimal number into 4 digit hexadecimal.
    hex_val = format(n, '04X')
    bin_val = format(n, '016b')  # format(n, '016b') is used to convert the decimal number into 16 digit binary.   
 
    if n < 32768: # check if the number is out of range for 16-bit unsigned integer
        signed = n # if the number is out of range, we can keep it as is for signed representation
    else:
        signed = n - 65536  # convert to negative signed value
    return hex_val, bin_val, signed #return all values