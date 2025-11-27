from flask import Flask

app = Flask(__name__)

# ---------- HTML BASE REUTILIZABLE ----------
html_base = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {{
            background: #f7f7f7;
            font-family: Arial, sans-serif;
        }}
        .card {{
            margin-top: 60px;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }}
        h1, h2 {{
            text-align: center;
            font-weight: 700;
        }}
    </style>
</head>
<body>

<div class="container">
    <div class="card">
        {contenido}
    </div>
</div>

</body>
</html>
"""

@app.route('/')
def home():
    contenido = "<h1>🚀 Bienvenido a la Web de GRUPOX</h1><p style='text-align:center;'>Esta es una página Flask con estilo mejorado.</p>"
    return html_base.format(titulo="Inicio", contenido=contenido)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    contenido = f"<h2>Hola {nombre} 👋</h2><p style='text-align:center;'>Bienvenido a angel.pyangel.com</p>"
    return html_base.format(titulo="Saludo", contenido=contenido)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
