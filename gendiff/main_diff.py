from gendiff.cmd_interface import cli
from gendiff.diff_generator import generate_diff
from gendiff.formatters import get_formatter


def main():
    """
    Main function to handle command-line input, generate a file diff,
    and print the formatted result.
    """
    args = cli()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    formatter = get_formatter(args.format)
    formatted_diff = formatter(diff)

    print(formatted_diff)
