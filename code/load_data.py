#reading raw data
rawDataPath = "../raw_data/COVID-19/csse_covid_19_data/csse_covid_19_time_series/"

fn_confirmed = rawDataPath + "time_series_covid19_confirmed_global.csv"
fn_deaths = rawDataPath + "time_series_covid19_deaths_global.csv"
fn_recovered = rawDataPath + "time_series_covid19_recovered_global.csv"
fn_regions = '../config_data/regions.csv'

FirstDateIdx = 4

def UpdateSeries(line, attrib, regionList):
    elems = line.split(',')
    
    for region in regionList:
        if (region['province'] == '*' and elems[1] == region['country'] ) or (elems[0] == region['province']) and (elems[1] == region['country']):
            if attrib not in region:
                region[attrib] = []
            
            # this line matches search criteria
            if len(region[attrib]) == 0:
                for i in range (4, len(elems)):
                    region[attrib].append(int(elems[i]))
            else:
                for i in range (4, len(elems)):
                    region[attrib][i - 4] = int(elems[i]) + region[attrib][i - 4]

def Open(filename, attrib, regionList):
    f = open(filename)
    for line in f:
        UpdateSeries(line, attrib, regionList)
    f.close()

def InitRegions():
    f = open(fn_regions)
    regionList = []
    
    for line in f:
        elems = line.split(',')
        region = {}
        region['province'] = elems[0]
        region['country'] = elems[1]
        region['population'] = elems[2]

        regionList.append(region)
        
    return regionList


def LoadRegionList():
    regionList = InitRegions()

    Open(fn_confirmed, "confirmed", regionList)
    Open(fn_deaths, "deaths", regionList)
    Open(fn_recovered, "recovered", regionList)

    return regionList