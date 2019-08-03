import sys

from parse_kindle_notes import transform_notes_to_json
from write_file_to_disk import write_json_to_file_per_book, write_json_to_file

def _raise_message():
    print("Error: Please specify a valid file path!")
    print("Pattern: python main.py SOURCE_FILE_PATH")
    print("Sample Usage: python main.py '/users/xxx/desktop/My Clippings.txt'")
    exit()

if __name__ == "__main__":
    SOURCE_FILE_PATH = ""
    MULTIPLE_FILE = True
    try:
        SOURCE_FILE_PATH = sys.argv[1]
    except Exception as error:
        _raise_message()
    try:
        multiple_or_one = sys.argv[2]
        if multiple_or_one == '--together':
            MULTIPLE_FILE = False
    except Exception as error:
        pass
    if SOURCE_FILE_PATH == "":
        _raise_message()
        
    data = transform_notes_to_json(source_file_path=SOURCE_FILE_PATH)
    # write_json_to_file(content=data, dest_file=TARGET_FILE_PATH)
    if MULTIPLE_FILE:
        write_json_to_file_per_book(data)
    else:
        write_json_to_file(content=data)
