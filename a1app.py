""""
User Interface
"""
import a1
old = input("Enter original currency: ")
new = input("Enter desired currency: ")
amt = float(input("Enter original amt: "))
result = a1.exchange(old,new,amt)
print(f"You can exchange {amt} {old} for {result} {new}.")