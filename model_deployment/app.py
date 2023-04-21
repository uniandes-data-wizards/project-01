import dash
from dash.dependencies import Input, Output, State
from dash import html, dcc
import requests

app = dash.Dash(__name__,
                external_stylesheets=[
                    'https://codepen.io/chriddyp/pen/bWLwgP.css',
                    'https://fonts.googleapis.com/css?family=Roboto:400,500,700&display=swap'
                ])

app.layout = html.Div([
    html.H1('Clasificador de Sentimientos de Películas',
            style={
                'textAlign': 'center',
                'color': '#0074D9',
                'font-size': '36px',
                'font-weight': 'bold',
                'margin-top': '30px',
                'font-family': 'Roboto'
            }),
    dcc.Textarea(
        id='textarea_review',
        placeholder='Ingrese aquí su reseña de la película...',
        value='',
        style={
            'width': '100%',
            'height': '200px',
            'font-size': '20px',
            'padding': '10px',
            'margin-top': '30px',
            'border-radius': '5px',
            'border': '1px solid #ddd',
            'font-family': 'Roboto'
        }),
    html.Button('Enviar', id='submit_button', style={
        'margin-top': '20px',
        'background-color': '#0074D9',
        'color': 'white',
        'font-size': '15px',
        'padding': '10px',
        'border-radius': '5px',
        'border': 'none',
        'font-family': 'Roboto',
        'height': '50px',
        'width': '100px'
    }),
    html.Div(id='output_div', style={
        'margin-top': '30px',
        'font-size': '24px',
        'font-weight': 'bold',
        'font-family': 'Roboto'
    })
], style={'width': '80%', 'margin': 'auto'})


@app.callback(
    Output('output_div', 'children'),
    Input('submit_button', 'n_clicks'),
    State('textarea_review', 'value')
)
def update_output_div(n_clicks, textarea_value):
    if n_clicks is None:
        return ''
    if textarea_value == '':
        return 'Por favor ingrese una reseña.'
    else:
        data = {'review_es': textarea_value}
        response = requests.post('http://127.0.0.1:8000/predict', json=data)
        if response.status_code == 200:
            result = response.json()
            return f'El sentimiento de la película es {result}.'
        else:
            return 'Error al procesar la solicitud.'


if __name__ == '__main__':
    app.run_server(debug=True)
