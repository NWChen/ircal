import sys
import pandas as pd

from bokeh.layouts import gridplot, layout, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select
from bokeh.plotting import figure, show, output_file

def read_data(filename):
    """Converts a tab-separated data file into a pandas DataFrame. Any timestamps are converted into datetime objects.
        :param filename: Absolute or relative path to data file
        :type filename: String
        :returns: DataFrame containing datetime objects and corresponding rows of ata
        :rtype: pandas.DataFrame
    """
    df = pd.read_csv(filename, sep='\t', lineterminator='\n')
    df['TIME'] = pd.to_datetime(df['TIME'], format='%m/%d/%Y %H:%M:%S.%f')
    df.columns = df.columns.str.replace('\r', '')
    return df

def generate_graph(df):
    """Generate Bokeh graph from Pandas DataFrame."""
    fig = figure(x_axis_type='datetime')
    fig.line(df['TIME'], df['KT SEA REF'])
    return fig

def update(source, df, axis):
    source.data = dict(
        x=df['TIME'],
        y=df[axis]
    ) 
    import pdb; pdb.set_trace()
    return source

def main():
    """Application entry point."""
    SIZING_MODE = 'fixed'
    filename = sys.argv[1]

    # data source displayed by the plot
    source = ColumnDataSource(data=dict(x=[], y=[]))

    # plot/data elements
    df = read_data(filename)
    p = figure(x_axis_type='datetime')
    p.circle(x='x', y='y', source=source)

    # set up dashboard controls
    #fig = generate_graph(df)
    y_axis = Select(title="Y Axis", options=sorted(df.columns), value='KT SEA REF')
    source = update(source, df, y_axis.value)
    y_axis.on_change('value', lambda attr, old, new: update(source, df, y_axis.value))

    # display dashboard controls
    controls = [y_axis]
    inputs = widgetbox(*controls, sizing_mode=SIZING_MODE)
    l = layout([
        [inputs, p]
    ], sizing_mode=SIZING_MODE)

    show(l)

if __name__ == '__main__':
    sys.exit(main())
