from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

productos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre_producto = request.form['nombre']
        precio_producto = request.form['precio']
        productos.append({'nombre': nombre_producto, 'precio': precio_producto})
        return redirect(url_for('index'))
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
