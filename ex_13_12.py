# from pandas import Series, DataFrame
#
# kakao = Series([92600, 92400, 92100, 94300, 92300])
# print(kakao)
#
# kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
#                                                             '2016-02-18',
#                                                             '2016-02-17',
#                                                             '2016-02-16',
#                                                             '2016-02-15'])
# print(kakao2)
#
# for date in kakao2.index:
#     print(date)
#
# for ending_price in kakao2.values:
#     print(ending_price)


from pandas import Series, DataFrame

raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)


from pandas import Series, DataFrame

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)

daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'])
print(daeshin_day)
