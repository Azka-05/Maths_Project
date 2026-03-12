# option4_array.py
# array addressing calculations and simple memory read/write

memory = {} #to store values at addresses for read/write operations

def element_address(base, index, size): #calculate address of array element
    return base + index * size #returns the calclated address 


def memory_write(addr, value):#writes a value to the specified address 
    memory[addr] = value


def memory_read(addr):# reads value from memory address
    return memory.get(addr, 0) #if address has no value it retrurns 0


def array_addressing(base, index, size, mode, value=None): #calculates address of an array element
    address = element_address(base, index, size)
    print(f"ADDRESS = base+ index*size = {address}") #displays the address calculation

    if mode == "write":   # checks if the operation is write
        memory_write(address, value)#writes value to memory
        print(f"WRITE size={size} value={value} to ADDRESS {hex(address)}")

    elif mode == "read": #checks if the operation is read
        val = memory_read(address) #reads value from memory
        print(f"READ size={size} from ADDRESS {hex(address)} = {val}")