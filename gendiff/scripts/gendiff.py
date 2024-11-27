from gendiff.diff_generator import generate_diff
from gendiff.cmd_interface import cli


def main():
    cli()


def diff():
    print(generate_diff('../../tests/fixtures/file1.json',
                        '../../tests/fixtures/file2.json'))


if __name__ == '__main__':
    diff()
    main()
