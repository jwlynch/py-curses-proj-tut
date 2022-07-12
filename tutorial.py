import curses
from curses import KEY_BACKSPACE, color_pair, wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "hello world here is some text for this app"
    current_text = []

    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()

    while True:
        key_is_backspace_p = False
        key_is_esc_p = False
        key = stdscr.getkey()

        if len(key) == 1:
            # put more single-char key tests here

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

wrapper(main)

