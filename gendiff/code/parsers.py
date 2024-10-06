import json
import yaml


def parse_file(filepath):
    extension = filepath.split('.')[-1]

    if extension in ['yml', 'yaml']:
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    elif extension == 'json':
        with open(filepath, 'r') as file:
            return json.load(file)
    else:
        return f'Unsupported file format {extension}'
