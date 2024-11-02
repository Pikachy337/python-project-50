from gendiff.code.gendiff_main import generate_diff


def test_generate_diff_json():
    with open('tests/fixtures/file1.json') as file1, open('tests/fixtures/file2.json') as file2:
        expected_output = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected_output


def test_generate_diff_yml():
    expected_output = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == expected_output


def test_generate_diff_nested_json():
    expected_output = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

    assert generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json') == expected_output
