import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Calculate expected results based on the formula (bid_price + ask_price) / 2
        expected_results = [
            ('ABC', 120.48, 121.2, 120.84),
            ('DEF', 117.87, 121.68, 119.775)
        ]

        for i, quote in enumerate(quotes):
            with self.subTest(quote=quote):
                result = getDataPoint(quote)
                self.assertEqual(result, expected_results[i])

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Calculate expected results based on the formula (bid_price + ask_price) / 2
        expected_results = [
            ('ABC', 120.48, 119.2, 119.84),
            ('DEF', 117.87, 121.68, 119.775)
        ]

        for i, quote in enumerate(quotes):
            with self.subTest(quote=quote):
                result = getDataPoint(quote)
                self.assertEqual(result, expected_results[i])

if __name__ == '__main__':
    unittest.main()
