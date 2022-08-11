
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

def get_index(string, begin, width):
    idx = begin
    scanned_size = 0
    string_length = len(string)
    while scanned_size < width and idx < string_length:
        o = ord(string[idx])
        char_width = get_width(o)
        if scanned_size + char_width > width:
            break
        scanned_size += char_width
        idx += 1
    return idx, width - scanned_size

def substr(string, beg, length=-1, fill=True):
    if type(string) == bytes:
        raise ValueError("bytes type not allowed")

    if length < 0:
        return string

    fill_prefix = ""
    fill_suffix = ""
    idx_beg, fillsize = get_index(string, 0, beg)
    if fill:
        fill_prefix = " " * fillsize
        idx_beg +=fillsize
        length -= fillsize

    idx_end, fillsize = get_index(string, idx_beg, length)
    if fill:
        fill_suffix = " " * fillsize

    return fill_prefix + string[idx_beg:idx_end] + fill_suffix

