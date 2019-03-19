import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from plotly import graph_objs as go
from plotly import tools
import plotly.figure_factory as ff
import datetime
import json
import os
import pandas as pd
import numpy as np
from util_script import phrase_voter

css_url = 'https://codepen.io/munyont/pen/XoeGae.css'
css_bootstrap_url = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css'
external_stylesheets = [css_url, css_bootstrap_url, 'https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet',
'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css',
'https://codepen.io/munyont/pen/qvoMMj.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions']=True

server = app.server

app.layout = html.Div(className='',  children=[
     html.Div(
        className='section',
        children=[
            html.H1('Key Phrase Similarity', className='landing-text'),
        ]
    ),

    html.Br(),
    html.Br(),

    html.Div(className='container', children=[
        html.Div(className='row phrase-input-field', children=[
                dcc.Input(id='input-1-state', type='text', value='distance learning options'),
                html.Button(id='submit-button', n_clicks=0, children='Submit'),
        ]),

    html.Br(),
        html.Div(className='row', children=[
            html.H2(id='text-similar-phrase'),
        ]),

        html.Div(className='row', children=[
            dcc.Graph(id='histogram-similar-phrase', style={'width': '1000px'}),
        ]),

    ]),

    html.Br(),
    html.Br(),

])

@app.callback(Output('text-similar-phrase', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value')])
def text_run_input(n_clicks, input1):
    res = phrase_voter(input1)
    json_dump = json.dumps(res)
    res_json = json.loads(json_dump)

    #res_df = pd.DataFrame.from_dict(res, orient='index')
    #res_df = res_df.to_json()

    print(type(res_json))
    print(res_json)
    print(type(res_json))
    print(type(res_json))
    print(type(res_json))
    return res_json

@app.callback(Output('histogram-similar-phrase', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value')])
def histgram_run_input(n_clicks, input1):
    res = phrase_voter(input1)
    res_df = pd.DataFrame.from_dict(res, orient='index')
    print(res_df)

    trace = go.Bar(y=res_df.index, x=res_df.iloc[:, 0], orientation='h',
        marker=dict(
            color='rgb(55, 83, 109)'
            )
        )

    layout = go.Layout(title='Key Phrases', yaxis=dict(automargin=True, autorange="reversed"))

    return go.Figure(data=[trace], layout=layout)


if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
