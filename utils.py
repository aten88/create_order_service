import random
from binance.client import Client

API_KEY = 'ZJpGiiRpw0BUWRDm52kFr0vLnAg9PnNHonVjZce7G97hp98IPWdxBYQIBTnEOxeD'
API_SECRET = 'VzWgKQ2Tyll3buyXkxCSIFFRqAhll21zsjKKKD2U2CSGs5qQepoVAef6B07gvDLn'


def create_orders(data):

    client = Client(API_KEY, API_SECRET)

    volume = data['volume']
    number = data['number']
    amount_dif = data['amountDif']
    side = data['side']
    price_min = data['priceMin']
    price_max = data['priceMax']

    orders = []

    for _ in range(number):
        price = random.uniform(price_min, price_max)

        amount = random.uniform(
            volume/number - amount_dif,
            volume/number + amount_dif
        )

        if side == 'SELL':
            order = client.create_order(
                symbol='BTCUSDT',
                side='SELL',
                type='LIMIT',
                timeInForce='GTC',
                quantity=amount,
                price=price
            )
        elif side == 'BUY':
            order = client.create_order(
                symbol='BTCUSDT',
                side='BUY',
                type='LIMIT',
                timeInForce='GTC',
                quantity=amount,
                price=price
            )

        orders.append(order)
    return orders
