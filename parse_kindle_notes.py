# -*- coding: utf-8 -*-
import json, sys, codecs

class Note:
    def __init__(self, book_name, time_stamp, location, note_content):
        self.book_name = book_name
        self.time_stamp = time_stamp
        self.location = location
        self.note_content = note_content

def transform_notes_to_json(source_file_path):
    """
    book_notes are a list of Note objects:
        class Note:
            def __init__(self, book_name, time_stamp, location, note_content):
                self.book_name = book_name
                self.time_stamp = time_stamp
                self.location = location
                self.note_content = note_content
    """
    book_notes = _parse_kindle_note(source_file_path)
    book_list = []

    data = {}
    data["title"] = "Kindle Notes and Highlights"
    data["contents"] = []

    print("Total Number of Notes are {}".format(len(book_notes)))
    for note in book_notes:
        # Build a note dictionary for this note
        note_dic = {}
        note_dic["location"] = note.location.strip()
        note_dic["timestamp"] = note.time_stamp.replace("\r\n","")
        note_dic["note"] = note.note_content.replace("\r\n","")
        if note.book_name.strip() not in book_list:
            book_list.append(note.book_name.strip())
            # Build a note collection for this new book
            note_book1 = {}
            note_book1["bookName"] = note.book_name.replace("\r\n","")
            note_book1["notes"] = []
            # Append this note dictionary to its book collection
            note_book1["notes"].append(note_dic)
            # Append this book collection to root data
            data["contents"].append(note_book1)
        else:
            for book_collection in data["contents"]:
                if book_collection["bookName"] == note.book_name.replace("\r\n",""):
                    book_collection["notes"].append(note_dic)
    print("There are {} books in total ".format(len(book_list)))
    return data

def _parse_kindle_note(file_path):
    with codecs.open(file_path, "r", encoding="utf-8-sig") as file: #avoid codecs.BOM_UTF8 '\xef\xbb\xbf' in first line
        f1 = file.readlines()

        line_number = 0
        note = Note("", "", "", "")
        book_notes = []
        current_line = 0
        for x in f1:
            current_line += 1
            line_number += 1
            if line_number == 1:
                note.book_name = x
            elif line_number == 2:
                try:
                    note.location = x.split("|")[0].strip()
                    note.time_stamp = x.split("|")[1].strip()
                except Exception as ex:
                    _raise_incorrect_format(current_line=current_line, line_content=x)
            elif line_number == 4:
                note.note_content += x
            elif line_number == 5:
                line_number = 0
                book_notes.append(note)
                note = Note("", "", "", "")
        return book_notes

def _raise_incorrect_format(current_line, line_content):
    print("Error: Incorrect note format found in Line Number #{}, the content is:".format(current_line))
    print(line_content)
    exit()
    


    