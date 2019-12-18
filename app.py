import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


from figures import get_figures

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = 'ForensX\'s Divine Comedy'

app.layout = html.Div(children=[
    html.H1(children='ForensX\'s Divine Comedy',
            style={
                'textAlign': 'center',
                "marginTop": "2%"}
            ),

    html.Div(children='''
        ForensX - 7 levels of Hell.
    ''', style={
        'textAlign': 'center'
    }),

    dcc.Graph(
        id='forensx-levels-of-hell',
        figure=get_figures(),
        style={
            "height": "80vh"
        }
    )
])

if __name__ == '__main__':
    app.run_server(port=8080)
