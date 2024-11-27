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


def test_generate_diff_json(expected_output_json_yml):
    diff_json = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff_json == expected_output_json_yml


def test_generate_diff_yml(expected_output_json_yml):
    diff_yml = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    assert diff_yml == expected_output_json_yml


def test_generate_diff_nested_json(expected_output_nested_json):
    diff_nested_json = generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json')
    assert diff_nested_json == expected_output_nested_json


def test_plain_format(expected_output_plain):
    diff_plain = generate_diff('tests/fixtures/file3.json', 'tests/fixtures/file4.json',
                               format_name='plain')
    assert diff_plain == expected_output_plain


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
