import datetime

start_saturday = "28-12-2019"
start_thursday = None
mutation_saturday_days = 6*7
mutation_thursday_days = 6*7
offset_thursday_days = 3*7


saturday = datetime.datetime.strptime(start_saturday, "%d-%m-%Y")
with open('./README.md','w') as f:
    f.write('# CHIPdays\n\nThis is an indication as certain holidays are not considered\n\n')
    f.write('Saturday | Thursday\n')
    f.write('--- | ---\n')
    for i in range(12):
        f.write(datetime.datetime.strftime(saturday + datetime.timedelta(days=mutation_saturday_days*i), "%A, %d %B - %d/%m/%Y"))
        f.write(' | ')
        f.write(datetime.datetime.strftime(saturday + datetime.timedelta(days=-2+offset_thursday_days+mutation_saturday_days*i), "%A, %d %B - %d/%m/%Y"))
        f.write('\n')
