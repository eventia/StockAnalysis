import win32com.client

def CheckVolumn(instStockChart, code):
    # SetInputValue
    instStockChart.SetInputValue(0, code)
    instStockChart.SetInputValue(1, ord('2'))
    instStockChart.SetInputValue(4, 60)
    instStockChart.SetInputValue(5, 8)
    instStockChart.SetInputValue(6, ord('D'))
    instStockChart.SetInputValue(9, ord('1'))

    # BlockRequest
    instStockChart.BlockRequest()

    # GetData
    volumes = []
    numData = instStockChart.GetHeaderValue(3)
    for i in range(numData):
        volume = instStockChart.GetDataValue(0, i)
        volumes.append(volume)

    # Calculate average volume
    averageVolume = (sum(volumes) - volumes[0]) / (len(volumes) -1)

#    if(volumes[0] > averageVolume * 10):
    if(volumes[0] > averageVolume * 3):
#        return 1
        return (volumes[0]/ averageVolume, volumes[1]/ averageVolume, volumes[2] / averageVolume )
    else:
        return 0

if __name__ == "__main__":
    instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
    codeList = instCpCodeMgr.GetStockListByMarket(1)
    buyList = []

    iter = 0
    for code in codeList:
        checkVolumn = CheckVolumn(instStockChart, code)
        if checkVolumn != 0:
            iter = iter + 1
            buyList.append(code)
            print(code, end=", ")
            stockIndex = instCpStockCode.CodeToIndex(code)
            print(instCpStockCode.GetData(1, stockIndex), end=", ")
            print(checkVolumn[0], checkVolumn[1], checkVolumn[2] )
            if iter == 5:
                break
