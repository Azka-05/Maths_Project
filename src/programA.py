# programA.py – Main menu only
# Each option's logic lives in its own file (done by each group member)
from option5_stack import option5

def convert(n):
    hex_val = format(n, "X")
    bin_val = format(n, "016b")

from option1_convert import option1
from option2_endian import option2
from option3_ascii import option3
from option4_array import option4
from option5_stack import option5

def show_menu():
    print("\nWelcome to the Maths Converter!")
    print("Please select an option:")
    print("1) Convert (decimal -> hex and 16-bit binary)")
    print("2) Little-endian pack/unpack (16-bit)")
    print("3) ASCII memory dump")
    print("4) Array addressing")
    print("5) Stack frame (bp offsets)")
    print("0) Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            option4()
        elif choice == '5':
            option5()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
def show_menu():
    print("Welcome to the Maths Converter!")
    print("Please select an option:")
    print("1) Convert Decimal to Hexadecimal (16-bit)")
    print("2) Little-endian pack/unpack (16-bit)")
    print("3) ASCII memory dump")
    print("4) Array addressing")
    print("5) Stack frame")
    print("0) Exit")

<<<<<<< HEAD
#def convert(n):

#def ascii
def ascii_dump_lines(s, base=0x1000):
    if len(s) > 10:
        raise ValueError("String must be at most 10 characters")
    memory = {}

    for i, ch in enumerate(s):
        address = base + i
        ascii_value = ord(ch)
        memory[address] = ascii_value

    null_address = base + len(s) 
    memory[null_address] = 0   

    line = []

    for address in range(base, base + len(s) + 1)
        value = memory[address]
        formatted_line = f"0x{address:04x} : 0x{value:02X}"
        lines.append(formatted_line)

    length = 0
    current_address = base

    while memory[current_address] != 0:
        length += 1 
        current_address +=1

    return lines, length        



=======

if __name__ == "__main__":
    main()
>>>>>>> feb6e62d48b8249a4f8bb7c17837cd8722c03842




