import re

from VMCode import VMCode


class Parser:

    def __init__(self, filename):
        """
        Create a parser object over a .vm file
        :param filename: Path (absolute or relative) to the .vm file.
        """
        self.__filename = filename

    def parse(self):
        """
        Parse the .vm file, returning an object of type VMCode that is ready for compilation.
        :return: An VMCode object for the parsed code, including symbol values if there are any.
        """
        lines = []
        with open(self.__filename, 'r') as file:
            line = file.readline()
            while line:

                # Erase all leading and trailing white spaces:
                line = line.strip()

                # Find and erase comments:
                comment = line.find('//')
                if comment >= 0:
                    line = line[:comment]

                if not line:
                    line = file.readline()
                    continue

                # # Find and add label to label dictionary:
                # if line.startswith('('):
                #     pattern = re.compile('\((.+)\)')
                #     result = re.match(pattern, line)
                #     label = result.group(1)
                #     symbols[label] = line_index

                # Regular instruction - add to list of instructions:

                lines.append(line)
                line = file.readline()

        return VMCode(lines, file)
