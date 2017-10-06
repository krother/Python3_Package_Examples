
import curses


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    begin_x = 20; begin_y = 7
    height = 5; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)

    for x in range(3, 10):
        for y in range(3, 5):
            stdscr.addch(y, x, 42)
    win.refresh()

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()