from hexlet_python_package.code.gendiff_main import main_gendiff, generate_diff


def main():
    main_gendiff()


def diff():
    print(generate_diff('../../tests/fixtures/file1.json',
                        '../../tests/fixtures/file2.json'))


if __name__ == '__main__':
    diff()
    main()
