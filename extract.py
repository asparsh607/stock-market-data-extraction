import requests
import pandas as pd

API_URL = "https://www.alphavantage.co/query" 
symbol = ['NVDA', 'INTC', 'TSM', 'AMD', 'QCOM', 'AVGO', 'MU', 'AMAT', 'ASX', 'ASML']
dflist = []

for index in range(len(symbol)):
  data = { "function": "TIME_SERIES_MONTHLY_ADJUSTED", 
  "symbol": symbol[index],
  "apikey": "O2R5AEY1P7AA6ONW" } 

  response = requests.get(API_URL, data) 
  response_json = response.json() # maybe redundant
  print(response_json)
  result_dict = response_json['Monthly Adjusted Time Series']
  res_list = []

  date_list = list(result_dict.keys())


  for dates in result_dict:
    res_list.append(result_dict[dates])
    res_list[-1]['Company'] = symbol[index]
      


  df = pd.DataFrame.from_dict(res_list)
  df.columns = ["Opening Price", "High", "Low", "Close", "Adjusted Close", "Volume", "Dividend Amount", "Company"]
  df['Date'] = date_list
  dflist.append(df)


for index in range(len(dflist)):
  dflist[index].to_csv(f'Data_{symbol[index]}.csv', index = True)
