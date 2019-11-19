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
                        Defaults to None #TODO: Maybe change this to builtin hack symbols
        """
        self.__asm_code = asm_code
        self.__symbols = symbols
        self.__next_free_address = 16

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


