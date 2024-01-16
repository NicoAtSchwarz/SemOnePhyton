import re

transactionsList = [
        { "date": "yesterday", "amount": 100 },
        { "date": "2 days ago", "amount": -900 },
        { "date": "today", "amount": 500 },
        { "date": "yesterday", "amount": -50 }
]
def is_valid_date_format(date_string):
    return bool(re.compile(r"^\d{4} - ^\d{2} - ^\d{2}").match(date_string))

print(is_valid_date_format("2024.01.15"))

def transactionsDate(date):
    amountTransactionsOnDate = 0
    for item in transactionsList:
        if item["date"] == date:
            amountTransactionsOnDate+=1
    return amountTransactionsOnDate

def transactionsAmount(date):
    transactionsOnDate = 0
    for item in transactionsList:
        if item["date"] == date:
            transactionsOnDate+=item["amount"]
    return transactionsOnDate

print(transactionsDate("yesterday"))
print(transactionsAmount("yesterday"))

# find all with key and keyvalue
def find_all(key, key_value):
    myFinds=[]
    for item in transactionsList:
        if item[key] == key_value:
            myFinds.append(item)
    return myFinds

my_transactions = find_all("date", "yesterday")
print(my_transactions)
print(len(my_transactions))