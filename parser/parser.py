from parser.src.parser import full_parser
from parser.src.saver import save_to_json

def parser():
    data = full_parser()
    save_to_json(data)