from option5_stack import option5
from option4_array import array_addressing
from option2_endian import option2_little_endian
from option3_ascii import ascii_dump_lines


def show_menu():
    print("\n=================================================")
    print("Welcome to the Hex, Memory and Stack Calculator!")
    print("\n=================================================")
    print("Please select an option:")
    print("1) Convert (decimal to hexadecimal and 16-bit binary)")
    print("2) Little-endian pack/unpack (16-bit)")
    print("3) ASCII memory dump")
    print("4) Array addressing")
    print("5) Stack frame")
    print("0) Exit")

def convert(n):
    hex_val = format(n, "X")
    bin_val = format(n, "016b")

    if n < 32768:
        signed = n 
    else:
        signed = n - 65536 

    return hex_val, bin_val, signed

def option1():
    try:
        n = int(input("Enter a decimal number (0-65535): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 <= n <= 65535:
        hex_val, bin_val, signed = convert(n)
        
        print(f"Hexadecimal: {hex_val}")
        print(f"Binary: {bin_val}")
        print(f"Signed Integer: {signed}")
    else:
        print("Invalid input. Please enter a number between 0 and 65535.")

def main():
    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            option1()

        elif choice == '2':

            # repeatedly asking for n until user enters a valid 16-bit number
            while True:
                try:
                    n = int(input("Enter integer n (0-65535): "))

                    # checking that the number is within the allowed 16-bit range
                    if 0 <= n <= 65535:
                        break # validating input in order to move on
                    else:
                        print("Please enter a number between 0 and 65535.")

                # happens if user types something that isn't a number
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # now asking for the memory address
            # also accepts hexadecimal like 0x2000
            while True:
                try:
                    addr = int(input("Enter memory address (decimal or hex e.g. 0x2000: ) "), 0)
                    break

                except ValueError:
                    print("Invalid address. Try again.")
                
            # calling the function that performs the little-endian packing
            result = option2_little_endian(n, addr)

            # displaying the results so the user can see how the number was split into bytes
            print(f"LOW BYTE = {result['low']}")
            print(f"HIGH BYTE = {result['high']}")
            print(f"UNPACKED = {result['unpacked']}")

            # showing how the bytes were written into memory
            print(f"MEM[{hex(result['addr'])}] = 0x{result['low']:02X}")
            print(f"MEM[{hex(result['addr']+1)}] = 0x{result['high']:02X}")

            # reading the same memory back to prove the value can be reconstructed
            print(f"READ MEM[{hex(result['addr'])}] = 0x{result['read_low']:02X}")
            print(f"READ MEM[{hex(result['addr']+1)}] = 0x{result['read_high']:02X}")

        elif choice == '3':
            s = input("Enter a string (max 10 characters): ")

            try:
                lines,length = ascii_dump_lines(s)

                for line in lines:
                    print(line)

                print(f"Length (until 0x00) {length}")

            except ValueError as e:
                print(e)    

        elif choice == '4': 
            try:
                base = int(input("Base address: "))
                index = int(input("Index: "))
                size = int(input("Element size (1 or 2): "))
                mode = input("Mode (read/write): ") 
            except ValueError:
                print("Invalid input.")
                continue

            if mode == "write":
                value = int(input("Value:"))
                array_addressing(base, index, size, mode, value)
            else:
                array_addressing(base, index, size, mode)

        elif choice == '5':
            option5()

        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break

        else:
            
            print()

if __name__ == "__main__":
    main()




