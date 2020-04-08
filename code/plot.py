import plotly.io as pio
import load_data
import analyze

def PlotAttrib(regionList, attrib):
    xAxisTitle = 'days since outbreak began'
    #yAxisScale = 'log'
    yAxisScale = 'linear'
    
    layout = {}
    layout['title'] = {"text": attrib}
    layout['xaxis'] = {'title_text': xAxisTitle}
    layout['yaxis'] = {'type': yAxisScale}

    traces = []
    for region in regionList:
        name = region['country']
        if region['province'] != '*':
            name = region['province']
        
        traces.append({"type": "scatter", "y": region[attrib], "name":name})
    
    fig = {}
    fig['data'] = traces
    fig['layout'] = layout
    
    pio.show(fig)
    return
        

#pio.renderers.default = "firefox"

regionList = load_data.LoadRegionList()
analyze.AnalyzeRegions(regionList)

PlotAttrib(regionList, 'confirmed')
PlotAttrib(regionList, 'confirmed_pm')
PlotAttrib(regionList, 'deaths')
PlotAttrib(regionList, 'deaths_pm')
PlotAttrib(regionList, 'deaths_daily')
PlotAttrib(regionList, 'deaths_daily_pm')