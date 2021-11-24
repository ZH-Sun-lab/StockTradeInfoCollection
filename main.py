import src.StockTradingInfoCollect as stc

if __name__ == '__main__':
    config = {
        "name" : "SunZH"
    }

    collection = stc.StockTrading(config)
    collection.start()