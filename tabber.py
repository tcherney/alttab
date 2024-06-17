"""
Module that brings the nth instance of the requested program to the forground
"""

import string
import sys
import pygetwindow as gw

def tab_to_program(program_name: string, index: int=0) -> None:
    """Brings the given program to the forground

    Args:
        program_name (string): Name of program to bring forward
        index (int): Which instance of the program to bring forward
    """
    program_window: any = gw.getWindowsWithTitle(program_name)[index]
    program_window.minimize()
    program_window.restore()

def main() -> None:
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} program_name index(number starting at 0)")
        return
    else:
        program_name: string = sys.argv[1]
        try:
            index: int = int(sys.argv[2])
        except ValueError:
            print("index must be a number")
            return
        tab_to_program(program_name, index)

if __name__ == "__main__":
    main()

        