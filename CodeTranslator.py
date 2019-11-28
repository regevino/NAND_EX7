


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

    def translate(self):
        """
        Translate the VM code into HACK machine code.
        :return: A 16-bit byte array representing machine code for HACK.
        """

    def get_instruction_type(self, line):
        """
        Recieves a line of vm code and determines the type of the command.
        :param line: line of code to determine type.
        :return: the type of instruction.
        """

