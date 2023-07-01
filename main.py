import aiohttp
import asyncio
from datetime import datetime, timedelta
import sys

class Currency_exchange():
        
    async def exchange(self, date):
        self.link = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
        async with aiohttp.ClientSession() as session:
            async with session.get(self.link) as response:
                result = await response.json()
                return result
        

async def main(value = 0):
    if value >= 10:
        value = 10
    cur_ex_obj = Currency_exchange()
    date_lst = [f'{str(datetime.now().date()-timedelta(days=number_day)).split("-")[2]}.{str(datetime.now().date()-timedelta(days=number_day)).split("-")[1]}.{str(datetime.now().date()).split("-")[0]}'                  for number_day in range(0, value+1)]
    result = []
    
    for date in date_lst:
        
        
        data_PB = await (cur_ex_obj.exchange(date))
        res_dict = {}
        for data in data_PB['exchangeRate']:
            
            if data['currency'] == 'USD':
               
                res_dict.update({'USD':{'sale': data['saleRate'], 'purchase':data['purchaseRate'] }})
            elif data['currency'] == 'EUR':
               
                res_dict.update({'EUR':{'sale': data['saleRate'], 'purchase':data['purchaseRate'] }})

        result.append({date:res_dict})

    print(result)

        
        
    


        

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        val = sys.argv[1]
        asyncio.run(main(int(val)))
    except:
        asyncio.run(main())

    
    
    




