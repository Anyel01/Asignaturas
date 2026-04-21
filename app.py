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
    # Forzar la institución a "Colegio Gonzalo Rivera Laguado"
    data['institucion'] = 'Colegio Gonzalo Rivera Laguado'

    asignaturas = data.get('asignaturas', [])
    periodos = data.get('periodos', [])
    num_periodos = len(periodos)

    for asig in asignaturas:
        horas_vals = []
        for h in asig.get('horas', []):
            try:
                if h != '' and h is not None:
                    horas_vals.append(float(h))
            except (ValueError, TypeError):
                pass
        if horas_vals:
            asig['promedio'] = round(sum(horas_vals) / len(horas_vals), 1)
            asig['total'] = round(sum(horas_vals), 1)
        else:
            asig['promedio'] = 0
            asig['total'] = 0

    todos_promedios = [a['promedio'] for a in asignaturas if a['promedio'] > 0]
    promedio_general = round(sum(todos_promedios) / len(todos_promedios), 1) if todos_promedios else 0
    total_horas_global = sum(a['total'] for a in asignaturas)

    html = render_template('boletin_impresion.html',
        institucion=data.get('institucion', ''),
        programa=data.get('programa', ''),
        anio=data.get('anio', datetime.now().year),
        responsable=data.get('responsable', ''),
        observaciones=data.get('observaciones', ''),
        asignaturas=asignaturas,
        periodos=periodos,
        num_periodos=num_periodos,
        promedio_general=promedio_general,
        total_horas_global=total_horas_global,
        fecha=datetime.now().strftime('%d/%m/%Y')
    )
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
