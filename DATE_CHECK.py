import datetime
def date_input():
    while True:
        try:
            input_date = input('日期：')
            year_location = input_date.find('-')
            input_year = input_date[:year_location]
            month_location = input_date.find('-', year_location+1)
            input_month = input_date[year_location+1 : month_location]
            input_day = input_date[month_location+1 : ]
            rs_input_date = datetime.datetime.strptime(input_year+input_month+input_day, '%Y%m%d')
            return rs_input_date
            break
        except Exception as err:
            print (err)
            print("日期格式为：年年年年-月月-年年")
