from gendiff.formatters.json import format_json as json
from gendiff.formatters.plain import format_plain as plain
from gendiff.formatters.stylish import format_stylish as stylish


def get_formatter(format_name):
    """
    Returns the appropriate formatter function based on the format name.
    """
    if format_name == "stylish":
        return stylish
    elif format_name == "plain":
        return plain
    elif format_name == "json":
        return json
    else:
        raise ValueError(f"Unsupported formatter: {format_name.split('.')[-1]}")
