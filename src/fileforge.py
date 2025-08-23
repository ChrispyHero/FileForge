import argparse
import sys 
import textwrap
from pathlib import Path
import data


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

        # Getting the target_file_path
        abs_path = Path(__file__).resolve()
        json_data_path = abs_path.parents[1] / "data.json"
        json_data = data.load_data_from_json(str(json_data_path))
        target_file_path = data.load_target_file_path(json_data)

if __name__ == "__main__":
    args = parse()
    main(args)