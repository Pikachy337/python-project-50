INDENT = "    "


def format_value(value, depth):
    """
    Formats a value for displaying in a diff.
    """
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        nested_indent = ' ' * ((depth + 1) * 4)
        result = ['{']
        for k, v in value.items():
            result.append(f"{nested_indent}{k}: {format_value(v, depth + 1)}")
        result.append(f"{indent}}}")
        return '\n'.join(result)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def format_stylish(diff, depth=0):
    """
    Formats a diff as a stylish string representation.
    """
    indent = ' ' * (depth * 4)
    result = ['{']

    type_format_map = {
        'added': lambda key, item: (
            f"{indent}  + {key}: "
            f"{format_value(item['value'], depth + 1)}"
        ),
        'removed': lambda key, item: (
            f"{indent}  - {key}: "
            f"{format_value(item['value'], depth + 1)}"
        ),
        'unchanged': lambda key, item: (
            f"{indent}    {key}: "
            f"{format_value(item['value'], depth + 1)}"
        ),
        'changed': lambda key, item: (
            f"{indent}  - {key}: "
            f"{format_value(item['old_value'], depth + 1)}\n"
            f"{indent}  + {key}: "
            f"{format_value(item['new_value'], depth + 1)}"
        ),
        'nested': lambda key, item: (
            f"{indent}    {key}: "
            f"{format_stylish(item['children'], depth + 1)}"
        ),
    }

    for key, item in diff.items():
        type_ = item['type']
        result.append(type_format_map[type_](key, item))

    result.append(indent + '}')
    return '\n'.join(result)
