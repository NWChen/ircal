import sys
import pandas as pd

from bokeh.layouts import gridplot
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
    fig = figure(x_axis_type='datetime')
    fig.line(df['TIME'], df['KT SEA REF'])
    return fig

def main():
    """Application entry point."""
    filename = sys.argv[1]
    show(generate_graph(read_data(filename)))

if __name__ == '__main__':
    sys.exit(main())
