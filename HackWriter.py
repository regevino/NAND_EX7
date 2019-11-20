class HackWriter:
    """
    Writes HACK machine language code into a .hack file with a given name.
    """

    def __init__(self, code, filename):
        """
        Create a HackWriter object for some byte code.
        :param code: A 16-bit byte array containing Hack machine language code.
        :param filename: Path to a .hack out file. If it exists, it will be overwritten. If not, it will be
                         created.
        """
        self.__filename = filename
        self.__code = code

    def write_out(self):
        """
        Write the byte-code out into the .hack file.
        """
        with open(self.__filename, 'w') as file:
            for line in self.__code:
                file.writelines(line + '\n')
