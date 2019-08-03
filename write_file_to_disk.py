import json, os

def write_json_to_file(content, dest_file="data.json"):
    with open(dest_file, 'w') as outfile:
        json.dump(content, outfile)

def _create_folder_in_cwd(folder_name):
    path = os.getcwd()
    path_new = path + "/" + folder_name
    if not os.path.exists(path_new):
        os.mkdir(path_new)
    return path_new

def write_json_to_file_per_book(content):
    for book_collection in content["contents"]:
        file_name = _create_folder_in_cwd("data/") + book_collection["bookName"] + ".json"
        with open(file_name, "w") as outfile:
            json.dump(book_collection, outfile)