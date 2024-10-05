import argparse
import json


def main_gendiff():
    parser = argparse.ArgumentParser(description='Compares two'
                                                 ' configuration files'
                                                 ' and shows a difference.')

    # Positional arguments
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    # Optional argument
    parser.add_argument('-f', '--format', type=str, help='set format of output')

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

        all_keys = sorted(set(data1.keys()).union(data2.keys()))

        diff_result = []

        for key in all_keys:
            if key in data1 and key in data2:
                if data1[key] == data2[key]:
                    diff_result.append(f'   {key}: {data1[key]}')
                else:
                    diff_result.append(f'  - {key}: {data1[key]}')
                    diff_result.append(f'  + {key}: {data2[key]}')
            elif key in data1:
                diff_result.append(f'  - {key}: {data1[key]}')
            else:
                diff_result.append(f'  + {key}: {data2[key]}')
        return "{\n" + "\n".join(diff_result) + "\n}"
