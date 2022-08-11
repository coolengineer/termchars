
import os
import sys
import json
import termios

report_position = b'\x1b[6n'
move_to_home = b'\x1b[1;1H'
erase_screen = b'\x1b[0J'
erase_line = b'\x1b[0K'

def read_position(stdin):
    state = 0
    col = ''
    row = ''
    while True:
        ch = stdin.read(1)
        if ch is None:
            break
        ch = ch[0]
        if state == 0:
            if ch == ord('\x1b'):
                state = 1
            continue
        elif state == 1:
            if ch == ord('['):
                state = 2
            continue
        elif state == 2:
            if ch == ord(';'):
                state = 3
                continue
            row += chr(ch)
        elif state == 3:
            if ch == ord('R'):
                break
            col += chr(ch)

    row = int(row)
    col = int(col)

    return row, col

def set_noecho(fd):
    attr = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~(termios.ICANON | termios.ECHO)
    termios.tcsetattr(fd, termios.TCSADRAIN, new)
    return attr

def set_echo(fd, attr):
    termios.tcsetattr(fd, termios.TCSADRAIN, attr)

def build_character_width_table():
    if not os.isatty(sys.stdin.fileno()) or not os.isatty(sys.stdout.fileno()):
        raise Exception("stdin/stdout must be a terminal")

    stdin = os.fdopen(sys.stdin.fileno(), "rb", 0)
    stdout = os.fdopen(sys.stdout.fileno(), "wb", 0)
    fd = stdin.fileno()

    attr = set_noecho(fd)
    char_widths = []
    try:
        stdout.write(move_to_home + erase_screen)
        prev_width = 1
        begin = 0x1f
        max_value = 0x110000
        for ch in range(begin, max_value):
            # Skip surrogates
            if 0xd800 <= ch <= 0xdfff:
                continue
            buf = chr(ch).encode('utf8')
            stdout.write(move_to_home + buf + report_position)
            row, col = read_position(stdin)
            width = col - 1

            if ch % 0x1000 == 0 or ch // 0x110000:
                stdout.write(f"  {width} {hex(ch)}/{hex(max_value)}".encode() + erase_line)
            if prev_width == width:
                continue

            char_widths.append( [begin, ch - 1, prev_width] )
            prev_width = width
            begin = ch

        base_dir = os.path.dirname(__file__)
        out = open(f"{base_dir}/char_widths.json", "w")
        json.dump(char_widths, out, separators=(",", ":"))
        out.close()
    except KeyboardInterrupt:
        pass
    finally:
        set_echo(fd, attr)

    print("")

print("Do not type any keys...")
print("Do not change this terminal into background...")
print("----------------------------------------------")
input("Start with enter key:")

build_character_width_table()
