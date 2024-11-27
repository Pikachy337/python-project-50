import json


def format_json(diff):
    """
    Formats a diff as a JSON string.
    """
    return json.dumps(diff, indent=4)
