import threading

from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def is_valid(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:

        if not self.is_valid(account1) or not self.is_valid(account2):
            return False

        if self.balance[account1 - 1] < money:
            return False
        
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money

        return True
    
    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False
        
        self.balance[account - 1] += money
        return True
    
    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False
        
        if self.balance[account - 1] < money:
            return False
        
        self.balance[account - 1] -= money
        return True
    

class ThreadSafeBank:

    def __init__(self, balance: List[int]) -> None:
        self.balance = balance
        self.locks = [threading.Lock() for _ in range(len(balance))]

    def is_valid(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)
    
    def transfer(self, account1: int, account2: int, money:int) -> bool:
        if not self.is_valid(account1) or not self.is_valid(account2):
            return False
        
        first_lock_id = min(account1, account2) - 1
        second_lock_id = max(account1, account2) - 1

        if first_lock_id == second_lock_id:
            return True
        
        with self.locks[first_lock_id]:
            with self.locks[second_lock_id]:

                if self.balance[account1 - money] < money:
                    return False
                
                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money
                return True
            
