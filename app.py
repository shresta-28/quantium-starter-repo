from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('clean_data.csv')

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

fig = px.line(
    df,
    x='Date',
    y='Sales',
    color='Region',
    title='Pink Morsel Sales Over Time',
    labels={'Sales': 'Sales ($)', 'Date': 'Date', 'Region': 'Region'}
)

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Visualizer', style={'textAlign': 'center'}),
    
    html.Div(children='Visualizing daily sales data across regions.', style={'textAlign': 'center'}),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
    