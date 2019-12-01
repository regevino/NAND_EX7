ARITHMETIC_OPERATIONS = {'add': lambda x: ['M=M+D'], 'sub': lambda x: ['M=M-D'],
                         'neg': lambda x: ['A=A+1', 'M=-M', '@SP', 'M=M+1'],
                         'eq': lambda x: ['D=M-D', '@' + str(x + 9), 'M;JEQ', '@SP', 'A=M-1', 'M=0',
                                          '@' + str(x + 12), '0;JMP', '@SP', 'A=M-1', 'M=-1'],
                         'gt': lambda x: ['D=D-M', '@' + str(x + 9), 'M;JGT', '@SP', 'A=M-1', 'M=0',
                                          '@' + str(x + 12), '0;JMP', '@SP', 'A=M-1', 'M=-1'],
                         'lt': lambda x: ['D=M-D', '@' + str(x + 9), 'M;JGT', '@SP', 'A=M-1', 'M=0',
                                          '@' + str(x + 12), '0;JMP', '@SP', 'A=M-1', 'M=-1'],
                         'and': lambda x: ['M=M&D'],
                         'or': lambda x: ['M=M|D'],
                         'not': lambda x: ['A=A+1', 'M=!M', '@SP', 'M=M+1']}


class CodeTranslator:
    """
    Represents an object that can translate VMCode objects into hack assembly code.
    """

    def __init__(self, parsed_VM_code):
        """
        Create a translator object that can translate a specific VMCode object into HACK assembly code.
        :param parsed_VM_code: An VMCode object.
        """
        self.__VM_code = parsed_VM_code
        filename = self.__VM_code.get_filename()
        self.SEGMENTS = {'argument': lambda x: ['@ARG', 'D=A', '@' + str(x), 'D=D+A', '@R13', 'M=D'],
                         'local': lambda x: ['@LCL', 'D=A', '@' + str(x), 'D=D+A', '@R13', 'M=D'],
                         'static': lambda x: ['@' + filename + '.' + str(x), '@R13', 'M=D'],
                         'constant': lambda x: ['@' + str(x), 'D=A', '@R13', 'M=D'],
                         'this': lambda x: ['@THIS', 'D=A', '@' + str(x), 'D=D+A', '@R13', 'M=D'],
                         'that': lambda x: ['@THAT', 'D=A', '@' + str(x), 'D=D+A', '@R13', 'M=D'],
                         'pointer': lambda x: ['@R3', 'D=A', '@' + str(x), 'D=D+A', '@R13', 'M=D'],
                         'temp': lambda x: ['@R13', 'D=A', '@' + str(x), 'D=D+A', '@R13', 'M=D']}

    def translate(self):
        """
        Translate the VM code into Assembly code.
        :return: An array representing assembly code for HACK.
        """
        lines = []
        for index, line in enumerate(self.__VM_code.get_vm_code()):
            lines += self.translate_instruction(line, index)
            index = len(lines) -1
        return lines

    def translate_instruction(self, line, index):
        """
        Recieves a line of vm code and translates command.
        :param index:
        :param line: line of code to translate.
        :return: the lines of translated assembly code.
        """
        lines = []
        lines.append("//Translating vm command: " + line)
        cmds = line.split()
        if cmds[0] == 'push' or cmds[0] == 'pop':
            lines += self.__memory_access(cmds)
        elif len(cmds) == 1:
            lines += self.__translate_arithmetic(cmds[0], index)
        return lines

    @staticmethod
    def __push():
        lines = []
        lines.append('@R13')
        lines.append("D=M")
        lines.append('@SP')
        lines.append('M=M+1')
        lines.append('A=M-1')
        lines.append('M=D')
        return lines

    @staticmethod
    def __pop():
        lines = []
        lines.append('@SP')
        lines.append('M=M-1')
        lines.append('A=M')
        lines.append('D=M')
        lines.append('@R13')
        lines.append('M=D')
        return lines

    def __arithmetic(self, arithmetic_func, index):
        lines = []
        lines += self.__pop()
        lines.append('@SP')
        lines.append('A=M-1')
        index += len(lines)
        lines += arithmetic_func(index)
        return lines

    def __translate_arithmetic(self, line, index):
        return self.__arithmetic(ARITHMETIC_OPERATIONS[line], index)

    def __memory_access(self, split_line):
        lines = []
        lines += self.__set_address(split_line[1], split_line[2])
        if split_line[0] == 'pop':
            lines += self.__pop()
        elif split_line[0] == 'push':
            lines += self.__push()
        return lines

    def __set_address(self, segment_name, index):
        return self.SEGMENTS[segment_name](index)
