from iexfinance.stocks import Stock

company = Stock('TSLA', token='pk_34947d6f20564c52a9dcd62bf4d4ab5f')
print(company.get_quote())
