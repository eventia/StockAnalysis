# import win32com.client
# // 연결유무를 묻는다
# instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
# print(instCpCybos.IsConnect)

# // 상장된 주식의 수
# instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
# stockNum = instCpStockCode.GetCount()
# print(instCpStockCode.GetCount())

# // GetData(p1,p2)
# p1 : 0,1,2 중 하나 종목코드, 종목명, FullCode
# p2 : 인덱스 번호

# print(instCpStockCode.GetData(0,0))
# print(instCpStockCode.GetData(1,0))
# print(instCpStockCode.GetData(2,0))

# for i in range(0, 10):
#     print(instCpStockCode.GetData(1,i))

# // NAVER 검색하기
# for i in range(stockNum):
#     if instCpStockCode.GetData(1, i) == 'NAVER':
#         print(instCpStockCode.GetData(0,i))
#         print(instCpStockCode.GetData(1,i))
#         print(i)

# // 종목명을 넣어서 종목코드를 구하기 NameToCode
# naverCode = instCpStockCode.NameToCode('NAVER')
# naverIndex = instCpStockCode.CodeToIndex(naverCode)
# print("NAVER CODE = ", naverCode)
# print("NAVER INDEX= ", naverIndex)
# print(instCpStockCode.CodeToIndex('A003540'))
#
# print("A003540 = ", instCpStockCode.GetData(1,instCpStockCode.CodeToIndex('A003540')))
# //
# instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
# codeList = instCpCodeMgr.GetStockListByMarket(1)
# print(len(codeList))
# print(codeList)
# kospi = {}
# for code in codeList:
#     name = instCpCodeMgr.CodeToName(code)
#     kospi[code] = name

## https://wikidocs.net/3686 10. 대신증권 API >> 3) 기본API익히기 >> 1)종목코드가져오기
# instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
# codeList = instCpCodeMgr.GetStockListByMarket(1)
#
# kospi = {}
# for code in codeList:
#     name = instCpCodeMgr.CodeToName(code)
#     kospi[code] = name
#
# f = open('C:\\Dev\\wikidocs_2847\\aa\\kospi.csv', 'w')
# for key, value in kospi.items():
#     f.write("%s,%s\n" % (key, value))
# f.close()

# // https://wikidocs.net/3686 10. 대신증권 API >> 3) 기본API익히기 >> 1)종목코드가져오기
# import win32com.client
#
# instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
# codeList = instCpCodeMgr.GetStockListByMarket(1)
#
# for i, code in enumerate(codeList):
#     secondCode = instCpCodeMgr.GetStockSectionKind(code)
#     name = instCpCodeMgr.CodeToName(code)
#     print(i, code, secondCode, name)

# 과거데이터 구하기 https://wikidocs.net/3686 :: 10-3-2
# import win32com.client
# instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
#
# instStockChart.SetInputValue(0, "A003540")
# instStockChart.SetInputValue(1, ord('2'))
# instStockChart.SetInputValue(4, 10)
# instStockChart.SetInputValue(5, 5)
# instStockChart.SetInputValue(6, ord('D'))
# instStockChart.SetInputValue(9, ord('1'))
#
# instStockChart.BlockRequest()
#
# numData = instStockChart.GetHeaderValue(3)
# for i in range(numData):
#     print(instStockChart.GetDataValue(0, i))
#
# instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
# print("종목코드 A003540 의 인덱스: ", instCpStockCode.CodeToIndex('A003540'))
# print("종목코드 A003540 의 종목명: ", instCpStockCode.GetData(1,instCpStockCode.CodeToIndex('A003540')))
#


# import win32com.client
#
# # Create object
# instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
#
# # SetInputValue
# instStockChart.SetInputValue(0, "A003540")
# instStockChart.SetInputValue(1, ord('2'))
# instStockChart.SetInputValue(4, 10)
# instStockChart.SetInputValue(5, (0, 2, 3, 4, 5, 8))
# instStockChart.SetInputValue(6, ord('D'))
# instStockChart.SetInputValue(9, ord('1'))
#
# # BlockRequest
# instStockChart.BlockRequest()
#
# # GetHeaderValue
# numData = instStockChart.GetHeaderValue(3)
# numField = instStockChart.GetHeaderValue(1)
#
# # GetDataValue
# for i in range(numData):
#     for j in range(numField):
#         print(instStockChart.GetDataValue(j, i), end=" ")
#     print("")
#
# # 결과 출력 : 2018.09.05.20:49
# # 20180905 12500 12500 12150 12200 133821
# # 20180904 12300 12500 12200 12450 134727
# # 20180903 12200 12350 12150 12250 116751
# # 20180831 12100 12300 12050 12200 129673
# # 20180830 12250 12300 12150 12150 88441
# # 20180829 12300 12300 12150 12250 156129
# # 20180828 12400 12500 12150 12250 255561
# # 20180827 12250 12400 12100 12300 283725
# # 20180824 12150 12300 12100 12250 75991
# # 20180823 12250 12350 12050 12100 135018


# # PER, EPS 구하기 https://wikidocs.net/3686 :: 10-3-3
# import win32com.client
#
# # Create Object
# instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
#
# # SetInputValue
# instMarketEye.SetInputValue(0, (4, 67, 70, 111))
# instMarketEye.SetInputValue(1, 'A003540')
#
# # BlockRequest
# instMarketEye.BlockRequest()
#
# # GetData
# print("현재가: ", instMarketEye.GetDataValue(0, 0))
# print("PER: ", instMarketEye.GetDataValue(1, 0))
# print("EPS: ", instMarketEye.GetDataValue(2, 0))
# print("최근분기년월: ", instMarketEye.GetDataValue(3, 0))


# # 거래량분석을통한대박주포착 https://wikidocs.net/3686 :: 10-4-1
# # 대신증권 종목 60일치 거래량을 리스트에 저장
# import win32com.client
#
# # Create object
# instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
#
# # SetInputValue
# instStockChart.SetInputValue(0, "A003540")
# instStockChart.SetInputValue(1, ord('2'))
# instStockChart.SetInputValue(4, 60)
# instStockChart.SetInputValue(5, 8)
# instStockChart.SetInputValue(6, ord('D'))
# instStockChart.SetInputValue(9, ord('1'))
#
# # BlockRequest
# instStockChart.BlockRequest()
#
# # GetData
# volumes = []
# numData = instStockChart.GetHeaderValue(3)
# for i in range(numData):
#     volume = instStockChart.GetDataValue(0, i)
#     volumes.append(volume)
# print(volumes)


# # 한종목에 대한 대박주 찾기
# import win32com.client
#
# # Create object
# instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
#
# # SetInputValue
# instStockChart.SetInputValue(0, "A003540")
# instStockChart.SetInputValue(1, ord('2'))
# instStockChart.SetInputValue(4, 60)
# instStockChart.SetInputValue(5, 8)
# instStockChart.SetInputValue(6, ord('D'))
# instStockChart.SetInputValue(9, ord('1'))
#
# # BlockRequest
# instStockChart.BlockRequest()
#
# # GetData
# volumes = []
# numData = instStockChart.GetHeaderValue(3)
# for i in range(numData):
#     volume = instStockChart.GetDataValue(0, i)
#     volumes.append(volume)
#
# # Calculate average volume
# averageVolume = (sum(volumes) - volumes[0]) / (len(volumes) -1)
#
# if(volumes[0] > averageVolume * 10):
#     print("대박주")
# else:
#     print("일반주", volumes[0] / averageVolume)


# # 유가증권 전종목 거래량 급증 여부 확인 알고리즘
# import win32com.client
#
# def CheckVolumn(instStockChart, code):
#     # SetInputValue
#     instStockChart.SetInputValue(0, code)
#     instStockChart.SetInputValue(1, ord('2'))
#     instStockChart.SetInputValue(4, 60)
#     instStockChart.SetInputValue(5, 8)
#     instStockChart.SetInputValue(6, ord('D'))
#     instStockChart.SetInputValue(9, ord('1'))
#
#     # BlockRequest
#     instStockChart.BlockRequest()
#
#     # GetData
#     volumes = []
#     numData = instStockChart.GetHeaderValue(3)
#     for i in range(numData):
#         volume = instStockChart.GetDataValue(0, i)
#         volumes.append(volume)
#
#     # Calculate average volume
#     averageVolume = (sum(volumes) - volumes[0]) / (len(volumes) -1)
#
#     if(volumes[0] > averageVolume * 10):
#         return 1
#     else:
#         return 0
#
# if __name__ == "__main__":
#     instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
#     instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
#     codeList = instCpCodeMgr.GetStockListByMarket(1)
#     buyList = []
#     for code in codeList:
#         if CheckVolumn(instStockChart, code) == 1:
#             buyList.append(code)
#             print(code)


# # PER분석과 유망종목 https://wikidocs.net/3686 :: 10-4-2
# # 업종별 종목과 업종명 확인
# import win32com.client
#
# instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
# industryCodeList = instCpCodeMgr.GetIndustryList()
#
# for industryCode in industryCodeList:
#     print(industryCode, instCpCodeMgr.GetIndustryName(industryCode))


# # 음식료품(5번) 업종 종목 코드와 종목명
# import win32com.client
#
# instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
# tarketCodeList = instCpCodeMgr.GetGroupCodeList(5)
#
# for code in tarketCodeList:
#     print(code, instCpCodeMgr.CodeToName(code))


# 음식료퓸 업종에 대한 평균 PER 계산
import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

tarketCodeList = instCpCodeMgr.GetGroupCodeList(5)

# Get PER
instMarketEye.SetInputValue(0, 67)
instMarketEye.SetInputValue(1, tarketCodeList)

# BlockRequest
instMarketEye.BlockRequest()

# GetHeaderValue
numStock = instMarketEye.GetHeaderValue(2)

# GetData
sumPer = 0
for i in range(numStock):
    sumPer += instMarketEye.GetDataValue(0, i)

print("Average PER: ", sumPer / numStock)
