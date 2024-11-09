# Gendiff - Difference Generator

[![Actions Status](https://github.com/Pikachy337/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Pikachy337/python-project-50/actions)
![CI](https://github.com/Pikachy337/python-project-50/actions/workflows/pyci.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/434e378fb1ab4936a2f7/maintainability)](https://codeclimate.com/github/Pikachy337/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/434e378fb1ab4936a2f7/test_coverage)](https://codeclimate.com/github/Pikachy337/python-project-50/test_coverage)

`Gendiff` is a CLI utility for comparing configuration files and displaying the differences in various formats. It supports JSON and YAML formats, with output formats like `stylish`, `plain`, and `json`. It is useful for configuration management, logging changes, and integrating with automated systems.

## Description

`Gendiff` shows changes between two configuration files by:
- highlighting added properties
- marking removed properties
- indicating updated values
- displaying nested differences

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pikachy337/python-project-50.git
   ```
2. Navigate to the project directory:
   ```bash
   cd python-project-50
   ```
3. Install dependencies using [Poetry](https://python-poetry.org/):
   ```bash
   poetry install
   ```

## Usage

Run the `gendiff` command:

```bash
gendiff_main [options] <filepath1> <filepath2>
```

### Options

- `-h, --help`: Show help message and exit.
- `-f FORMAT, --format FORMAT`: Specify output format (`stylish`, `plain`, `json`). The default is `stylish`.

### Examples

#### JSON output

```bash
gendiff_main --format json file1.json file2.json
```

#### Plain output

```bash
gendiff_main --format plain file1.json file2.json
```

#### Stylish output

```bash
gendiff_main file1.yaml file2.yaml
```

## Output Formats

- **Stylish**: Default format with indentation and symbols to mark changes.
- **Plain**: Text-only format, ideal for reports and logs.
- **JSON**: Structured format suitable for programmatic integration with other applications.

## Examples (Asciinema)

- **Comparing JSON files**:  
  [![json](https://asciinema.org/a/BTQurZgbZAo5gm0ovKtBIilDU.svg)](https://asciinema.org/a/BTQurZgbZAo5gm0ovKtBIilDU)

- **Comparing YAML files**:  
  [![yml](https://asciinema.org/a/LLKj0XoYPhNbflZFN6q0ocKfd.svg)](https://asciinema.org/a/LLKj0XoYPhNbflZFN6q0ocKfd)

- **Recursive comparison**:  
  [![recursion](https://asciinema.org/a/WjU7giemLxqJthTg6dpLccvCX.svg)](https://asciinema.org/a/WjU7giemLxqJthTg6dpLccvCX)

- **Plain format output**:  
  [![plain](https://asciinema.org/a/b4SdUMAtL7RWUim5PbugI5wHN.svg)](https://asciinema.org/a/b4SdUMAtL7RWUim5PbugI5wHN)

- **JSON format output**:  
  [![json](https://asciinema.org/a/7w3PtdiW7wUpnOGZ1ccikwFka.svg)](https://asciinema.org/a/7w3PtdiW7wUpnOGZ1ccikwFka)

## Testing

To run tests, use:
```bash
poetry run pytest
```
