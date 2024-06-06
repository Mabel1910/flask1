from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesario para mostrar mensajes flash

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        # Aquí puedes procesar los datos como guardarlos en una base de datos o enviar un email
        flash(f'Formulario enviado por {nombre} con el correo {correo}!', 'success')
        return redirect(url_for('home'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
