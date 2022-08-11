
import os
import json

f = open(os.path.join( os.path.dirname(__file__), 'char_widths.json' ), "r")
char_widths = json.load(f)
f.close()

def get_width(code):
    global char_widths
    for begin, end, width in char_widths:
        if begin <= code <= end:
            return width
    return 1

def get_index(string, begin, total_width):
    idx = begin
    size = 0
    while size < total_width and idx < len(string):
        o = ord(string[idx])
        width = get_width(o)
        if size + width > total_width:
            break
        size += width
        idx += 1
    return idx, total_width - size

def substr(string, beg, length=-1, fill=False):
    if type(string) == bytes:
        raise ValueError("bytes type not allowed")

    if length < 0:
        return string

    idx_beg, fillsize = get_index(string, 0, beg)
    idx_end, fillsize = get_index(string, idx_beg, length)
    return string[idx_beg:idx_end] + (' ' * ( fillsize if fill else 0 ) )

