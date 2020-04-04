from numpy import loadtxt

rawDataPath = "../raw_data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"

def UpdateSeries(line, province, country):
    elems = line.split(',')
    
    if len(elems) < 5:
        return

    if (province == '*' and elems[3] == country ) or (elems[2] == province) and (elems[3] == country):
        confirmed = int(elems[7])
        deaths = int(elems[8])
        print(elems[2] + " c:" + str(confirmed) + "   D:" + str(deaths))


def Open(filename):
    f = open(filename)
    for line in f:
        UpdateSeries(line, "*", "Canada",)

fn = rawDataPath + "04-03-2020.csv"
Open(fn)
