from flask import Flask, render_template, request, jsonify, make_response
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boletin')
def boletin():
    return render_template('boletin.html')

@app.route('/generar', methods=['POST'])
def generar():
    data = request.get_json()
    return jsonify({'status': 'ok', 'data': data})

@app.route('/imprimir', methods=['POST'])
def imprimir():
    data = request.get_json()

    asignaturas = data.get('asignaturas', [])
    
    # Calcular total_horas como suma de intensidades
    total_horas = sum(asig.get('intensidad', 0) for asig in asignaturas)

    html = render_template('boletin_impresion.html',
        docente=data.get('docente', ''),
        titular=data.get('titular', ''),
        tipo_docente=data.get('tipo_docente', ''),
        asignaturas=asignaturas,
        total_horas=total_horas,
        mes_anio=datetime.now().strftime('%B de %Y')
    )
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=False)
