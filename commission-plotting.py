import plotly
import plotly.graph_objs as go


def maths(basicrate, higherrate, cutoff, sales):
    if (sales <= cutoff):
        result = sales * basicrate
    else:
        result = ((cutoff * basicrate) + ((sales - cutoff) * higherrate))
    return result


# plotting
def plot():
    xlist = []
    officeaylist = []
    officeb1ylist = []
    officeb2ylist = []
    officecylist = []
   
    for s in range(0, 15):
        xlist.append(s)
        # Office A
        result = maths(basicrate = 25, higherrate = 60, cutoff = 5, sales = s)
        officeaylist.append(result)
        # Office B, Higher: £50    
        result = maths(basicrate = 25, higherrate = 50, cutoff = 7, sales = s)
        officeb1ylist.append(result)
        # Office B, Higher: £60    
        result = maths(basicrate = 25, higherrate = 60, cutoff = 7, sales = s)
        officeb2ylist.append(result)
        # Office C, Higher: £100    
        result = maths(basicrate = 25, higherrate = 100, cutoff = 9, sales = s)
        officecylist.append(result)

    trace0 = go.Scatter(
        x=xlist,
        y=officeaylist,
        name='Office A - Cutoff: 5, Higher £60',
        line=dict(
            color=('rgb(205, 12, 24)'),
            width=4)
    )
    trace1 = go.Scatter(
        x=xlist,
        y=officeb1ylist,
        name='Office B - Cutoff: 7, Higher: £50',
        line=dict(
            color=('rgb(22, 96, 167)'),
            width=4)
    )
    trace2 = go.Scatter(
        x=xlist,
        y=officeb2ylist,
        name='Office B - Cutoff: 7, Higher: £60',
        line=dict(
            color=('rgb(0, 168, 107)'),
            width=4)
    )
    trace3 = go.Scatter(
        x=xlist,
        y=officecylist,
        name='Office C - Cutoff: 9, Higher: £100',
        line=dict(
            color=('rgb(255, 165, 0)'),
            width=4)
    )

    data = [trace0, trace1, trace2, trace3]

    # Edit the layout
    layout = dict(title='Office A / Office B profitability',
                  xaxis=dict(title='# Sales'),
                  yaxis=dict(title='Commission £'),
                  )

    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='styled-line')


plot()
