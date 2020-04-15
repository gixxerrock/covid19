def AnalyzeRegion(region):
    region['confirmed_pm'] = []
    region['deaths_pm'] = []
    region['deaths_daily'] = []
    region['deaths_daily_pm'] = []
    
    for cnt in region['confirmed']:
        region['confirmed_pm'].append(cnt*1000000/region['population'])
        
    for cnt in region['deaths']:
        region['deaths_pm'].append(cnt*1000000/region['population'])

    # calculate daily death toll, normalize per million
    lastDeath = 0 
    for cnt in region['deaths']:
        deathDaily = cnt - lastDeath
        lastDeath = cnt
        region['deaths_daily'].append(deathDaily)
        region['deaths_daily_pm'].append(deathDaily*1000000/region['population'])
        
    SmoothSeries(region['deaths_daily'])
    SmoothSeries(region['deaths_daily_pm'])


def SmoothSeries(series):
    num = len(series)

    #initialize array
    smooth = []
    for i in range(0, num):
        smooth.append(0)

    for i in range(1, num - 1):
        cur = series[i]
        smooth[i-1] += cur*0.2
        smooth[i]   += cur*0.6
        smooth[i+1] += cur*0.2

    smooth[num-1] = series[num-1]
    smooth[num-2] += series[num-1]*0.2

    for i in range(0, num):
        series[i] = smooth[i]

def AnalyzeRegions(regionList):
    for region in regionList:
        AnalyzeRegion(region)
    
        
