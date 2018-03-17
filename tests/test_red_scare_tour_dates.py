#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `red_scare_tour_dates` package."""


import unittest
from click.testing import CliRunner

from red_scare_tour_dates import red_scare_tour_dates
from red_scare_tour_dates import cli


class TestRed_scare_tour_dates(unittest.TestCase):
    """Tests for `red_scare_tour_dates` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'red_scare_tour_dates.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
