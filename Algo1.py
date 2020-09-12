#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 01:01:46 2020

@author: Sauren Gupta

"""

# Import necesary libraries
import yfinance as yf
import datetime
import matplotlib.pyplot as plt

#Getting Current Date and End Date
from datetime import date
start_date = date.today()
end_date = start_date + datetime.timedelta(days=14) #change run-up period here

#Getting tickers from Yahoo Earnings Calendar
'''Optimize this by putting into file for the day'''
from yahoo_earnings_calendar import YahooEarningsCalendar
date_from = start_date
date_to = end_date
my_custom_delay_s = 0.5
yec = YahooEarningsCalendar(my_custom_delay_s)
print(yec.get_earnings_of('box'))
y = yec.earnings_between(date_from, date_to)
tickers={} #contains tickers we are looking at
for x in y:
    temp = x.get('ticker')
    tickers[temp] = {}
    tickers[temp]['name']=temp

#Historical Run-up
for ticker in tickers:
    ticker['run_up_dates'] = [] #NEED TO ACTUALLY PUT DATA, needs to be datetime
    average_increase = 0
    for date_temp in ticker['run_up_dates']:
        date1= date_temp - datetime.timedelta(days=14)
        date2= date_temp - datetime.timedelta(days=7)
        date3= date_temp
        data1 = float(yf.Ticker(ticker['name'] , start= date1)['price'])
        data2 = float(yf.Ticker(ticker['name'] , start= date2)['price'])
        data3 = float(yf.Ticker(ticker['name'] , start= date3)['price'])
        two_week_out_increase = 100*(data2/data1)-100
        one_week_out_increase = 100*(data3/data2)-100
        total_increase = 100*(data3/data1)-100
        average_increase+=total_increase/4
    ticker['average increase'] = average_increase
    if(average_increase < 5):
        tickers.pop(ticker)

#Sentiment
        
#Zacks ESP
        
#Zacks Earnings Growth
        
#Twitter Sentiment
        
#Internal Guidance
        
#Upward Estimate Revisions
        
#Call/Put Ratio
        
#Large Inflow Volume
        
#EMA(20)
        
#RSI
        
#Free-float
        
#IV - how
        
#Insider Trading Flashes
        
#Total Stock Gain over 7 days
        
#Forward Testing

















