import os
import sys

from CodeTranslator import CodeTranslator
from HackWriter import HackWriter
from Parser import Parser

if __name__ == '__main__':
    if len(sys.argv) != 2 or os.path.exists(sys.argv[1]):
        exit(1)
    asm_file_path = sys.argv[1]

    files_list = [asm_file_path]

    if os.path.isdir(asm_file_path):
        files_list = os.listdir(asm_file_path)

    for file in files_list:
        file_parser = Parser(file)
        parsed_code = file_parser.parse()

        code_translator = CodeTranslator(parsed_code)
        machine_code = code_translator.translate()

        hack_writer = HackWriter(machine_code, file)
        hack_writer.write_out()
