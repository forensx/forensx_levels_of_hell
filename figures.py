import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


def get_figures():
    fig = go.Figure()

    fig.add_trace(
        go.Bar(x=[10, 20, 30, 40, 50, 60, 70],
               y=['Level 1', 'Level 2', 'Level 3',
                  "Level 4", "Level 5", "Level 6", "Level 7"],
               text=["Never speaking again after high school", "30 minutes till Code Freeze",
                     "Colorblindness", "UPenn and MIT ED/EA", "Dash Tabs and Folium", "Lonnie not equal vro to rest of us", "TeenTech and GSU"],
               textposition='auto',
               hoverinfo="skip",
               orientation='h')
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=go.layout.Margin(
            l=200,
            r=200,
            b=100,
            t=100,
            pad=4
        ),
        font=dict(
        ),
        xaxis=dict(
            title="",
            showline=False,
            showgrid=False,
            showticklabels=False,
            zeroline=False,
            linecolor='rgb(204, 204, 204)',
            linewidth=0,
            tickangle=-45,
            ticks='outside',
            tickfont=dict(
                family='Arial',
            ),

        ),
        yaxis=dict(
            title="Level of Hell",
            showgrid=False,
            zeroline=False,
            tickfont=dict(
                family='Arial',
            )
        ),
        title=dict(
            text="",
            x=0.5
        )
    )

    return fig
