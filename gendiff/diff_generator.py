from gendiff.formatters import get_formatter
from gendiff.parsers import parse_file
from gendiff.diff_builder import build_diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    """
     Generates a diff between two files and formats the result.
    """
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    format_func = get_formatter(format_name)

    diff = build_diff(data1, data2)

    return format_func(diff)
