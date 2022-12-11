import hashlib
from dataclasses import dataclass
from enum import Enum
from typing import List


class WalletType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'


class Wallet: #Account class
    cash_amount: int
    wallet_type: WalletType

    def __init__(self, wallet_type: WalletType):
        self.wallet_type = wallet_type

@dataclass #при принте выходить как метод toString
class User: #BankAccount class
    username: str #name and surname
    __password: str
    wallets: Wallet

    def __init__(self, username: str):
        self.username = username

    def set_wallet(self,wallets:Wallet):#setter
        self.wallets=wallets

    @property #getter
    def wallets(self):
        return self.wallets

    def addToBankAccount(self,a:int):
        return self.addToBankAccount(a)

    def substractFromBankAccount(self, a:int):
        return self.substractFromBankAccount(a)

    def moneyConversion(self, ex_from, ex_to):
        match ex_from, ex_to:
            case 'USD', 'KZT':
                return self.wallets * 470
            case 'KZT', 'USD':
                return self.wallets / 470
            case 'EUR', 'KZT':
                return self.wallets * 480
            case 'KZT', 'EUR':
                return self.wallets / 480
            case _:
                return 'Invalid parametres'

    def filter_wallets(self, wallet_type: WalletType):
        return [w for w in self.wallets if w.wallet_type == wallet_type]

    def set_password(self, password: str):
        self.__password = self._hash_password(password)

    def check_password(self, password: str) -> bool:
        return self.__password == self._hash_password(password)

    @staticmethod
    def _hash_password(password: str):
        return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()

    def __repr__(self):
        return f'{self.username} {self.__password}'

    @wallets.setter
    def wallets(self, value):
        self._wallets = value
