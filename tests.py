import unittest
from unittest.mock import patch
from app import create_orders


class CreateOrdersTestCase(unittest.TestCase):

    @patch('app.Client')
    def test_create_orders_sell(self, mock_client):
        data = {
            "volume": 10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "SELL",
            "priceMin": 200.0,
            "priceMax": 300.0
        }

        mock_client.return_value.create_order.return_value = {
            "symbol": "BTCUSDT",
            "side": "SELL",
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": 100.0,
            "price": 250.0,
            "orderId": 123456789
        }

        orders = create_orders(data)

        self.assertEqual(len(orders), 5)
        for order in orders:
            self.assertEqual(order['side'], 'SELL')
            self.assertEqual(order['symbol'], 'BTCUSDT')

    @patch('app.Client')
    def test_create_orders_buy(self, mock_client):
        data = {
            "volume": 10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "BUY",
            "priceMin": 200.0,
            "priceMax": 300.0
        }

        mock_client.return_value.create_order.return_value = {
            "symbol": "BTCUSDT",
            "side": "BUY",
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": 100.0,
            "price": 250.0,
            "orderId": 123456789
        }

        orders = create_orders(data)

        self.assertEqual(len(orders), 5)
        for order in orders:
            self.assertEqual(order['side'], 'BUY')
            self.assertEqual(order['symbol'], 'BTCUSDT')


if __name__ == '__main__':
    unittest.main()
