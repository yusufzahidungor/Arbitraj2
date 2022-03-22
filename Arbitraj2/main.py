from ccxt.base import exchange
import ccxt
from ccxt.btcturk import btcturk
from ccxt.coinbasepro import coinbasepro
import sqlite3 
import pandas as pd

dict = {0 : 'Binance', 1 : 'BtcTurk', 2 : 'CoinbasePro', 3 : 'Ftx', 4 : 'Kraken', 5 :  'Huobi', 6 : 'Kucoin', 7 :  'Bitfinex', 8 : 'GateIo'}

Binance_Exchange = ccxt.binance()
BTCTurk_Exchange = ccxt.btcturk()
Coinbasepro_Exchange = ccxt.coinbasepro()

binance_maker = 0.1
binance_taker = 0.1
btcTurk_maker = 0.05
btcTurk_taker = 0.09
money = 100
komisyonFee = 0.1

def karsilastir():
    data = [["BTC","Bitcoin",0.0005,0],
            ["ETH","ERC20",0.005,0.007],
            ["AAVE","ERC20",0.37,0.1629],
            ["ADA","Cardano",1,1],
            ["ANKR","ERC20",306,268.4465],
            ["ATOM","Cosmos",0.005,0.005],
            ["AVAX","Avalanche",0.01,0.001],
            ["AXS","ERC20",0.33,0.2730],
            ["BAT","ERC20",26,23.6464],
            ["CHZ","ERC20",107,94.6960],
            ["COMP","ERC20",0.16,0.13689229],
            ["DASH","Dash",0.002,0.002],
            ["DOGE","dogecoin",5,2],
            ["DOT","Polkadot",0.1,0.1],
            ["ENJ","ERC20",12,10.8818],
            ["EOS","Eos",0.1,0.1],
            ["FET","ERC20",59,51.9673],
            ["FIL","Filecoin",0.001,0.001],
            ["FTM","ERC20",21,19.0637],
            ["GALA","ERC20",72,64.4678],
            ["GRT","ERC20",49,42.5876],
            ["LINK","ERC20",0.512,1.3823],
            ["LRC","ERC20",14,12.5385],
            ["LTC","Litecoin",0.001,0.001],
            ["MANA","ERC20",9.13,8.1275],
            ["MATIC","ERC20",9.72,12.7200],
            ["MKR","ERC20",0.013,0.0112],
            ["NEO","NEO",0,0.0250],
            ["NU","ERC20",43,38.6024],
            ["OMG","ERC20",4.91,4.4054],
            ["POLY","ERC20",58,52.1901],
            ["SAND","ERC20",6.52,5.6840],
            ["SHIB","ERC20",945529,828.164],
            ["SNX","ERC20",10,5.095444],
            ["SOL","Solana",0.01,0.0001],
            ["STORJ","ERC20",18,16.2901],
            ["STX","Stacks",1.5,0.0002],
            ["TRX","TRON",1,1],
            ["UMA","ERC20",3.35,2.7839],
            ["UNI","ERC20",2,1.7205],
            ["XLM","Stellar Lumens",0.02,0.02],
            ["XRP","Ripple",0.25,0.02],
            ["XTZ","Tezos",0.1,0.1]]
    df = pd.DataFrame(data , columns=["Sembol","Gonderim Turu","Binance","BtcTurk"])
    # print(df)
    borsa(df)
    
   
    

class Binance():
    def bid(sembol):
        return Binance_Exchange.fetch_ticker(sembol+"/USDT")["bid"]

class BTCTurk():
    def bid(sembol):
        return BTCTurk_Exchange.fetch_ticker(sembol+"/USDT")["bid"]

class Coinbasepro():
    def btc():
        return Coinbasepro_Exchange.fetch_ticker("BTC/USDT")["bid"]

def kar(Borsa1,Borsa1name,Borsa2,Borsa2name,df,i):
    if Borsa1 > Borsa2:
        max = Borsa1
        maxBorsaName = Borsa1name
        min = Borsa2
        minBorsaName = Borsa2name

        brut_kar = ((max-min)/min)*100
        brut_gelir = money + (money*brut_kar)

        a = df["Binance"][i]
        minBorsaFeeGider = money*komisyonFee
        cryptoMin = money/min
        gönderimUcreti = a*money
        moneyMax = cryptoMin*max
        maxBorsaFeeGider = moneyMax*komisyonFee
        giderToplam = minBorsaFeeGider+gönderimUcreti+maxBorsaFeeGider

    else:
        max = Borsa2
        maxBorsaName = Borsa2name
        min = Borsa1
        minBorsaName = Borsa1name
        brut_kar = ((max-min)/min)*100
        brut_gelir = money + (money*brut_kar)

        a = df["BtcTurk"][i]
        minBorsaFeeGider = money*komisyonFee
        cryptoMin = money/min
        gönderimUcreti = a*money
        moneyMax = cryptoMin*max
        maxBorsaFeeGider = moneyMax*komisyonFee
        giderToplam = minBorsaFeeGider+gönderimUcreti+maxBorsaFeeGider


    net_gelir = brut_gelir - giderToplam
    net_kar = ((brut_gelir-net_gelir)/net_gelir)*100

    print("***"+df["Sembol"][i]+"***"+minBorsaName+"-"+str(min)+"-"+maxBorsaName+"-"+str(max)+"---"+str(brut_kar)+"-"+str(brut_gelir)+"-"+str(net_kar)+"-"+str(net_gelir))
    
    # a=1
    # for i in range(len(list)):        
    #     for j in range(a,len(list)):
    #         if list[i] > list[j]:
    #             max = list[i]
    #             max_index = i
    #             min = list[j]
    #             min_index = j
    #         elif list[i] < list[j]:
    #             max = list[j]
    #             max_index = j
    #             min = list[i]
    #             min_index = i
    #         else:
    #             pass
    #         brut_kar = ((max-min)/min)*100
    #         brut_gelir = money + (money*brut_kar)
    #         gider1 = 0
    #         gider2 = 0
    #         gider3 = 0
    #         if min_index == 0:
    #             gider1 = money*binance_taker
    #             gider2 = min*df["Binance"][i]
    #             gider3 = money*btcTurk_maker
    #             gider = gider1+gider2+gider3
    #         elif min_index == 1:
    #             gider1 = money*btcTurk_taker
    #             gider2 = min*df["BtcTurk"][i]
    #             gider3 = money*binance_maker
    #             gider = gider1+gider2+gider3

    #         net_gelir = brut_gelir - gider
    #         if brut_gelir > net_gelir:
    #             net_kar = ((brut_gelir-net_gelir)/net_gelir)*100
    #         elif brut_gelir < net_gelir:
    #             net_kar = ((net_gelir-brut_gelir)/brut_gelir)*100
    #         sss = df["Sembol"][i]
    #         print("***"+sembol+"***"+dict[min_index]+"-"+str(min)+"-"+dict[max_index]+"-"+str(max)+"-"+str(brut_kar)+"-"+str(brut_gelir)+"-"+str(net_kar)+"-"+str(net_gelir))
    #     a+=1

def borsa(df):
    for i in range(len(df["Sembol"])):
        listt = []
        Borsa1 = Binance.bid(df["Sembol"][i])
        Borsa2 = BTCTurk.bid(df["Sembol"][i])
        kar(Borsa1,"Binance",Borsa2,"BtcTurk",df,i)


if __name__ == "__main__":
    karsilastir()
    
