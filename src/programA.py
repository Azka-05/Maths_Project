from option5_stack import option5
from option4_array import array_addressing



def convert(n):
    hex_val = format(n, "X")
    bin_val = format(n, "016b")

    if n < 32768:
        signed = n 
    else:
        signed = n - 65536 #these values represent the binary in 16bit, highest and lowesst

    return hex_val, bin_val, signed

def option1():
    n = int(input("Enter a decimal number (0-65535): "))
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
        elif choice == '4':

            base = int(input("Base address: "))
            index = int(input("Index: "))
            size = int(input("Element size (1 or 2): "))
            mode = input("Mode (read/write): ")
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
            print("Invalid choice. Please try again.")

def show_menu():
    print("Welcome to the Maths Converter!")
    print("Please select an option:")
    print("1) Convert Decimal to Hexadecimal (16-bit)")
    print("2) Little-endian pack/unpack (16-bit)")
    print("3) ASCII memory dump")
    print("4) Array addressing")
    print("5) Stack frame")
    print("0) Exit")


if __name__ == "__main__":
    main()




