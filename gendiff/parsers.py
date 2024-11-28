import json

import yaml


def parse_file(filepath):
    """
    Parses a file based on its extension ('yaml', 'yml', 'json').

    Supports YAML and JSON formats. Raises an error for unsupported formats.
    """
    extension = filepath.split('.')[-1]

    if extension in ['yml', 'yaml']:
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    elif extension == 'json':
        with open(filepath, 'r') as file:
            return json.load(file)
    else:
        raise ValueError(f'Unsupported format: {extension}')
