import json


def format_stylish(diff):
    return json.dumps(diff, indent=4)
