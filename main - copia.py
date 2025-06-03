# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')

    email = request.form.get("email")
    textContent = request.form.get("text")

    with open("mensajes.txt" , "a+", encoding = "utf-8") as archivo:
        archivo.write(email)
        archivo.write("\n")
        archivo.write(textContent)
        archivo.write("\n")

    

    return render_template('index.html', button_python=button_python)

if __name__ == "__main__":
    app.run(debug=True)
