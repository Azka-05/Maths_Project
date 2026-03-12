# option1_convert.py
# conversion from decimal to hex and binary

#this function converts a decimal number into hexadecimal.
def decimal_to_hex_16bit():  
    try:
        # Ask the user to enter a decimal number between 0 and 65535.
        num = int(input("Enter a decimal number (0 - 65535): "))

        # Check if the number is outside the valid range for a 16-bit unsigned integer.
        if num < 0 or num > 65535:
            print("Number out of range for 16-bit unsigned integer.")
            return

        # converts a decimal number into hexadecimal.
        # format(num, '04X') is used to convert the decimal number into 4 digit hexadecimal. 
        hex_value = format(num, '04X')
        #prints the hexidecimals. 
        print("Hexadecimal (16-bit):", hex_value)

    # if user enters something that isnt a number then then this error message will print.
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")