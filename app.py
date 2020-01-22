import json
import flask
import converter
import do_xml

app = flask.Flask(__name__)

def to_json(data):
    return json.dumps(data) + "\n"

def response(code, data):
    return flask.Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )

@app.route('/', methods=['GET'])
def main_page():
    return response(200, {"status": "OK"})


@app.route('/id_code', methods=['GET'])
def get_id_code(product_code):
    product_code = flask.request.args.get('product_code')
    id_code = converter.convert_to_IC(product_code)
    return response(200, {"id_code": id_code})


@app.route('/product_code', methods=['GET'])
def get_product_code(id_code):
    id_code = flask.request.args.get('id_code')
    product_code = converter.convert_to_PC(id_code)
    return response(200, {"product_code": product_code})


@app.route('/post_xml', methods=['POST'])
def get_xml():
    order_dict = flask.request.get_json()
    do_xml.xml_builder(order_dict)
    path = "answer.xml"
    return flask.send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)