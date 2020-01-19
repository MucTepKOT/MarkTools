import codecs
import base64

def convert_to_PC(idcode):
    '''converting idcode to product_code'''
    gtin = idcode[0:14]
    gtin_hex = str(hex(int(gtin)).lstrip("0x"))
    gtin_hex = gtin_hex.rjust(12,'0')
    serial = idcode[14:]
    serial_hex = ''
    for i in serial:
        a = str(hex(ord(i))).lstrip("0x")
        serial_hex += a
    idcode_hex = '444d' + gtin_hex + serial_hex
    product_code = codecs.encode(codecs.decode(idcode_hex, 'hex'), 'base64').decode()
    return product_code

def convert_to_IC(product_code):
    '''converting product_code to idcode'''
    idcode_hex = base64.b64decode(product_code).hex()
    # prefics = idcode_hex[:4]
    gtin_hex = idcode_hex[4:16]
    gtin = str(int(gtin_hex, 16)).rjust(14,'0')
    serial_hex = idcode_hex[16:]
    serial = bytes.fromhex(serial_hex).decode('utf-8')
    idcode = gtin + serial
    return idcode

# while True:
#     hello_text = input('Нажмите цифру для ввода: \n1.Код идентификации \n2.Продуктовый код\n3.Выход\nВаш выбор: ')
#     if hello_text == '1':
#         idcode = input('Введите код идентификации: ')
#         print('ProductCode: ' + convert_to_PC(idcode))
#     elif hello_text == '2':
#         product_code = input('Введите продуктовый код: ')
#         print('CodeId: ' + convert_to_IC(product_code) + '\n')
#     else:
#         print('Ну и пиздуй')
#         break