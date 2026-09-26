from ..bank.account import show_balance
from ..bank.fees import apply_fee
from .calculator import deposite


balance = 1000

print(show_balance(balance))

balance = deposite(balance, 500)

print(show_balance(balance))

balance = apply_fee(balance, 50)

print(show_balance(balance))