INDENT = "    "


def format_value(value, depth):
    if not isinstance(value, dict):
        return str(value)

    items = []
    indent = INDENT * (depth + 1)
    for k, v in value.items():
        items.append(f"{indent}{k}: {format_value(v, depth + 1)}")
    return "{\n" + "\n".join(items) + f"\n{INDENT * depth}}}"


def format_node(node, depth):
    indent = INDENT * depth
    if node["type"] == "added":
        return f"{indent}+ {node['key']}: {format_value(node['value'], depth)}"
    elif node["type"] == "removed":
        return f"{indent}- {node['key']}: {format_value(node['value'], depth)}"
    elif node["type"] == "unchanged":
        return f"{indent}  {node['key']}: {format_value(node['value'], depth)}"
    elif node["type"] == "changed":
        return (f"{indent}- {node['key']}: {format_value(node['old_value'],
                                                         depth)}"
                f"\n{indent}+ {node['key']}: {format_value(node['new_value'],
                                                           depth)}")
    elif node["type"] == "nested":
        children = "\n".join(format_node(child, depth + 1)
                             for child in node["children"].values())
        return f"{indent}  {node['key']}: {{\n{children}\n{indent}  }}"


def format_stylish(diff, depth=0):
    result = []
    for key, node in diff.items():
        node["key"] = key
        result.append(format_node(node, depth))
    return "{\n" + "\n".join(result) + "\n}"
