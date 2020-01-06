import datetime

start_saterday = "27-12-2019"
start_thursday = None
mutation_saterday_days = 6*7
mutation_thursday_days = 6*7
offset_thursday_days = 3*7


saterday = datetime.datetime.strptime(start_saterday, "%d-%m-%Y")
with open('./README.md','w') as f:
    f.write('# CHIPdays\n\nThis is an indication as certain holidays are not considered\n')
    f.write('Saterday | Thursday\n')
    f.write('--- | --- | ---\n')
    for i in range(12):
        f.write(datetime.datetime.strftime(saterday + datetime.timedelta(days=mutation_saterday_days*i), "%d/%m/%Y"))
        f.write('|')
        f.write(datetime.datetime.strftime(saterday + datetime.timedelta(days=5+offset_thursday_days+mutation_saterday_days*i), "%d/%m/%Y"))
        f.write('\n')
