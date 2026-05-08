#Simple assembler made for my CPU design. It reads assembly instructions from a text file and converts them into binary opcodes. The opcodes are defined in a dictionary, and the assembler handles unknown opcodes gracefully by printing an error message.
opdata = {
    "LOADA": "0000",
    "LOADB": "0001",
    "MOVAB": "0010",
    "MOVBA": "0011",
    "ADD": "0100",
    "SUB": "0101",
    "AND": "0110",
    "OR": "0111",
}

with open("assembler.txt", "a") as f:
    #this part is used jsut in case a file isjnt created (really smart ik ill fixx it later ngas)
    pass

with open("assembler.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        opcode = line.split(" ")[0]
        operand = line.split(" ")[1]
        try:
            opcode_bin = opdata[opcode]
            print(opcode_bin, operand)
        except KeyError:
            print(f"Unknown opcode: {opcode}")  