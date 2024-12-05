from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    html.H4("Camera Calibration Analysis"),
    html.P("x-axis:"),
    dcc.Checklist(
        id='x-axis', 
        options=['phone_model', 'camera_model', 'calib_grid', 'calib_size'],
        value=['camera_model'], 
        inline=True
    ),
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis', 
        options=['fx', 'fy', 'cx', 'cy', 'k1', 'k2'],
        value='fx', 
        inline=True
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("x-axis", "value"), 
    Input("y-axis", "value"))
def generate_chart(x, y):
    df = pd.read_csv("data/cam_calib.csv") # replace with your own data source
    fig = px.box(df, x=x, y=y)
    return fig


app.run_server(debug=True)