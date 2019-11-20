import re

from ASMCode import ASMCode


class Parser:

    def __init__(self, filename):
        """
        Create a parser object over a .asm file
        :param filename: Path (absolute or relative) to the .asm file.
        """
        self.__filename = filename

    def parse(self):
        """
        Parse the .asm file, returning an object of type ASMCode that is ready for compilation.
        :return: An ASMCode object for the parsed code, including symbol values if there are any.
        """
        lines = []
        symbols = dict()
        with open(self.__filename, 'r') as file:
            line = file.readline()
            line_index = 0
            while line:
                line = re.sub('\s', '', line)
                comment = line.find('//')
                if comment > 0:
                    line = line[:comment]
                print(line)

                if not line:
                    continue

                if line.startswith('('):
                    pattern = re.compile('\((.+)\)')
                    result = re.match(pattern, line)
                    label = result.group(0)
                    symbols[label] = line_index

                else:
                    lines.append(line)
                    line_index += 1

                line = file.readline()

        return ASMCode(lines, symbols)
