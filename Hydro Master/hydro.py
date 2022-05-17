
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


# Test program
program = [
    push(34),
    push(35),
    plus(),
    dump(),
    push(36),
    dump(),
]


def simulate_program(program):
    stack = [] 
    for op in program:
        assert COUNT_OPERATIONS == 3, "Error: too many operations within program" 
        if op[0] == OPERATION_PUSH:
            stack.append(op[1])
        elif op[0] == OPERATION_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif op[0] == OPERATION_DUMP:
            a = stack.pop()
            print(a)
        else:
            assert False, "Unknown operation" + str(op) 

# compile program
def compile_program(program):
    assert False, "not yet implemented"


program=[
    push(34),
    push(35),
    plus(),
    dump(),
    push("piss"),
    dump(),
]

simulate_program(program)