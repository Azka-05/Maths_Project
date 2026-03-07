# programA.py – Main menu only
# Each option's logic lives in its own file (done by each group member)

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