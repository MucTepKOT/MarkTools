import codecs
import base64

def do_hex(data):
    '''doing hex from string'''
    idcode_hex = base64.b64decode(data).hex()
    return idcode_hex

def convert_to_PC(gtin, serial, gcode_hex):
    '''converting idcode to product_code'''
    # gtin = idcode[0:14]
    gtin_hex = str(hex(int(gtin)).lstrip("0x"))
    gtin_hex = gtin_hex.rjust(12,'0')
    # serial = idcode[14:]
    serial_hex = ''
    for i in serial:
        a = str(hex(ord(i))).lstrip("0x")
        serial_hex += a
    idcode_hex = gcode_hex + gtin_hex + serial_hex
    product_code = codecs.encode(codecs.decode(idcode_hex, 'hex'), 'base64').decode()
    return product_code, idcode_hex

def convert_to_IC(**kwargs):
    '''converting product_code to idcode'''
    if kwargs.get('product_code'):
        idcode_hex = do_hex(kwargs['product_code'])
    if kwargs.get('product_code_hex'):
        idcode_hex = kwargs['product_code_hex']
    # prefics = idcode_hex[:4]
    gtin_hex = idcode_hex[4:16]
    gtin = str(int(gtin_hex, 16)).rjust(14,'0')
    serial_hex = idcode_hex[16:]
    serial = bytes.fromhex(serial_hex).decode('utf-8')
    idcode = gtin + serial
    return idcode