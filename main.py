# Importar
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La primera página
@app.route('/')
def index():
    return render_template('index.html')
# Segunda página
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# La tercera página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# El formulario
@app.route('/submit', methods=['POST'])
def submit_form():
    # SOLUCIÓN AL 'NONE': Asegúrate de capturar los nombres correctos del formulario
    # Si sigue saliendo None, revisa que en tu formulario HTML diga name="nombre"
    nombre = request.form.get('nombre') or request.form.get('name') or "No proporcionado"
    email = request.form.get('email') or request.form.get('correo') or "No proporcionado"
    address = request.form.get('address') or request.form.get('direccion') or "No proporcionado"
    date = request.form.get('date') or request.form.get('fecha') or "No proporcionado"

  
    with open("usuarios.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Usuario: {nombre} | Correo: {email} | Dirección: {address} | Fecha: {date}\n")


    return render_template('form_result.html', 
                           name=nombre, 
                           email=email, 
                           address=address, 
                           date=date)

app.run(debug=True)
