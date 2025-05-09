# tests/test_console.py
import click.testing
import pytest

from card_sorter import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.mark.skip("broken atm")
def test_main_succeeds(runner):
    result = runner.invoke(console.main, args="")
    assert result.exit_code == 0
