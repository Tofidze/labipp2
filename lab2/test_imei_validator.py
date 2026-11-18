import unittest
import tempfile
import os
import io

from contextlib import redirect_stdout
from unittest.mock import patch, Mock

import requests

from imei_validator import (luhn_check, find_imeis_in_text, fetch_imeis_from_url, process_user_input, process_file, process_url)


#  алгоритм Luhn

class TestLuhnCheck(unittest.TestCase):

    def test_valid_imei(self):
        """Корректные IMEI"""
        self.assertTrue(luhn_check("490154203237518"))
        self.assertTrue(luhn_check("356938035643809"))
        self.assertTrue(luhn_check("123456789876543"))

    def test_invalid_checksum(self):
        """Неверная контрольная цифра"""
        self.assertFalse(luhn_check("490154203237519"))
        self.assertFalse(luhn_check("353013101234560"))

    def test_invalid_length(self):
        """IMEI должен состоять ровно из 15 цифр"""
        self.assertFalse(luhn_check("49015420323751"))
        self.assertFalse(luhn_check("4901542032375180"))
        self.assertFalse(luhn_check(""))

    def test_invalid_characters(self):
        """Запрещены буквы пробелы"""
        self.assertFalse(luhn_check("49015420323751A"))
        self.assertFalse(luhn_check("49015420323751 "))
        self.assertFalse(luhn_check("ABCDEFGHIJKLMNO"))

    def test_not_string(self):
        """На вход должна поступать строк"""
        self.assertFalse(luhn_check(490154203237518))
        self.assertFalse(luhn_check(None))

    def test_all_identical_digits(self):
        """одинаковые"""
        self.assertFalse(luhn_check("000000000000000"))
        self.assertFalse(luhn_check("111111111111111"))


# поиск IMEI в тексте


class TestFindImeisInText(unittest.TestCase):

    def test_find_valid_imeis(self):
        text = """
        Телефон 1: 490154203237518
        Телефон 2: 356938035643809
        """

        found = find_imeis_in_text(text)

        self.assertEqual(
            found,
            ["490154203237518", "356938035643809"]
        )

    def test_ignore_invalid_imeis(self):
        text = """
        Неверная сумма: 490154203237519
        Неверная длина: 49015420323751
        Одинаковые цифры: 000000000000000
        """

        found = find_imeis_in_text(text)

        self.assertEqual(found, [])

    def test_mixed_text(self):
        text = """
        Телефон: Samsung
        IMEI: 490154203237518
        Номер: 12345
        Ошибка: 490154203237519
        IMEI: 356938035643809
        """

        found = find_imeis_in_text(text)

        self.assertEqual(
            found,
            ["490154203237518", "356938035643809"]
        )

    def test_empty_text(self):
        """Пустой текст."""
        self.assertEqual(find_imeis_in_text(""), [])

    def test_no_imei(self):
        text = "Просто обычный текст без IMEI."

        self.assertEqual(find_imeis_in_text(text), [])

    def test_duplicate_imeis(self):
        text = "490154203237518 490154203237518"

        found = find_imeis_in_text(text)

        self.assertEqual(
            found,
            ["490154203237518", "490154203237518"]
        )


# загрузка страницы по URL

class TestFetchImeisFromUrl(unittest.TestCase):

    @patch("imei_validator.requests.get")
    def test_successful_request(self, mock_get):
        """загрузка HTML со страницы"""
        mock_response = Mock()
        mock_response.text = """
        <html>
            <body>
                <p>IMEI: 490154203237518</p>
                <p>IMEI: 356938035643809</p>
                <p>IMEI: 490154203237519</p>
            </body>
        </html>
        """

        mock_get.return_value = mock_response

        found = fetch_imeis_from_url("http://example.com")

        self.assertEqual(
            found,
            ["490154203237518", "356938035643809"]
        )

        mock_get.assert_called_once_with(
            "http://example.com",
            timeout=10
        )

    @patch("imei_validator.requests.get")
    def test_connection_error(self, mock_get):
        """Ошибка подключения к сайту"""
        mock_get.side_effect = requests.exceptions.ConnectionError(
            "Connection error"
        )

        output = io.StringIO()

        with redirect_stdout(output):
            found = fetch_imeis_from_url("http://example.com")

        self.assertEqual(found, [])
        self.assertIn("Ошибка загрузки страницы", output.getvalue())

    @patch("imei_validator.requests.get")
    def test_http_error(self, mock_get):
        """вернул ошибку HTTP"""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = (
            requests.exceptions.HTTPError("404 Not Found")
        )

        mock_get.return_value = mock_response

        output = io.StringIO()

        with redirect_stdout(output):
            found = fetch_imeis_from_url("http://example.com")

        self.assertEqual(found, [])
        self.assertIn("Ошибка загрузки страницы", output.getvalue())

    @patch("imei_validator.requests.get")
    def test_empty_page(self, mock_get):
        """Страница загружена, IMEI на ней отсутствует"""
        mock_response = Mock()
        mock_response.text = "<html><body>Nothing here</body></html>"

        mock_get.return_value = mock_response

        found = fetch_imeis_from_url("http://example.com")

        self.assertEqual(found, [])



if __name__ == "__main__":
    unittest.main(verbosity=2)