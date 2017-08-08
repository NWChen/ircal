import sys
import pandas as pd

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

def read_data(filename):
    df = pd.read_csv(filename, sep='\t', lineterminator='\n')
    df['TIME'] = pd.to_datetime(df['TIME'], format='%m/%d/%Y %H:%M:%S.%f')
    df.columns = df.columns.str.replace('\r', '')
    return df

def generate_graph(df):
    pass 

def main():
    """Application entry point."""
    pass

if __name__ == '__main__':
    sys.exit(main())
