def format_value(value):
    """
    Formats a value for a plain diff representation.
    """
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    else:
        return str(value).lower()


def format_plain(diff, path=''):
    """
    Formats a diff as a plain string representation.
    """
    lines = []
    for key, value in diff.items():
        full_path = f"{path}.{key}" if path else key

        if value['type'] == 'added':
            lines.append(f"Property '{full_path}' was"
                         f" added with value: {format_value(value['value'])}")
        elif value['type'] == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif value['type'] == 'changed':
            old_value = format_value(value['old_value'])
            new_value = format_value(value['new_value'])
            lines.append(f"Property '{full_path}' was"
                         f" updated. From {old_value} to {new_value}")
        elif value['type'] == 'nested':
            nested_lines = format_plain(value['children'], full_path)
            lines.append(nested_lines)

    return '\n'.join(line for line in lines if line)
