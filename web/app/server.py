from datetime import datetime, timedelta

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.graph_objs as go
import plotly.express as px

from db import crud, models

load_figure_template('cyborg')
instruments_count = 100
hour_lookup = 1  # range for datetime filter


app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.CYBORG], update_title="Ticker")


instrument_names = [f"ticker_0{i}" if i <
                    10 else f"ticker_{i}" for i in range(instruments_count)]

# Container for web app
app.layout = html.Div(
    [dcc.Dropdown(instrument_names, instrument_names[0], id='dropdown', clearable=False),
     dcc.Graph(id='graph', animate=True),
     dcc.Interval(id="interval", interval=1*1000, n_intervals=0)])  # update every 1 second


@app.callback(Output('graph', 'figure'), [Input('dropdown', 'value'), Input('interval', 'n_intervals')])
def update_data(value, n_intervals):
    """update selected chart from dropdown every second"""

    # get ticks in datetime range
    start_date = datetime.now() - timedelta(hours=hour_lookup)
    end_date = datetime.now()
    ticks = crud.get_ticks(value, start_date, end_date)

    # graph settings
    x_seconds = [tick.updated_at for tick in ticks]
    y_prices = [tick.price for tick in ticks]
    range_x = [x_seconds[0], x_seconds[-1] + timedelta(seconds=5)]
    range_y = [min(y_prices)-1, max(y_prices)+1]
    graph = px.line(x=x_seconds, y=y_prices, template='cyborg',
                    markers=True, range_x=range_x, range_y=range_y, labels=['Time', 'Price'])
    graph.update_xaxes(title_text='Time')
    graph.update_yaxes(title_text='Price')
    return graph


server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
