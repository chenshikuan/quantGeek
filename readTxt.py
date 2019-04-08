
from MyClass import itemMd001
from MyClass import itemMdElse
from MyClass import Logger
import time
import os
dataList=[]
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
#         print(root) #当前目录路径
#         print(dirs) #当前路径下所有子目录
        return files #当前路径下所有非目录子文件
def readData(fpath):
    k=0
    logDebug=Logger("./log/logDebug.txt",4,"logD").getlog()
    logError=Logger("./log/logError.txt",4,"logE").getlog()
    while('15:01:00'!=time.strftime('%H:%M:%S',time.localtime(time.time()))):

        try:
            file_to_read=open(fpath, 'r')
            lines = file_to_read.readlines()
            k+=1
            print("第"+str(k)+"读取"+str(len(lines))+"行")
        except IOError:
            logError.info("打开文件"+fpath+"失败或不能读取："+str(IOError))
        else:
            file_to_read.close()
        for line in lines:
            line = line.split('|')
            if (line[0] == 'MD001'):
                try:
                    temp = itemMd001(line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9],
                                     line[10],
                                     line[11], line[12])
                except IndexError:
                    logError.info(str(IndexError))
                dataList.append(temp)

            elif (line[0] == 'MD002' or line[0] == 'MD003' or line[0] == 'MD004'):
                try:
                    temp = itemMdElse(line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9],
                                  line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17],
                                  line[18], line[19], line[20], line[21], line[22], line[23], line[24], line[25],
                                  line[26], line[27], line[28], line[29], line[30], line[31], line[32])
                except IndexError:
                    logError.info(str(IndexError))
                dataList.append(temp)
            else:
                logDebug.info("问题样本："+str(line))
        time.sleep(0.03)






if __name__=="__main__":
    fpath="data/mktdt00.txt"
    print(readData(fpath))





