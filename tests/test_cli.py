from click.testing import CliRunner
from detect_languages.cli import all, main

runner = CliRunner()


def test_cli_main_language():
    response = runner.invoke(main, ["--path", "./samples/Python", "--output", "json"])
    assert response.exit_code == 0
    assert "Python" in response.output


def test_cli_all_languages():
    response = runner.invoke(all, ["--path", ".", "--output", "json", "--exclude-dirs", ".venv", "--exclude-dirs", ".tox", "--exclude-dirs", "samples", "--output", "json"])
    assert response.exit_code == 0
    assert "Python" in response.output
    assert "JSON" in response.output
    assert "Markdown" in response.output
    assert "TOML" in response.output
    assert "INI" in response.output
