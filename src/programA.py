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

            try:
                n = int(input("Enter integer n (0-65535): "))
                addr = int(input("Enter memory address: "))
            except ValueError:
                print("Invalid input.")
                continue
            result = option2_little_endian(n, addr)

            print(f"Low Byte: {result['low']}")
            print(f"High Byte: {result['high']}")
            print(f"Unpacked: {result['unpacked']}")
            print(f"Memory[{hex(result['addr'])}] = 0x{result['low']:02X}")
            print(f"Memory[{hex(result['addr']+1)}] = 0x{result['high']:02X}")
            print(f"Read memory[{hex(result['addr'])}] = 0x{result['read_low']:02X}")
            print(f"Read memory[{hex(result['addr']+1)}] = 0x{result['read_high']:02X}")

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
            print("Invalid choice. Please enter 0-5.")

        print()

if __name__ == "__main__":
        main()




