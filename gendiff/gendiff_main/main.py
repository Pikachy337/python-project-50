import argparse
from gendiff.gendiff_main.parsers import parse_file
from gendiff.formatters.stylish import format_stylish as stylish
from gendiff.formatters.plain import format_stylish as plain
from gendiff.formatters.json import format_stylish as json


def main_gendiff():
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

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == "stylish":
        return stylish(diff)
    elif format_name == "plain":
        return plain(diff)
    elif format_name == "json":
        return json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}

    for key in keys:
        if key in data1 and key not in data2:
            diff[key] = {"type": "removed", "value": data1[key]}
        elif key not in data1 and key in data2:
            diff[key] = {"type": "added", "value": data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {"type": "nested",
                         "children": build_diff(data1[key], data2[key])}
        elif data1[key] == data2[key]:
            diff[key] = {"type": "unchanged", "value": data1[key]}
        else:
            diff[key] = {"type": "changed",
                         "old_value": data1[key], "new_value": data2[key]}

    return diff
