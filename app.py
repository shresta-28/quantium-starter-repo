from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

BG_COLOR = "#F7D8FF"
TEXT_COLOR = "#2B0D33"
ACCENT_COLOR = "#FFAFDF"

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

app.layout = html.Div(
    style={
        'backgroundColor' : BG_COLOR,
        'color': TEXT_COLOR,
        'fontFamily': 'Segoe UI, sans-serif',
    },
    children=[
    html.H1(id="header", children='Pink Morsel Visualizer', style={'textAlign': 'center'}),
    html.H2(children='Visualizing daily sales data across regions.', style={'textAlign': 'center'}),
    html.Div([
        html.Label('Select Region:', style={'fontWeight': 'bold'}),
        dcc.RadioItems(
            id='region-radio',
            options=[
                     {'label':'All', 'value':'all'},
                     {'label':'North', 'value':'north'},
                     {'label':'South', 'value':'south'},
                     {'label':'East', 'value':'east'},
                     {'label':'West', 'value':'west'}],
            value='all',  # Default selected value
            inline=True,   # Displays options horizontally
            style={'padding': '10px'}
        )
    ], style={'textAlign': 'center', 'marginBottom': '20px'}),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(selected_region):
    # Filter dataset based on selection
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    # Re-render the line chart with filtered data
    fig = px.line(
        filtered_df,
        x='Date',
        y='Sales',
        color='Region' if selected_region == 'all' else None,
        title=f'Sales Over Time ({selected_region.title() if selected_region != "all" else "All Regions"})',
        labels={'Sales': 'Sales ($)', 'Date': 'Date'}
    )

    if selected_region != 'all':
        fig.update_traces(line_color=TEXT_COLOR)

    fig.update_layout(
        paper_bgcolor=BG_COLOR,
        plot_bgcolor=ACCENT_COLOR,
        font_color=TEXT_COLOR,
        title_font_color=TEXT_COLOR
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
    