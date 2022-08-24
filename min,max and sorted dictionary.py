stock={"amazon":200,
       "tcs":350,
       "microsoft":455,
       "infosys":310,
       "google":415}
print('Minimum stock value -> ',(min(zip(stock.values(),stock.items()))))
print('Maximum stock value -> ',(max(zip(stock.values(),stock.items()))))
print('Sorted according to value ->',(sorted(zip(stock.values(),stock.items()))))
#print('Sorted according to Items ->'(sorted(zip(stock.items(),stock.values()))))
