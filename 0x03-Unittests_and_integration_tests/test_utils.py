#!/usr/bin/env python3
"""
Test the utils.py module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        test get_json
        """
        mock_requests = Mock()
        mock_requests.json.return_value = test_payload

        mock_requests_get.return_value = mock_requests

        result = get_json(test_url)

        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """test memoize function
    """
    def test_memoize(self):
        """
        test memoize
        """
        class TestClass:
            """test class"""

            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """a property"""
                return self.a_method()

        test_instance = TestClass()
        with patch.object(test_instance, 'a_method', return_value=42) as \
                mock_a_method:
            result = test_instance.a_property
            self.assertEqual(result, 42)
            result = test_instance.a_property
            self.assertEqual(result, 42)

            mock_a_method.assert_called_once()
