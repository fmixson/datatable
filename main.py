import dash
import pandas
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash import Dash, dash_table

import pandas as pd

df = pd.read_csv('C:/Users/flmix/OneDrive/Desktop/Division_Enrollment.csv', encoding='Latin')


app = Dash()

dept_options = []

for dept in df['Dept'].unique():
    dept_options.append({'label': dept, 'value': dept})

app.layout = html.Div(children=[
    dcc.Dropdown(
        id='dept-picker',
        options=dept_options,
        value='ASL'
    ),
    dcc.Dropdown(
        id='size-picker',
        options=[5, 10, 15],
        value=35
    ),
    dash_table.DataTable(id='table-container', columns=[{'id': c, 'name': c} for c in df.columns.values])]
)


@app.callback(Output(component_id='table-container', component_property='data'),
              [Input(component_id='dept-picker', component_property='value')],
              [Input(component_id='size-picker', component_property='value')])
def update_table(selected_dept, selected_size):
    filtered_df = df[df['Dept']==selected_dept]
    size_df = filtered_df[filtered_df['Size']<=selected_size]
    print(size_df)
    return size_df.to_dict('records')

if __name__ == '__main__':
     app.run_server(debug=True)










# df = pd.read_csv('gapminder.csv')
# print(df)
#
# app = dash.Dash()
#
# year_options = []
# for year in df['year'].unique():
#     year_options.append({'label': str(year), 'value': year})
#
# app.layout = html.Div([
#     dcc.Graph(id='graph'),
#     dcc.Dropdown(
#         id='year-picker', options=year_options,
#         value=df['year'].min())
# ])
#
# @app.callback(Output(component_id='graph', component_property='figure'),
#               [Input(component_id='year-picker', component_property='value')])
# def update_figure(selected_year):
#     filtered_df = df[df['year']==selected_year]
#     traces = []
#
#     for continent_name in filtered_df['continent'].unique():
#         df_by_continent = filtered_df[filtered_df['continent']==continent_name]
#         print(traces)
#         traces.append(go.Scatter(
#             x = df_by_continent['gdpPercap'],
#             y= df_by_continent['lifeExp'],
#             mode='markers',
#             opacity=0.7,
#             marker={'size': 15},
#             name=continent_name) )
#
#     return {'data': traces,
#             'layout': go.Layout(title='My Plot',
#                                xaxis={'title': 'GDP Per Cap', 'type': 'log'})}
#
# # def update_output_div(input_value):
# #     return 'You entered: {}'.format(input_value)
#
#
# if __name__ == '__main__':
#     app.run_server()
#
#
# # app.layout = html.Div([
# #
# #     html.Label('Dropdown'),
# #     dcc.Dropdown(options=[{'label': 'New York City', 'value': 'NYC'},
# #                           {'label': 'San Francisco', 'value': 'SF'}],
# #                  value='Select a City'),
# #     html.Label('Slider'),
# #     dcc.Slider(min=-10, max=10, step=0.5, value=0),
# #
# #     html.Label('Some Radio Items'),
# #     dcc.RadioItems(options=[{'label': 'New York City', 'value': 'NYC'},
# #                           {'label': 'San Francisco', 'value': 'SF'}],
# #                    value='SF'),
# # ])
#
#
#
#
# # app = dash.Dash()
# #
# #
# # app.layout = html.Div(['This is outmost div!',
# #                         html.Div(['This is an inner div!'],
# #                         style={'color': 'red', 'border': '2px red solid'}),
# #                         html.Div(['Another inner div!'],
# #                         style={'color': 'blue', 'border': '3px blue solid'})],
# #                     style={'color': 'green', 'border': '2px green solid'})
#
#
#
# if __name__ == '__main__':
#     app.run_server()
