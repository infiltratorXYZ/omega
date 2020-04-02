#!/usr/bin/env python
"""Terminal User Interface creator

This module creates a simple terminal user interface, allows you to add
and manage widgets.

...

Classes
-------
initTUI
    Initialises a Terminal User Interface
"""

import curses


class initTUI:
    """Init TUI resosources

    Create empty screen object that can contain windows and widgets.

    ...

    Warnings
    --------
    This class is only a wrapper for the 'TUI' class, which contains all
    the necessary methods (initialisation, widgets, etc.).

    """

    def __enter__(self):
        class TUI:
            """Create entire screen

            ...
            Attributes
            ----------
            stdscr : curses.initscr() object
                The entire screen representation.

            Methods
            -------
            cleanup()
                Ending curses aplication

            """

            def __init__(self):
                # Starting curses aplication
                self.stdscr = curses.initscr()
                curses.noecho()
                curses.cbreak()
                self.stdscr.keypad(True)

            def cleanup(self):
                curses.nocbreak()
                self.stdscr.keypad(False)
                curses.echo()
                curses.endwin()

        self.tui = TUI()
        return self.tui

    def __exit__(self, exc_type, exc_value, traceback):
        self.tui.cleanup()
