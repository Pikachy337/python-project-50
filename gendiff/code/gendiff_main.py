import argparse
from gendiff.code.parsers import parse_file


def main_gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    # Positional arguments
    parser.add_argument('first_file', type=str, help='First file path')
    parser.add_argument('second_file', type=str, help='Second file path')
    # Optional argument with choices for format
    parser.add_argument('-f', '--format', type=str, default='stylish', help='Output format',
                        choices=['stylish'])

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == "stylish":
        return format_stylish(diff)
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
            diff[key] = {"type": "nested", "children": build_diff(data1[key], data2[key])}
        elif data1[key] == data2[key]:
            diff[key] = {"type": "unchanged", "value": data1[key]}
        else:
            diff[key] = {"type": "changed", "old_value": data1[key], "new_value": data2[key]}

    return diff


def format_stylish(diff, depth=0):
    indent = ' ' * (depth * 4)
    result = ['{']

    for key, item in diff.items():
        type_ = item['type']
        current_indent = indent + ' ' * 2  # Adjusted indentation for each type

        if type_ == 'added':
            result.append(f"{current_indent}+ {key}: {format_value(item['value'], depth + 1)}")
        elif type_ == 'removed':
            result.append(f"{current_indent}- {key}: {format_value(item['value'], depth + 1)}")
        elif type_ == 'unchanged':
            result.append(f"{current_indent}  {key}: {format_value(item['value'], depth + 1)}")
        elif type_ == 'changed':
            result.append(f"{current_indent}- {key}: {format_value(item['old_value'], depth + 1)}")
            result.append(f"{current_indent}+ {key}: {format_value(item['new_value'], depth + 1)}")
        elif type_ == 'nested':
            children = format_stylish(item['children'], depth + 1)
            result.append(f"{current_indent}  {key}: {children}")

    result.append(indent + '}')
    return '\n'.join(result)


def format_value(value, depth):
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
