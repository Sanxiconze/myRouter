def getdataDict():
    file = 'C:\\Users\\sanxiconze\\Desktop\\2018-11-29\\20181122.shan_ge'
    dict = {}
    timedict={}
    with open(file,"r")as f:
        oldtimes = ""
        while True:

            str = f.readline()
            if not str:break
            mac = str.split(" ")[-1]
            times = str.split(" ")[0]+" "+str.split(" ")[1]
            if not mac[:-1] in dict.keys():
                dict[mac[:-1]]=1
            else:
                dict[mac[:-1]]+=1


            #下一次
            if oldtimes!=times:
                for macInList in timedict.copy():
                    timedict[macInList][1] -= 1
                    if timedict[macInList][1] <= 0:
                        timedict.pop(macInList)
            oldtimes = times

            #下面不在在线列表内
            if not mac[:-1] in timedict.keys():
                timeList = [times,10]
                timedict[mac[:-1]] =timeList
            else:
                #timeList = [times, 10]
                timedict[mac[:-1]][1] = 10

    f.close()

    return dict,timedict
def getNameDict():
    file = 'C:\\Users\\sanxiconze\\Desktop\\2018-11-29\\maclist.sg'
    nameDict = {}
    with open(file, "r")as f:
        while True:
            str = f.readline()
            if not str: break
            mac  = str.split(" ")[0]
            name = str.split(" ")[-1][:-1]
            nameDict[mac] = name
    f.close()
    return nameDict
def getsortList(dataDict,nameDict):
    dataList = []
    for key in dataDict.keys():
        name = nameDict[key]
        sum = dataDict[key]
        sumTime = str(sum//60)+"小时"+str(sum%60)+"分钟"
        print(name+"\t:   "+sumTime)
        dataList.append((name,sumTime))
    #print(dataList)
    dataLista = sorted(dataList,key = lambda x:x[1],reverse=True)
    #print(dataLista)
    return dataLista

def selectTime(time):
    timeLen = len(time)
    file = 'C:\\Users\\sanxiconze\\Desktop\\2018-11-29\\20181122.shan_ge'
    timeList = []
    with open(file, "r")as f:
        timeList = f.readlines()
    f.close()
    for timeMac in timeList:
        if (timeMac[0:timeLen])== time:
            mac = timeMac[-18:-1]
            nameDict = getNameDict()
            print(nameDict[mac],end="")
            print("在线\t:",end = "")
            print(timeMac[:-1])
    #print(timeList)
    pass

def main():
    dataDict,timeDict= getdataDict()
    nameDict = getNameDict()
    sortList = getsortList(dataDict,nameDict)
    print("最长时间："+str(sortList[0]))
    print("最短时间：" + str(sortList[-1]))
    print("请输入时间：",end = "")
    print (timeDict)
    time = input()
    selectTime(time)
main()
