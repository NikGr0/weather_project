import datetime

dt2 = datetime.date.today()

dt1 = datetime.datetime.now()

dt_n = datetime.datetime.strptime(str(dt1)[:19], '%Y-%m-%d %H:%M:%S')
dt_n1 = 'history/' + str(dt1)[:10] + '_' + str(dt1)[11:13] + '_' + str(dt1)[14:16] + '_' + str(dt1)[17:19] + '.csv'
print(dt2)
print(type(dt2))
print(dt1)
print(dt_n1)