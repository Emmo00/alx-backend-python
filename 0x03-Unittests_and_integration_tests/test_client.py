#!/usr/bin/env python3
"""
Test client.py
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test GithubOrgClient
    """
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, test_org, mock_get_json):
        """
        test org return value
        """
        mock_get_json.return_value = {'payload': True}

        GithubOrgClient(test_org).org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{test_org}")
