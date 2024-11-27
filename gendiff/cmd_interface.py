import argparse


def cli():
    """
    Parse and return command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    # Positional arguments
    parser.add_argument('first_file', type=str, help='First file path')
    parser.add_argument('second_file', type=str, help='Second file path')
    # Optional argument with choices for format
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        help='Output format',
                        choices=['stylish', 'plain', 'json'])

    return parser.parse_args()
