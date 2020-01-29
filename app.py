import json
import os
import flask
from werkzeug.utils import secure_filename
from openpyxl import load_workbook
import convert_func
import do_xml


UPLOAD_FOLDER = f'{os.getcwd()}\\uploads'
ALLOWED_EXTENSIONS = set(['xlsx'])

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

def response(code, data):
    return flask.Response(
        status = code,
        mimetype = "application/json",
        response = json.dumps(data) + "\n"
    )

@app.route('/')
def main():
    return flask.render_template('home.html')

@app.route('/', methods=['GET'])
def main_page():
    return response(200, {"status": "OK"})

@app.route('/converter')
def converter():
    id_code = flask.request.args.get('id_code')
    if id_code:
        output_1 = convert_func.convert_to_PC(id_code)
    else:
        output_1 = 'Введите идентификационный код'
    
    product_code = flask.request.args.get('product_code')
    if product_code:
        output_2 = convert_func.convert_to_IC(product_code)
    else:
        output_2 = 'Введите продуктовый код'
    return flask.render_template('converter.html', product_code=output_1, id_code=output_2)

@app.route('/order_codes', methods=['GET'])
def order_codes():
    return flask.render_template('order_codes.html')

@app.route('/user_input', methods=['POST'])
def user_input():
    order_dict = flask.request.form.to_dict(flat=False)
    print(order_dict)
    do_xml.xml_builder(order_dict)
    path = "answer.zip"
    return flask.send_file(path, as_attachment=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_xlsx(filepath):
    wb = load_workbook(filepath)
    ws = wb['Данные']
    all_gtin = ws['B']
    all_gtin_list = []
    all_quantity = ws['S']
    all_quantity_list = []
    for row in all_gtin[6:-1]:
        all_gtin_list.append(str(row.value))
    for row in all_quantity[6:-1]:
        all_quantity_list.append(str(row.value))
    return [all_gtin_list, all_quantity_list]

@app.route('/user_file', methods=['POST'])
def user_file():
    order_dict = flask.request.form.to_dict(flat=False)
    print(order_dict)
    file = flask.request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        gtin_and_quantity_lists = parse_xlsx(filepath)
        order_dict['product_code'] = gtin_and_quantity_lists[0]
        order_dict['quantity'] = gtin_and_quantity_lists[1]
        do_xml.xml_builder(order_dict)
        path = "answer.zip"
        return flask.send_file(path, as_attachment=True)
    return '404'


if __name__ == '__main__':
    app.run(debug=True)