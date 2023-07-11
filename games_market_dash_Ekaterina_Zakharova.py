
import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px

app = Dash(__name__)

#Data inmport and cleaning
df = pd.read_csv('games.csv')
df = df.dropna(axis='index',how='any')
df = df[(df['Year_of_Release'] > 2000)]
df.to_csv('games.csv')

dff=df.copy()
#Scatter plot
fig = px.scatter(dff, x='User_Score', y='Critic_Score', color='Genre')

#Filter by game genres - button
app.layout = html.Div([
    html.H1('Games', style={'text-align':'center'}),
    dcc.Checklist(id = 'select_genre',
                  options=[{'label':'Sports', 'value': 'Sports'},
                           {'label':'Racing', 'value': 'Racing'},
                           {'label':'Platform', 'value':'Platform'},
                           {'label':'Misc', 'value': 'Misc'},
                           {'label':'Action', 'value': 'Action'},
                           {'label':'Puzzle', 'value': 'Puzzle'},
                           {'label':'Shooter', 'value':'Shooter'},
                           {'label':'Fighting', 'value': 'Fighting'},
                           {'label':'Simulation', 'value': 'Simulation'},
                           {'label':'Role-Playing', 'value': 'Role-Playing'},
                           {'label': 'Adventure', 'value':'Adventure'},
                           {'label':'Strategy','value':'Strategy'}],
                  labelStyle={"display": "block"},
                  value=[]),
    html.Button('Check',id='button',n_clicks=0),
    html.Br(),
    dcc.Graph(id='basic-interactions',figure=fig)
])

@callback(
    Output(component_id='button', component_property='n_clicks'),
    Output(component_id='basic-interactions', component_property='figure'),
    Input(component_id='select_genre', component_property='value'))
def change_values(n_clicks):
    container = 'The amount of games chosen:{}'.format(n_clicks)
    return ["Sports"] if n_clicks > 0 else [], container, fig

if __name__ == '__main__':
    app.run(debug=True)

