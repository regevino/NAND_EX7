DEFAULT_ASM_LABELS = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576}
DEFAULT_ASM_LABELS.update({'R{}'.format(i): i for i in range(16)})


class ASMCode:
    """
    Represents parsed assembly code ready for translation, and holds all the symbol info (i.e labels and
    variable names).
    """

    def __init__(self, asm_code, symbols=None):
        """
        Creates an ASMCode object with some lines of code and some (optional) symbol information.
        :param asm_code: A list of strings, each containing a line of assembly code, with no whitespaces and
                         no label decelerations.
        :param symbols: A dictionary containing symbol values.
                        Defaults to Default Hack assembly labels.
        """
        self.__asm_code = asm_code
        symbols.update(DEFAULT_ASM_LABELS)
        self.__symbols = symbols
        self.__next_free_address = 16

    def get_asm_code(self):
        """
        Returns this object's list of assembly code lines
        :return: this object's list of assembly code lines
        """
        return self.__asm_code

    def get_symbol_value(self, symbol):
        """
        Get the value for an assembly symbol. If it's a variable that is being declared, register it's value
        and return it.
        :param symbol: The symbol to query.
        :return: The symbol's address value in 16 bits
        """
        if not self.__symbols:
            raise NotImplementedError("Symbol parsing not yet implemented!")
        if symbol in self.__symbols:
            return self.__symbols[symbol]
        else:
            return self.__register_symbol(symbol)

    def __register_symbol(self, symbol):
        """
        Register a new variable name and return it's allocated address in 16 bits
        :param symbol: The new variable name.
        :return: The variable's address.
        """
        address = self.__next_free_address
        self.__symbols[symbol] = address
        self.__next_free_address += 1
        return address
