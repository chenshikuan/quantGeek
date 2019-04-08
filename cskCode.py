import time
import sqlite3
import logging
import logging.handlers
import datetime
# from MyClass import Logger


def myLogging():
    # logDebug = Logger("./log/logDebug.txt", 4, "logD").getlog()
    # logError = Logger("./log/logError.txt", 4, "logE").getlog()
    mylogger = logging.getLogger("mylogger")
    mylogger.setLevel(level=logging.DEBUG)

    allLog=logging.handlers.RotatingFileHandler("./log/logDebug.txt",maxBytes=102400000,backupCount=5)
    allLog.setLevel(level=logging.DEBUG)
    allLog.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    errorLog=logging.handlers.RotatingFileHandler("./log/logError.txt",maxBytes=100,backupCount=5)
    errorLog.setLevel(level=logging.ERROR)
    errorLog.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    mylogger.addHandler(allLog)
    mylogger.addHandler(errorLog)
    return mylogger



#更新数据库
def processData(lines,c,mylogger):

    listdatas = []
    for line in lines:
        mylogger.debug("原始样本："+str(line))
        line = line.split('|')
        if (line[0] == 'MD002'):
            # 是股票行情
            line[32]=line[32].rstrip('\n')
            mylogger.debug("经过处理后的样本："+str(line))
            c.execute("select SecurityID,TradePrice,Timestamp from T_stockTable where SecurityID=" + line[
                1] + " order by Timestamp DESC limit 1")
            # 查看数据库中是否有对应的股票代码
            row = c.fetchone()
            if (row is not None):  # 该股票信息在数据库中存在
                try:
                    if (row[2] != line[32]):
                        # 时间戳不同，计算增长率，将该股票最新行情插入数据库
                        p = (line[9] - row[1]) / row[1] * 100
                        line.insert(32, p)
                        listdatas.append(tuple(line))
                except Exception as e:
                    mylogger.error("数据库已存在的问题数据：---row:"+str(row)+"---line:"+str(line)+"--"+str(e))
            else:  # 该股票信息在数据库中不存在，直接插入数据库，增长率为0
                try:
                    line.insert(32, 0)
                    listdatas.append(tuple(line))
                except Exception as e:
                    mylogger.error("数据库中为存在的问题数据："+str(line)+"--"+str(e))
    if(len(listdatas)>0):
        try:
            c.executemany(
                "insert into T_stockTable values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                listdatas)
            conn.commit()
        except Exception as e:
            mylogger.error("数据插入数据库失败："+str(e))



def readData(fpath,conn):
    mylogger=myLogging()
    c=conn.cursor()
    k=0
    while('15:01:00'!=time.strftime('%H:%M:%S',time.localtime(time.time()))):
        k=k+1
        starttime = datetime.datetime.now()
        try:
            file_to_read=open(fpath, 'r')
            lines = file_to_read.readlines()
        except IOError:
            mylogger.error("打开文件"+fpath+"失败或不能读取："+str(IOError),exc_info=True, stack_info=True)
        else:
            file_to_read.close()
        processData(lines,c,mylogger)
        endtime = datetime.datetime.now()
        print("第"+str(k)+"次扫描、更新数据库耗时："+str((endtime - starttime).seconds)+"秒")
        time.sleep(0.015)
    conn.close()





if __name__=="__main__":
    conn = sqlite3.connect("file:memDB1?mode=memory&cache=shared", check_same_thread=False, uri=True)
    c = conn.cursor()
    c.execute('''CREATE TABLE T_stockTable(
                 MDStreamID CHAR(5) not null,
                 SecurityID char(6),
                 Symbol char(8),
                 TradeVolume bigint,
                 TotalValueTraded double,
                 PreClosePx double,
                 OpenPrice double,
                 HighPrice double,
                 LowPrice double,
                 TradePrice double,
                 ClosePx double,
                 BuyPrice1 double,
                 BuyVolume1 bigint,
                 SellPrice1 double,
                 SellVolume1 bigint,
                 BuyPrice2 double,
                 BuyVolume2 bigint,
                 SellPrice2 double,
                 SellVolume2 bigint,
                 BuyPrice3 double,
                 BuyVolume3 bigint,
                 SellPrice3 double,
                 SellVolume3 bigint,
                 BuyPrice4 double,
                 BuyVolume4 bigint,
                 SellPrice4 double,
                 SellVolume4 bigint,
                 BuyPrice5 double,
                 BuyVolume5 bigint,
                 SellPrice5 double,
                 SellVolume5 bigint,
                 TradingPhaseCode char(8),
                 GrowthRate REAL DEFAULT 0,
                 Timestamp char(20));''')
    conn.commit()
    fpath="data/mktdt00.txt"
    readData(fpath,conn)