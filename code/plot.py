import plotly.io as pio
import load_data


def DrawConfirmed(regionList):
    layout = {"title": {"text": "Confirmed Cases"}}

    traces = []
    for region in regionList:
        name = region['country']
        if region['province'] != '*':
            name = region['province']
        
        traces.append({"type": "scatter", "y": region['confirmed'], "name":name})
    
    fig = {}
    fig['data'] = traces
    fig['layout'] = layout

    pio.show(fig)
    return
        

regionList = load_data.LoadRegionList()
DrawConfirmed(regionList)