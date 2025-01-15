from flask import Flask, render_template, request

app = Flask(__name__)

data = [
    {"name": "Efraín Cruz Trejo", "position": "Presidente Consejo", "phone": "4142310060", "email": "presidenteconsejo@giftzin.com"},
    {"name": "Gerardo Frías Aguilera", "position": "Gerencia General", "phone": "4142267636", "email": "gerenciageneral@giftzin.com"},
    {"name": "Osbaldo Nieto Rodríguez", "position": "Contabilidad", "phone": "4142320129", "email": "contabilidad@giftzin.com"},
    {"name": "Jimena Olguín Trejo", "position": "Talento humano", "phone": "4141140022", "email": "talentohumano@giftzin.com"},
    {"name": "Uriel Iván Martínez Vega", "position": "Innovación y Diseño", "phone": "4142192832", "email": "innovacionydiseno@giftzin.com"},
    {"name": "Elvira Cruz Trejo", "position": "Gerencia Marketing e Innovación", "phone": "4142315956", "email": "marketingeinnovacion@giftzin.com"},
    {"name": "María de Jesús Reséndiz Valencia", "position": "Gerencia Administrativa", "phone": "4141070664", "email": "administrativo@giftzin.com"},
    {"name": "Alessandra Hernández Martínez", "position": "Auxiliar de diseño", "phone": "4141000839", "email": "diseno@giftzin.com"},
    {"name": "José Alejandro Hernández Chacón", "position": "Cobranza", "phone": "4141192485", "email": "cobranza@giftzin.com"},
    {"name": "Gustavo Alejandro Cruz Trejo", "position": "Compras", "phone": "4142808728", "email": "compras@giftzin.com"},
    {"name": "Isabel Morán Hernández", "position": "Mejora continua", "phone": "4141224702", "email": "mejoracontinua@giftzin.com"},
    {"name": "Jesús Antonio Hernández Rangel", "position": "Logística", "phone": "4141030543", "email": "logistica@giftzin.com"},
    {"name": "Mayra Teresa Jiménez García", "position": "Almacén", "phone": "4142320165", "email": "almacen@giftzin.com"},
    {"name": "Sergio Guerrero Rivera", "position": "Ventas Mercado Libre", "phone": "4141199529", "email": "mercadolibre@giftzin.com"},
    {"name": "Leticia Velasco Girón", "position": "Ventas Online", "phone": "4271841709", "email": "ventasonline@giftzin.com"},
    {"name": "Rafaela Reséndiz Valencia", "position": "Cortes y conteo", "phone": "4272311106", "email": "cortes@giftzin.com"},
    {"name": "María José Pérez Lugo", "position": "Compras Nacionales", "phone": "4141075931", "email": "comprasestrategicas@giftzin.com"},
    {"name": "Araceli Adriana Hernández Bautista", "position": "Auxiliar de Marketing", "phone": "4272020119", "email": "marketingypublicidad@giftzin.com"},
    {"name": "Alejandro Machuca", "position": "Sistemas e Infraestructura", "phone": "4411386593", "email": "infraestructuratecnologica@giftzin.com"},
    {"name": "José Iván Guerrero González", "position": "Líder Sucursal Giftzin Importaciones", "phone": "4141190764", "email": "lidersucursalimportaciones@giftzin.com"},
    {"name": "Jorge Axel Chávez Piñón", "position": "Líder Sucursal Giftzin Quiroga", "phone": "4436457333", "email": "lidersucursalquiroga@giftzin.com"},
    {"name": "Ángel Israel Huerta Torres", "position": "Líder Sucursal Giftzin Home", "phone": "4142310304", "email": "lidersucursalhome@giftzin.com"},
    {"name": "Gabriela Martínez González", "position": "Líder Sucursal Giftzin CDMX", "phone": "5564662158", "email": "lidersucursalcdmx@giftzin.com"},
    {"name": "Rubén Cruz Méndez", "position": "Líder Rutas", "phone": "5521113149", "email": "liderrutas@giftzin.com"},
    {"name": "Adán Edrey Rico Aguayo", "position": "Ventas Online", "phone": "4141123803", "email": "ventasonline2@giftzin.com"},
]

@app.route('/')
def index():
    query = request.args.get('query', '').lower()
    if query:
        filtered_data = [person for person in data if query in person['name'].lower()]
    else:
        filtered_data = data
    return render_template('index.html', data=filtered_data, query=query)

if __name__ == '__main__':
    app.run(debug=True)
