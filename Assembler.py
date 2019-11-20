import os
import sys

from CodeTranslator import CodeTranslator
from HackWriter import HackWriter
from Parser import Parser

if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
        exit(1)
    asm_file_path = sys.argv[1]

    files_list = [asm_file_path]

    if os.path.isdir(asm_file_path):
        files_list = os.listdir(asm_file_path)

    print("got file list")

    for file in files_list:
        print('FILE:\n')
        file_parser = Parser(file)
        parsed_code = file_parser.parse()
        print('Parsed\n')
        code_translator = CodeTranslator(parsed_code)
        machine_code = code_translator.translate()
        print('Translated:\n')

        out_file = file[:-4] + '.hack'

        hack_writer = HackWriter(machine_code, out_file)
        hack_writer.write_out()
        print('written:\n')

