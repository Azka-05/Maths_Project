#importing functions from other files
#this helps keep it organised and allows each option to be implemented separately
from src.option5_stack import stack_frame_lines
from src.option4_array import array_addressing
from src.option2_endian import option2_little_endian
from src.option3_ascii import ascii_dump_lines

#function to display the main menu to the user
def show_menu():
    print("\n=================================================\n")

    print("Welcome to the Hex, Memory and Stack Calculator!")
    print("\n=================================================")
    print("Please select an option:")
    print("1) Convert (decimal to hexadecimal and 16-bit binary)")
    print("2) Little-endian pack/unpack (16-bit)")
    print("3) ASCII memory dump")
    print("4) Array addressing")
    print("5) Stack frame")
    print("0) Exit")

#function used in option 1 to convert a number into different representations
def convert(n):
    hex_val = format(n, "X") #convert decimal to hexadecimal
    bin_val = format(n, "016b")#convert decimal to 16-bit binary string

    if n < 32768:
        signed = n 
    else:
        signed = n - 65536 

    return hex_val, bin_val, signed#return the results so they can be printed

def option1():#this function performs option 1 from the menu

    while True:#keep looping until we get valid input
        try:
            n = int(input("Enter a decimal number (0-65535): "))

            if 0 <= n <= 65535:
                break

            else:
                print("Invalid input. Please enter a number between 0 and 65535.")

        except ValueError:
            print("Invalid input. Please enter a number. ")
    
    if 0 <= n <= 65535:
        hex_val, bin_val, signed = convert(n) #call the convert function
        
        print(f"Hexadecimal: {hex_val}")
        print(f"Binary: {bin_val}")
        print(f"Signed Integer: {signed}")
    else:
        print("Invalid input. Please enter a number between 0 and 65535.")

def main():#main program loop
    while True:
        show_menu()

        while True: #validate menu choice
            choice = input("Enter your choice: ") #get users menu choice
            if choice in ('0', '1', '2', '3', '4', '5'):
                break
            else:
                print("Invalid choice. Please enter a number from the menu options.")

        if choice == '1': #option 1 - number conversion
            option1()

        elif choice == '2': #option 2 - little endian packing
            while True: #validate number input
                try:
                    n = int(input("Enter integer n (0-65535): "))
                    if 0 <= n <= 65535:
                        break
                    else:
                        print("Invalid input. Please enter a number between 0 and 65535.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            while True:
                try:
                    addr = int(input("Enter memory address (decimal or hex e.g. 0x2000): "), 0)
                    if addr >= 0:
                        break
                    else:
                        print("Invalid input. Address must be non-negative.")
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

        elif choice == '3': #option 3-ascii memory dump

            while True: #validate string input
                s = input("Enter a string (max 10 characters): ")

                if len(s) == 0:
                    print("Input cannot be empty. Please enter at least one letter. ")
                    continue

                if len(s) > 10:
                    print("Invalid input. Maximum length is 10 characters.")
                    continue
                if not s.isalpha():
                    print("Invalid input. Only letters A-Z are allowed. ")
                    continue

                break
    
            lines,length = ascii_dump_lines(s) #call the ascii dump function

            for line in lines:#print the memory dump
                print(line)

            print(f"Length (until 0x00) {length}") #display the calculated length

        elif choice == '4': #option 4 - array addressing 
            try: #get base address and index
                base = int(input("Base address: "))
                index = int(input("Index: "))
            except ValueError:
                print("Invalid input. ")
                return

            while True: #validate element size
                try:
                    size = int(input("Element size (1 or 2): "))
                    if size in (1, 2):
                        break
                    else:
                        print("Invalid input. Please enter 1 or 2.")
                except ValueError:
                    print("Invalid input. Please enter 1 or 2.")

            while True:#validate mode
                mode = input("Mode (read/write): ").lower()
                if mode in ("read", "write"):
                    break
                else:
                    print("Invalid input. Please enter 'read' or 'write'.")

            if mode == "write": #perform memory operation
                value = int(input("Value:"))
                array_addressing(base, index, size, mode, value)
            else:
                array_addressing(base, index, size, mode)

        elif choice == '5': #option 5 stack frame

            while True: #validate number of local variables
                try:
                    a = int(input("Enter value for a: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number. ")

            while True:
                try: 
                    b = int(input("Enter value for b: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number. ")
            
            lines = stack_frame_lines(a, b) #call the stack frame function
            for line in lines: #print the stack frame
                print(line)

        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break

        else:
            
            print()

if __name__ == "__main__": #ensures the program runs when it is executed directly
    main()




