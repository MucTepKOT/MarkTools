import json
import flask
import convert_func
import do_xml

app = flask.Flask(__name__)

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

# @app.route('/id_code', methods=['GET'])
# def get_id_code(product_code):
#     product_code = flask.request.args.get('product_code')
#     id_code = convert_func.convert_to_IC(product_code)
#     return response(200, {"id_code": id_code})


# @app.route('/product_code', methods=['GET'])
# def get_product_code(id_code):
#     id_code = flask.request.args.get('id_code')
#     product_code = convert_func.convert_to_PC(id_code)
#     return response(200, {"product_code": product_code})


@app.route('/order_codes', methods=['GET'])
def order_codes():
    return flask.render_template('order_codes.html')

@app.route('/uploads', methods=['POST'])
def download():
    order_dict = flask.request.form.to_dict(flat=False)
    print(order_dict)
    do_xml.xml_builder(order_dict)
    path = "answer.xml"
    return flask.send_file(path, as_attachment=True)

    # order_dict = flask.request.get_json()
    # do_xml.xml_builder(order_dict)
    # path = "answer.xml"
    # return flask.send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)