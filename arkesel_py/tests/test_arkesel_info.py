"""Tests for Arkesel info module."""

# from arkesel_py import arkesel_py
from arkesel_py.arkesel_info import Info
import pytest
import vcr

from click.testing import CliRunner

from arkesel_py import cli

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'sms_api_wrapper.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

@pytest.fixture
def balance_response():
    """Test data response"""
    return ["data", "status" ]

@pytest.mark.vcr()
def test_smsBalance(balance_response):
    """Tests an API call to get check account balance"""
    arkesel = Info()
    result = arkesel.smsBalance()
    assert isinstance(result, dict), """The response should be in the form of a dictionary"""
    assert set(balance_response).issubset(result) , """All Keys should be in the response"""