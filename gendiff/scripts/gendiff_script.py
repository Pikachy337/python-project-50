from gendiff.code.gendiff_main import main_gendiff, generate_diff


def main():
    main_gendiff()


def diff():
    print(generate_diff('file1.json', 'file2.json'))


if __name__ == '__main__':
    diff()
    main()
