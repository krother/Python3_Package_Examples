
# vertical typing

import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    begin_x = 20; begin_y = 7
    height = 15; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)

    char = 'A'
    for x in range(3, 40):
        for y in range(3, 15):
            stdscr.addch(y, x, char)
            win.refresh()
            stdscr.refresh()
            char = stdscr.getkey()[0]
            char = max(['A', char])


wrapper(main)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()
