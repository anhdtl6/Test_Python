
import datetime
# 1
def day_diff(release_date, code_complete_day):
    date1 = datetime.datetime.strptime(release_date,"%d/%m/%Y").strftime("%Y-%m-%d")
    date2 = datetime.datetime.strptime(code_complete_day,"%Y-%d-%m").strftime("%Y-%m-%d")
    mdate1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
    rdate1 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()
    delta = (mdate1 - rdate1).days
    print(delta)
    return delta

# 2
def alpha_num(sentence):
    result = []
    values = sentence.split()
    print(values)
    for x in values:
        check = x.isalnum() and not x.isalpha() and not x.isdigit()
        if check:
            result.append(x)
    print(result)
    return result