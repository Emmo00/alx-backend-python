#!/usr/bin/env python3
"""
Test the utils.py module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access nested map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
        Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map raises error with wrong parameters"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test get_json function
    """
    @patch('module_name.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        mock_requests = Mock()
        mock_requests.json.return_value = test_payload
        
        mock_requests_get.return_value = mock_requests

        result = get_json(test_url)

        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
