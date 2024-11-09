import json
from gendiff.gendiff_main.main import generate_diff


def test_generate_diff_json():
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


def test_plain_format():
    expected_output = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From true to null\n"
        "Property 'common.setting4' was added with value: 'blah blah'\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
        "Property 'common.setting6.ops' was added with value: 'vops'\n"
        "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
        "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
        "Property 'group2' was removed\n"
        "Property 'group3' was added with value: [complex value]"
    )
    assert generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json',
                         format_name='plain') == expected_output


def test_generate_diff_json_output():
    diff_json = generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json', format_name='json')
    diff_data = json.loads(diff_json)

    assert isinstance(diff_data, dict)
    assert "common" in diff_data
    assert "group1" in diff_data
    assert "group2" in diff_data
    assert "group3" in diff_data

    assert isinstance(diff_data["common"], dict)
    assert "children" in diff_data["common"]
    assert "setting1" in diff_data["common"]["children"]
    assert "setting6" in diff_data["common"]["children"]
