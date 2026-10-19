class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message

def evaluate(input_data):
    output = []
    operations = {
        '+': [lambda x: plus(x)],
        '-': [lambda x: minus(x)],
        '*': [lambda x: times(x)],
        '/': [lambda x: divides(x)],
        'dup': [lambda x: x.append(x[-1])],
        'drop': [lambda x: x.pop()],
        'swap': [lambda x: swap(x)],
        'over': [lambda x: x.append(x[-2])]
    }

    def plus(elements):
        elements.append(elements[-1]+elements[-2])
        elements.pop(-2)
        elements.pop(-2)
        return elements
    
    def minus(elements):
        elements.append(elements[-2]-elements[-1])
        elements.pop(-2)
        elements.pop(-2)
        return elements
    
    def times(elements):
        elements.append(elements[-2]*elements[-1])
        elements.pop(-2)
        elements.pop(-2)
        return elements
    
    def divides(elements):
        if elements[-1] == 0:
            raise ZeroDivisionError("divide by zero")
        elements.append(elements[-2]//elements[-1])
        elements.pop(-2)
        elements.pop(-2)
        return elements
    
    def swap(elements):
        elements[-2], elements[-1] = elements[-1], elements[-2]
        return elements
    
    for line in input_data:
        commands = line.split()
        if commands[0] == ':':
            if commands[1].strip('-').isnumeric():
                raise ValueError("illegal operation")
            operation = []
            for cmd in commands[2:-1]:
                if cmd.strip('-').isnumeric():
                    operation.append(lambda x, n=int(cmd): x.append(n))
                elif cmd.lower() in operations.keys():
                    operation.extend(operations[cmd.lower()])
                else:
                    raise StackUnderflowError("Insufficient number of items in stack")
            operations[commands[1].lower()] = operation
        else:
            for command in commands:
                if command.strip('-').isnumeric():
                    output.append(int(command))
                else:
                    try:
                        if command.lower() in operations.keys():
                            for cmd in operations[command.lower()]:
                                cmd(output)
                        else:
                            raise ValueError("undefined operation")
                    except IndexError:
                        raise StackUnderflowError("Insufficient number of items in stack")
    return output