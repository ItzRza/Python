from itertools import product
import os

passw = "9123"  # aradığımız şifre
numbers = "0123456789"

# Şifre uzunluğunu otomatik alıyoruz
length = len(passw)

# tüm kombinasyonları üret
for combo in product(numbers, repeat=length):
    attempt = ''.join(combo)
    print(attempt, flush=True)
    
    if attempt == passw:
        print("\n")
        print("Your password is:", attempt)
        break
