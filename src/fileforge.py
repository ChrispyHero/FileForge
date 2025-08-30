import argparse
import sys 
import textwrap
from data import *
from append import *


def parse() -> argparse.Namespace: 
    """
    Function to parse the arguments
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""\
            Github link: 
            https://github.com/ChrispyHero/FileForge""")
    )


    # The quick flag. For entering lines of text quickly. 
    # Example: py fileforge.py -q "This text will be appended to a file"
    parser.add_argument(
        "-q",
        "--quick",
        nargs="+",
        type=str,
        metavar="ITEM",
        help="Gathers all subsequent items into a list. " \
        "To include spaces within a single item, enclose it in quotes.",
        dest="quick"
    )

    # Prints the help message if no flags are given
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    
    return args


def main(args: argparse.Namespace):
    """
    Function to execute the logic behind each flag given by the user
    """
    if args.quick is not None:
        print("Your input:", args.quick)
        target_file_path = load_target_file_path()
        append_list_to_textfile(text=args.quick, filepath=target_file_path)
        

if __name__ == "__main__":
    args = parse()
    main(args)