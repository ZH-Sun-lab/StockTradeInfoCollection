import src.StockTradingInfoCollect as stc

if __name__ == '__main__':
    config = {

    }

    collection = stc.StockTrading(config)
    collection.start()