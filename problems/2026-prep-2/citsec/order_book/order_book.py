import heapq
from collections import deque
from dataclasses import dataclass, field
from enum import Enum

class Side(Enum):
    BUY = "B"
    SELL = "S"

    @property
    def opposite(self) -> "Side":
        return Side.SELL if self is Side.BUY else Side.BUY


class TIF(Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"


@dataclass
class Order:
    order_id: int
    side: Side
    price: int
    quantity: int
    remaining: int
    seq: int
    active: bool = True


@dataclass(frozen=True)
class Fill:
    taker_id: int
    maker_id: int
    price: int
    quantity: int


@dataclass
class Level:
    price: int
    orders: deque = field(default_factory=deque)
    total: int = 0  # live quantity at this price


class OrderBook:
    def __init__(self):
        self.levels = {Side.BUY: {}, Side.SELL: {}}   # side -> price -> Level
        self.heaps = {Side.BUY: [], Side.SELL: []}
        self.orders: dict[int, Order] = {} # live orders by id.
        self._seq = 0


    def best(self, side: Side):
        """ best live price on a side, or None. Pops stale heap entries """
        heap = self.heaps[side]
        while heap:
            # if we use a min_heap for both buy and sell, the below line for price will be:
            # price = -heap[0] if side is Side.BUY else heap[0]
            price = heap[0]
            level = self.level[side].get(price)
            if level and level.total > 0:
                return price

            heapq.heappop(heap) if side is Side.SELL else heapq.heappop_max(heap)
            self.levels[side].pop(price, None)
        return None


    # TODO: Look into this carefully. This is sleek but is it useful in 
    # an interview.
    def depth(self, side: Side, n: int = 5):
        """ Top n (price, total_quantity) on a side. L2 view """
        prices = sorted((p for p, lv in self.levels[side].items() if lv.total > 0), reverse=side is Side.BUY)
        return [(p, self.levels[side][p].total) for p in prices[:n]]


    def submit(self, order_id: int, side: Side, quantity: int, price: int | None = None, tif: TIF = TIF.GTC) -> list[Fill]:
        if order_id in self.orders:
            raise ValueError(f"duplicate order id {order_id}")
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if price is not None and price <= 0:
            raise ValueError("price must be positive")
        if price is None and tif is TIF.GTC:
            tif = TIF.IOC
            
        self._seq += 1
        order = Order(order_id, side, price, quantity, remaining=quantity, seq=self._seq)
        
        if tif is TIF.FOK and self._fillable(order) < quantity:
            return []
        
        fills = self._match(order)
        if order.remaining > 0 and tif is TIF.GTC:
            self._rest(order)
        return fills
    
    def cancel(self, order_id: int) -> bool:
        order = self.orders.pop(order_id, None)
        if order is None:
            return False
        order.active = False
        self.levels[order.side][order.price].total -= order.remaining
        order.remaining = 0
        return True
    
    def modify():
        pass
    
    def _crosses(self, order: Order, best_opposite: int) -> bool:
        if order.price is None:
            return True
        
        if order.side is Side.BUY:
            return order.price >= best_opposite
        return order.price <= best_opposite
    
    
    def _match(self, order: Order) -> list[Fill]:
        fills = []
        opposite = order.side.opposite
        while order.remaining > 0:
            best = self.best(opposite)
            
            if best is None or not self._crosses(order, best):
                break
            level = self.levels[opposite][best]
            while order.remaining > 0 and level.orders:
                maker = level.orders[0]
                if not maker.active:
                    level.orders.popleft()
                    continue
                quantity = min(order.remaining, maker.remaining)
                fills.append(Fill(order.order_id, maker.order_id, best, quantity))
                order.remaining -= quantity
                maker.remaining -= quantity
                level.total -= quantity
                if maker.remaining == 0:
                    maker.active = False
                    level.orders.popleft()
                    del self.orders[maker.order_id]
                    
        return fills
    
    
    def _fillable(self, order: Order) -> int:
        pass
    
    def _rest(self, order: Order) -> None:
        levels = self.levels[order.side]
        level = levels.get(order.price)
        
        heap_push_func = heapq.heappush_max if order.side is Side.SELL else heapq.heappush
        if level is None:
            level = levels[order.price] = Level(order.price)
            heap_push_func(self.heaps[order.side], order.price)
        elif level.total == 0:
            heap_push_func(self.heaps[order.side], order.price)
            
        level.orders.append(order)
        level.total += order.remaining
        self.orders[order.order_id] = order
