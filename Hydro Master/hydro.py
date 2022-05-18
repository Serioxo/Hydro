import sys
import subprocess

enum_counter =0
def enum(reset=False):
    if reset:
        global enum_counter
        enum_counter = 0
    result = enum_counter
    enum_counter +=1
    return result

#interpreter
OPERATION_PUSH = enum(True) # 0
OPERATION_PLUS = enum() # 1
OPERATION_DUMP = enum() # 2
OPERATION_MINUS = enum() # 3
COUNT_OPERATIONS = enum() # 4

# Push a value onto the stack
def push(x):
    return (OPERATION_PUSH, x)
def plus():
    return (OPERATION_PLUS, None)
def dump():
    return (OPERATION_DUMP, None)
def minus():
    return (OPERATION_MINUS, None)



def simulate_program(program):
    stack = [] 
    for op in program:
        assert COUNT_OPERATIONS == 4, "Error: too many operations within program" 
        if op[0] == OPERATION_PUSH:
            stack.append(op[1])
        elif op[0] == OPERATION_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif op[0] == OPERATION_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif op[0] == OPERATION_DUMP:
            a = stack.pop()
            print(a)
        else:
            assert False, "Unknown operation" + str(op) 

# compile program
def compile_program(program, outfile_path):

    with open(outfile_path, "w") as out:
        out.write("section .text\n")
        out.write("global _WinMain@16\n")
        out.write("_WinMain@16:\n")
        for op in program:
            if op[0] == OPERATION_PUSH:
                out.write("     push dword {}\n".format(op[1]))
            elif op[0] == OPERATION_PLUS:
                out.write("     pop eax\n")
                out.write("     pop ebx\n")
                out.write("     add eax, ebx\n")
                out.write("     push eax\n")
            elif op[0] == OPERATION_MINUS:
                out.write("     pop eax\n")
                out.write("     pop ebx\n")
                out.write("     sub eax, ebx\n")
                out.write("     push eax\n")
            elif op[0] == OPERATION_DUMP:
                out.write("     pop eax\n")
                out.write("     mov ebx, eax\n")
                out.write("     call _printf@4\n")
            else:
                assert False, "Unknown operation" + str(op)
        out.write("")
        out.write("     mov eax, 0\n")
        out.write("     mov ret, 16\n")
        out.write("     syscall\n")
    assert False, "not yet implemented"



program=[
    push(34),
    push(35),
    plus(),
    dump(),
    push(360),
    push(400),
    minus(),
    dump(),
]

def usage():
    print("Usage: python3 hydro.py <SUBCOMMANDS> [ARGUMENTS]")
    print("Subcommands:")
    print("  comp <program> to compile a program")
    print("  sim <program> to simulate a program")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        print("ERROR: no subcommand given")
        exit(1)
    subcommand = sys.argv[1]
    if subcommand == "com":
        # compile program and generate assembly file for compilation
        print(compile_program(program, "asmOUTPUT.asm"))
        subprocess.call(["nasm", "-fwin32", "asmOUTPUT.asm"])
        subprocess.call(["ld", "asmOUTPUT.o", "-o", "asmOUTPUT.exe"])

    elif subcommand == "sim":
        simulate_program(program)
    else:
        usage()
        print("Unknown subcommand: " + subcommand)
        sys.exit(1)
        

simulate_program(program)