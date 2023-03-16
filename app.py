import dash
from dash import Dash, html, dcc

# dg = (
#   pd.read_csv("final csv files/word_frequency_by_year_girl")
# )
# db = (
#   pd.read_csv("final csv files/word_frequency_by_year_boy")
# )

# fig_g = px.line(dg, x=dg['year'], y=[dg['love'], dg['baby'], dg['male-related'], dg['female-related'], dg["like"], dg["want"]])
# fig_b = px.line(db, x=db['year'], y=[db['love'], db['baby'], db['female-related'], db['male-related'], db["like"], db["want"]])

# fig_g.update_layout(
#   {
#     'plot_bgcolor': 'rgba(0,0,0,0)',
#     'paper_bgcolor': 'rgba(0,0,0,0)',
#   },
#   font=dict(
#     family="Raleway, sans-serif",
#     size=14
#   )
# )
# fig_g.update_xaxes(showline=True, linewidth=1, linecolor='black', showgrid=True, gridwidth=1, gridcolor='rgb(240, 240, 240)')
# fig_g.update_yaxes(showline=True, linewidth=1, linecolor='black', showgrid=True, gridwidth=1, gridcolor='rgb(240, 240, 240)')

# fig_b.update_layout(
#   {
#     'plot_bgcolor': 'rgba(0,0,0,0)',
#     'paper_bgcolor': 'rgba(0,0,0,0)',
#   },
#   font=dict(
#     family="Raleway, sans-serif",
#     size=14
#   )
# )
# fig_b.update_xaxes(showline=True, linewidth=1, linecolor='black', showgrid=True, gridwidth=1, gridcolor='rgb(240, 240, 240)')
# fig_b.update_yaxes(showline=True, linewidth=1, linecolor='black', showgrid=True, gridwidth=1, gridcolor='rgb(240, 240, 240)')

app = Dash(__name__, use_pages=True)

# html - Multi Pages

app.layout = html.Div([
	html.H1('Multi-page app with Dash Pages'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container
])



# html - Single Page

# app.layout = html.Div(
#   children=[
#     html.H1(
#       children="Kpop Analysis",
#       className="flex"
#       ),
#     html.Div(
#       children=[
#         html.Div(
#           children=html.P(
#             children="word_frequency_by_year_girl",
#             className="wrapper chart_title"
#             )
#         ),
#         dcc.Graph(figure=fig_g),
#       ]
#     ),
#     html.Div(
#       children=[
#         html.Div(
#           children=html.P(
#             children="word_frequency_by_year_boy",
#             className="wrapper chart_title"
#             )
#         ),
#         dcc.Graph(figure=fig_b)
#       ]
#     )
#   ]
# )

if __name__ == "__main__":
    app.run_server(debug=True)
