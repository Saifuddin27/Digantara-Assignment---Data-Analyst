#!/usr/bin/env python
# coding: utf-8

# In[3]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load your data
data = pd.read_csv('sort-minRange.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Conjunction Analysis Dashboard"),
    
    html.Div([
        html.Label("Select a Satellite:"),
        dcc.Dropdown(
            id='satellite-dropdown',
            options=[{'label': sat, 'value': sat} for sat in data['OBJECT_NAME_1'].unique()],
            value=data['OBJECT_NAME_1'].unique()[0]
        ),
    ], style={'width': '30%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='risk-pie-chart')
    ], style={'width': '50%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='conjunction-scatter-plot')
    ], style={'width': '50%', 'display': 'inline-block'}),
])

# Define callback to update graphs based on user selection
@app.callback(
    [Output('risk-pie-chart', 'figure'),
     Output('conjunction-scatter-plot', 'figure')],
    [Input('satellite-dropdown', 'value')]
)
def update_graphs(selected_satellite):
    # Filter data based on selected satellite
    selected_data = data[data['OBJECT_NAME_1'] == selected_satellite]
    
    # Risk Assessment Pie Chart
    risk_counts = [len(selected_data[selected_data['MAX_PROB'] < 0.2]),  # Define risk level thresholds as needed
                   len(selected_data[(selected_data['MAX_PROB'] >= 0.2) & (selected_data['MAX_PROB'] < 0.5)]),
                   len(selected_data[selected_data['MAX_PROB'] >= 0.5])]
    pie_chart_fig = px.pie(values=risk_counts, names=['Low Risk', 'Moderate Risk', 'High Risk'], title='Risk Assessment')
    
    # Conjunction Scatter Plot
    scatter_plot_fig = px.scatter(selected_data, x='TCA', y='MAX_PROB', color='MAX_PROB',
                                  labels={'TCA': 'Time of Closest Approach', 'MAX_PROB': 'Max Probability'},
                                  title='Conjunction Details')
    
    return pie_chart_fig, scatter_plot_fig

if __name__ == '__main__':
    app.run_server(debug=True)


# # 

# # 

# In[2]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import random

# Generate random data for demonstration purposes
random.seed(42)
satellites = ['Satellite A', 'Satellite B', 'Satellite C']
risk_levels = ['Low Risk', 'Moderate Risk', 'High Risk']
data = []

for satellite in satellites:
    for _ in range(30):
        data.append({
            'Satellite': satellite,
            'TCA': random.randint(1, 30),
            'Max Probability': random.uniform(0.1, 0.9),
            'Risk Level': random.choice(risk_levels)
        })

data = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Conjunction Analysis Dashboard"),
    
    html.Div([
        html.Label("Select a Satellite:"),
        dcc.Dropdown(
            id='satellite-dropdown',
            options=[{'label': sat, 'value': sat} for sat in satellites],
            value=satellites[0]
        ),
    ], style={'width': '30%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='risk-pie-chart')
    ], style={'width': '50%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='conjunction-scatter-plot')
    ], style={'width': '50%', 'display': 'inline-block'}),
])

# Define callback to update graphs based on user selection
@app.callback(
    [Output('risk-pie-chart', 'figure'),
     Output('conjunction-scatter-plot', 'figure')],
    [Input('satellite-dropdown', 'value')]
)
def update_graphs(selected_satellite):
    # Filter data based on selected satellite
    selected_data = data[data['Satellite'] == selected_satellite]
    
    # Risk Assessment Pie Chart
    risk_counts = [len(selected_data[selected_data['Risk Level'] == level]) for level in risk_levels]
    pie_chart_fig = px.pie(values=risk_counts, names=risk_levels, title='Risk Assessment')
    
    # Conjunction Scatter Plot
    scatter_plot_fig = px.scatter(selected_data, x='TCA', y='Max Probability', color='Risk Level', 
                                  labels={'TCA': 'Time of Closest Approach', 'Max Probability': 'Max Probability'},
                                  title='Conjunction Details')
    
    return pie_chart_fig, scatter_plot_fig

if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




