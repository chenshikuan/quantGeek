import cskCode
import sqlite3
import threading



def readsqlite(conn):
    c=conn.cursor()
    while(1):
        c.execute("select * from T_stockTable")
        alist=c.fetchall()
        print("sun:"+str(len(alist)))
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

t1=threading.Thread(target=cskCode.readData,args=(fpath,conn))
# cskCode.readData(fpath,conn)
t2=threading.Thread(target=readsqlite,args=(conn,))
t1.start()
t2.start()
t1.join()
t2.join()