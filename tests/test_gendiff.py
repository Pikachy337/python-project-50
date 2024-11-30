# flake8: noqa
import json

import pytest

from gendiff.diff_generator import generate_diff
from gendiff.formatters import get_formatter
from gendiff.parsers import parse_file


@pytest.fixture
def expected_output_json_yml():
    with open('tests/fixtures/expected_results/expected_output_json_yml.txt', 'r') as file:
        return file.read()


@pytest.fixture
def expected_output_nested_json():
    with open('tests/fixtures/expected_results/expected_output_nested_json.txt', 'r') as file:
        return file.read()


@pytest.fixture
def expected_output_plain():
    with open('tests/fixtures/expected_results/expected_output_plain.txt', 'r') as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, formatter, expected_output_func",
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish', 'json_yml'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'stylish', 'json_yml'),

        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'stylish', 'nested_json'),

        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'plain', 'plain')
    ]
)
def test_generate_diff(file1, file2, formatter, expected_output_func,
                       expected_output_json_yml, expected_output_nested_json,
                       expected_output_plain):
    if expected_output_func == 'json_yml':
        expected_output = expected_output_json_yml
    elif expected_output_func == 'nested_json':
        expected_output = expected_output_nested_json
    elif expected_output_func == 'plain':
        expected_output = expected_output_plain

    diff = generate_diff(file1, file2, formatter)
    assert diff == expected_output


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


def test_get_file_unsupported_format():
    with pytest.raises(ValueError, match="Unsupported format: txt"):
        parse_file("tests/fixtures/expected_results/unsupported_format.txt")


def test_parse_file_unsupported_format():
    with pytest.raises(ValueError, match="Unsupported formatter: txt"):
        get_formatter("tests/fixtures/expected_results/unsupported_format.txt")
