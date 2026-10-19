

class OrderBook:

    def __init__(self):
        self.orders = {}

    # side - BUY or SELL
    # order_id - unique integer
    # price - limit price
    # quantity - +ve integer.
    def add_order(self, side, price, quantity, order_id):


        # if side == 'buy':
        #     if price not in self.buy_orders:
        #         self.buy_orders[price] = {}
        #     self.buy_orders[price][order_id] = quantity
        # elif side == 'sell':
        #     if price not in self.sell_orders:
        #         self.sell_orders[price] = {}
        #     self.sell_orders[price][order_id] = quantity
        self.orders[order_id] = {
            'price': price,
            'quantity': quantity,
            'side': side.lower(),
        }
        

    def modify_order(self, order_id, price, quantity): 
        if order_id in self.orders:
            self.orders[order_id]['price'] = price
            self.orders[order_id]['quantity'] = quantity


    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]

    def display_book(self):
        bids = []
        asks = []

        for order_id, details in self.orders.items():
            order_record = {
                'order_id': order_id,
                'price': details['price'],
                'quantity': details['quantity']
            }

            if details['side'] == 'buy':
                bids.append(order_record)
            else:
                asks.append(order_record)

        bids.sort(key=lambda x: x['price'], reverse=True)
        asks.sort(key=lambda x: x['price'])
        return {
            "buy": bids,
            "sell": asks
        }

    
    # def best_bid():
    #     pass

    # def best_ask():
    #     pass

    # def top_of_book_volume():
    #     pass

import heapq
from typing import List

# Limit order book matching engine
# system receives N limit orders in sequence.
# When an incoming order arrives, it first matches against eligible resting orders already in the book 
# A buy order can trade with sell orders prices <= it's limit price
# A sell order can trade with buy orders prices >= it's limit price
# Buy orders consume the lowest ask first; sell orders consume the highest bid first. 
# At the same price, orders are matched in price-time priority (FIFO).
# The execution price is the price of the resting order.
# An order may be partially filled and may match multiple counterparties.
# Any unfilled portion of the incoming order becomes a resting order in the book.

# This order can produce a trade, then we print something, else if no trade, don't print anyting
# TRADE buy_order_id sell_order_id execution_price execution_quantity

# Input orders is a stream of buy, sell orders we have to match. 
# Each order is in the form "BUY 1 100 10" or "SELL 2 105 5"
def match_orders(orders: List[str]):

    bids = [] # max heap for resting BUY orders
    asks = [] # min heap for resting SELL orders

    idx = 0
    seq_num = 0
    while idx < len(orders):
        side, order_id, price, quantity = orders[idx].split()
        price = int(price)
        quantity = int(quantity)
        idx += 1

        if side == "BUY":

            while quantity > 0 and asks:
                best_ask = asks[0]
                ask_price, _, ask_order_id, ask_quantity = best_ask

                if ask_price > price:
                    break

                # Match found
                trade_quantity = min(quantity, ask_quantity)
                print(f"TRADE {order_id} {ask_order_id} {ask_price} {trade_quantity}")

                quantity -= trade_quantity
                best_ask[3] -= trade_quantity

                if best_ask[3] == 0:
                    heapq.heappop(asks)


            if quantity > 0:
                heapq.heappush_max(bids, [price, seq_num, order_id, quantity])
        else: # side == "SELL"
            while quantity > 0 and bids:
                best_bid = bids[0]
                bid_price, _, bid_order_id, bid_quantity = best_bid

                if bid_price < price:
                    break

                trade_quantity = min(quantity, bid_quantity)
                print(f"TRADE {bid_order_id} {order_id} {bid_price} {trade_quantity}")

                quantity -= trade_quantity
                best_bid[3] -= trade_quantity

                if best_bid[3] == 0:
                    heapq.heappop_max(bids)

            if quantity > 0:
                heapq.heappush(asks, [price, seq_num, order_id, quantity])

        seq_num += 1

if __name__ == "__main__":
    orders = [
        "BUY 1 100 10",
        "SELL 2 105 5",
        "SELL 3 99 6",
        "BUY 4 110 3"
    ]
    match_orders(orders)