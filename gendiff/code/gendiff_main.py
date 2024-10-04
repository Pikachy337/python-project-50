import argparse
import json

def about_gendiff():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    # Positional arguments
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    # Optional argument
    parser.add_argument('-f', '--format', type=str, help='set format of output')

    args = parser.parse_args()

    with open(args.first_file) as f1, open(args.second_file) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    return args
