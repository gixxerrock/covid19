def AnalyzeRegion(region):
    region['confirmed_pm'] = []
    region['deaths_pm'] = []
    
    for cnt in region['confirmed']:
        region['confirmed_pm'].append(cnt*1000000/region['population'])
        
    for cnt in region['deaths']:
        region['deaths_pm'].append(cnt*1000000/region['population'])

def AnalyzeRegions(regionList):
    for region in regionList:
        AnalyzeRegion(region)
        
