import curses
from curses import KEY_BACKSPACE, color_pair, wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)

    if wpm > 0:
        stdscr.addstr(1, 0, f"{wpm} Words per Minute")

    for i, char in enumerate(current):
        if i < len(target):
            correct_char = target[i]

            if current[i] == correct_char:
                color = color_pair(1)
            else:
                color = color_pair(2)
        else:
            color = color_pair(2)

        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    target_text = "hello world here is some text for this app"
    current_text = []
    start_time = time.time()

    while True:
        time_elapsed = max(time.time() - start_time, 1) # avoid div by 0
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        key_is_backspace_p = False
        key_is_esc_p = False
        key = stdscr.getkey()

        if len(key) == 1:
            if ord(key) == 27:
                key_is_esc_p = True
            elif key in ('\b', "\x7f"):
                key_is_backspace_p = True
            # put more single-char key tests here
        else: # length of key is not 1
            if key in ("KEY_BACKSPACE"):
                key_is_backspace_p = True

        # interpret (possibly special) key
        if key_is_backspace_p:
            if len(current_text) > 0:
                current_text.pop()
        elif key_is_esc_p:
            break

        else: 
            # key isn't special, or a "command"
            # so just append it to the current_text list

            # the only way user should be able to get keys into the
            # current list, is if its length is under the length of
            # the target text.

            if len(current_text) < len(target_text):
                current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)

