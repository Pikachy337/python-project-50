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
    "file1, file2",
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    ]
)
def test_generate_diff(file1, file2, expected_output_json_yml):
    diff = generate_diff(file1, file2)
    assert diff == expected_output_json_yml


@pytest.mark.parametrize(
    "file1, file2",
    [
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json')
    ]
)
def test_generate_diff_nested(file1, file2, expected_output_nested_json):
    diff = generate_diff(file1, file2)
    assert diff == expected_output_nested_json


@pytest.mark.parametrize(
    "file1, file2, format_name",
    [
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json', 'plain')
    ]
)
def test_plain_format(file1, file2, format_name, expected_output_plain):
    diff = generate_diff(file1, file2, format_name=format_name)
    assert diff == expected_output_plain


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
