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
        

def AnalyzeRegions(regionList):
    for region in regionList:
        AnalyzeRegion(region)
        
