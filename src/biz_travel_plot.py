import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import numpy as np
import pandas as pd


# Read in global data
#testtest
df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Setup app and layout/frontend
app = dash.Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.layout = html.Div([
    html.Iframe(
        id='bar_biz_travel',
        #srcDoc=plot_altair(),
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='gender-widget',
        value='',  # REQUIRED to show the plot on the first page load
        options=[
            {'label': "Female", 'value': "Female"},
            {'label': "Male", 'value': "Male"}
            ]
        )])

# Set up callbacks/backend
@app.callback(
    Output('bar_biz_travel', 'srcDoc'),
    Input('gender-widget', 'value'))
def plot_altair(gen_value):
    if gen_value == '':
        data = df
    else:
        data = df[df["Gender"]== gen_value]
    #data = df[df["Gender"]== gen_value]
    chart = alt.Chart(data).mark_bar().encode(
        y=alt.Y("BusinessTravel", title="Frequency of Business Travel"),
        x=alt.X('count()', stack="normalize"),  # rwidth = xx or something to change the bar width
        color = "Attrition")
    return chart.to_html()
    #return chart

if __name__ == '__main__':
    app.run_server(debug=True) # debug=True