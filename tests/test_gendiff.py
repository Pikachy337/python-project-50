from gendiff.code.gendiff_main import generate_diff


def test_generate_diff_json():
    with open('tests/fixtures/file1.json') as file1, open('tests/fixtures/file2.json') as file2:
        expected_output = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected_output


def test_generate_diff_yml():
    expected_output = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == expected_output
