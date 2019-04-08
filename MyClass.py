import logging


class itemMd001:
    def __init__(self,SecurityID=' ',Symbol=' ',TradeVolume=0,TotalValueTraded=0,PreClosePx=0,OpenPrice=0,HighPrice=0,
                 LowPrice=0,TradePrice=0,ClosePx=0,TradingPhaseCode=' ',Timestamp=' ',*arg):
        self.SecurityID=SecurityID
        self.Symbol=Symbol
        self.TradeVolume=TradeVolume
        self.TotalValueTraded=TotalValueTraded
        self.PreClosePx=PreClosePx
        self.OpenPrice=OpenPrice
        self.HighPrice=HighPrice
        self.LowPrice=LowPrice
        self.TradePrice=TradePrice
        self.ClosePx=ClosePx
        self.TradingPhaseCode=TradingPhaseCode
        self.Timestamp=Timestamp
        self.arg=arg
    pass

class itemMdElse:
    def __init__(self,SecurityID=' ',Symbol=' ',TradeVolume=0,TotalValueTraded=0,PreClosePx=0,OpenPrice=0,HighPrice=0,
                LowPrice=0,TradePrice=0,ClosePx=0,BuyPrice1=0,BuyVolume1=0,SellPrice1=0,SellVolume1=0,BuyPrice2=0,BuyVolume2=0,SellPrice2=0,
                SellVolume2=0,BuyPrice3=0,BuyVolume3=0,SellPrice3=0,SellVolume3=0,BuyPrice4=0,BuyVolume4=0,SellPrice4=0,SellVolume4=0,
                BuyPrice5=0,BuyVolume5=0,SellPrice5=0,SellVolume5=0,TradingPhaseCode=' ',Timestamp=' ',*arg):
        self.SecurityID=SecurityID
        self.Symbol=Symbol
        self.TradeVolume=TradeVolume
        self.TotalValueTraded=TotalValueTraded
        self.PreClosePx=PreClosePx
        self.OpenPrice=OpenPrice
        self.HighPrice=HighPrice
        self.LowPrice=LowPrice
        self.TradePrice=TradePrice
        self.ClosePx=ClosePx
        self.BuyPrice1=BuyPrice1
        self.BuyVolume1=BuyVolume1
        self.SellPrice1=SellPrice1
        self.SellVolume1=SellVolume1
        self.BuyPrice2=BuyPrice2
        self.BuyVolume2=BuyVolume2
        self.SellPrice2=SellPrice2
        self.SellVolume2=SellVolume2
        self.BuyPrice3=BuyPrice3
        self.BuyVolume3=BuyVolume3
        self.SellPrice3=SellPrice3
        self.SellVolume3=SellVolume3
        self.BuyPrice4=BuyPrice4
        self.BuyVolume4=BuyVolume4
        self.SellPrice4=SellPrice4
        self.SellVolume4=SellVolume4
        self.BuyPrice5=BuyPrice5
        self.BuyVolume5=BuyVolume5
        self.SellPrice5=SellPrice5
        self.SellVolume5=SellVolume5
        self.TradingPhaseCode=TradingPhaseCode
        self.Timestamp=Timestamp
        self.arg=arg
    pass



format_dict = {
   1: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   2: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   3: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   4: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   5: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
}


class Logger():
    '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''
    def __init__(self, logDir, loglevel,loggerName):


        # 创建一个logger
#       logging.getLogger([name])
# 　　  返回一个logger实例，如果没有指定name，返回root logger。只要name相同，返回的logger实例都是同一个而且只有一个，
#       即name和logger实例是一一对应的。这意味着，无需把logger实例在各个模块中传递。只要知道name，
#       就能得到同一个logger实例。
        self.logger = logging.getLogger(loggerName)
        self.logger.setLevel(logging.DEBUG)
#级别高低顺序：NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logDir)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        #ch = logging.StreamHandler()
        #ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = format_dict[int(loglevel)]
        fh.setFormatter(formatter)
        #ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        #self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


# class InitSqlite():
#     def __init__(self):
