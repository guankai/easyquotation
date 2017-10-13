import easyquotation
quotation = easyquotation.use('sina')
data = quotation.market_snapshot(prefix=True) 
print(data)
