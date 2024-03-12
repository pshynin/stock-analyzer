import unittest
from unittest.mock import Mock, patch
import json
from analyze_stocks import CandleData, fetch_candle_data, parse_candle_data, handler


class TestCandleData(unittest.TestCase):
    def test_candle_data_initialization(self):
        candle = CandleData(123, 100, 200, 150, 180, 1000)
        self.assertEqual(candle.time, 123)
        self.assertEqual(candle.low, 100)
        self.assertEqual(candle.high, 200)
        self.assertEqual(candle.open_price, 150)
        self.assertEqual(candle.close_price, 180)
        self.assertEqual(candle.volume, 1000)

    def test_fetch_candle_data(self):
        mock_response_data = [[123, 100, 200, 150, 180, 1000]]
        mock_https_connection = self.setup_mock_https_connection(mock_response_data)

        with patch('http.client.HTTPSConnection', mock_https_connection):
            data = fetch_candle_data()
            self.assertEqual(data, json.dumps(mock_response_data))

    def test_parse_candle_data(self):
        json_data = [[123, 100, 200, 150, 180, 1000]]
        candle_data_list = parse_candle_data(json.dumps(json_data))
        self.assertEqual(len(candle_data_list), 1)
        candle = candle_data_list[0]
        self.assertEqual(candle.time, 123)
        self.assertEqual(candle.low, 100)
        self.assertEqual(candle.high, 200)
        self.assertEqual(candle.open_price, 150)
        self.assertEqual(candle.close_price, 180)
        self.assertEqual(candle.volume, 1000)

    def test_handler(self):
        mock_response_data = [[123, 100, 200, 150, 180, 1000]]
        mock_fetch_candle_data = Mock(return_value=json.dumps(mock_response_data))
        mock_parse_candle_data = Mock(return_value=[CandleData(123, 100, 200, 150, 180, 1000)])

        with patch('your_script_name.fetch_candle_data', mock_fetch_candle_data), \
                patch('your_script_name.parse_candle_data', mock_parse_candle_data), \
                patch('builtins.print') as mocked_print:
            handler(None, None)
            mocked_print.assert_called_with('Time:', 123, 'Low:', 100, 'High:', 200, 'Open Price:', 150, 'Close Price:', 180, 'Volume:', 1000)

    @staticmethod
    def setup_mock_https_connection(mock_response_data):
        mock_response = Mock()
        mock_response.read.return_value = json.dumps(mock_response_data)
        mock_response.decode.return_value = json.dumps(mock_response_data)
        mock_response.getresponse.return_value = mock_response

        mock_https_connection = Mock()
        mock_https_connection.return_value = mock_response

        return mock_https_connection


if __name__ == '__main__':
    unittest.main()
