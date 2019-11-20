import os
import sys

from CodeTranslator import CodeTranslator
from HackWriter import HackWriter
from Parser import Parser

if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
        exit(1)
    asm_file_path = sys.argv[1]

    files_list = [os.path.abspath(asm_file_path)]
    path_to_dir = ''

    if os.path.isdir(asm_file_path):
        files_list = os.listdir(asm_file_path)
        path_to_dir = os.path.abspath(asm_file_path)

    for file in filter(lambda x: x[-4:] == '.asm', files_list):
        file = os.path.join(path_to_dir, file)
        file_parser = Parser(file)
        parsed_code = file_parser.parse()
        code_translator = CodeTranslator(parsed_code)
        machine_code = code_translator.translate()

        out_file = file[:-4] + '.hack'

        hack_writer = HackWriter(machine_code, out_file)
        hack_writer.write_out()
