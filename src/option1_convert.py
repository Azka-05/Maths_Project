# conversion from decimal to hex and binary

def decimal_to_hex_16bit():
    try:
        num = int(input("Enter a decimal number (0 - 65535): "))

        if num < 0 or num > 65535:
            print("Number out of range for 16-bit unsigned integer.")
            return

        hex_value = format(num, '04X')
        print("Hexadecimal (16-bit):", hex_value)

    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")