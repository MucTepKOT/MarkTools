import xml.etree.ElementTree as ET
import os
import shutil

def separate_list(lst, n):
    '''разделяет список на двумерный список в каждом елементе которого n элементов ([1,2,3,4] --> [[1,2],[3,4]] при n=2) '''
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def xml_builder(order_dict):
    elem = {"xmlns": "urn:oms.order", "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", "xsi:schemaLocation": "urn:oms.order order-v5.0.xsd"}

    root = ET.Element("order", elem)
    shoes = ET.SubElement(root, 'shoes')
    productGroupe = ET.SubElement(shoes, 'productGroupe')
    productGroupe.text = order_dict['productGroupe'][0]
    contactPerson = ET.SubElement(shoes, 'contactPerson')
    contactPerson.text = order_dict['contactPerson'][0]
    releaseMethodType = ET.SubElement(shoes, 'releaseMethodType')
    releaseMethodType.text = order_dict['releaseMethodType'][0]
    createMethodType = ET.SubElement(shoes, 'createMethodType')
    createMethodType.text = order_dict['createMethodType'][0]
    contractNumber = ET.SubElement(shoes, 'contractNumber')
    contractNumber.text = order_dict['contractNumber'][0]
    contractDate = ET.SubElement(shoes, 'contractDate')
    contractDate.text = order_dict['contractDate'][0]
    products = ET.SubElement(shoes, 'products')

    # если ты решил, что выше полная дичь написана, спешу тебя огорчить, самый пиздец ниже
    # задача такая: при формировании xml, в products может быть не > 10 product
    # на вход подаётся xlsx, в котором мы находим пары gtin, quantity
    # из которых составляется products

    sep_product_code_list = separate_list(order_dict['product_code'], 10)
    print(sep_product_code_list)
    sep_quantity_list = separate_list(order_dict['quantity'], 10)
    print(sep_quantity_list)
    big_codes_and_quantity = zip(sep_product_code_list, sep_quantity_list)

    counter = 0
    filepath = f'{os.getcwd()}\\xml_dir'
    print(filepath)
    

    for product_code, quantity in big_codes_and_quantity:
        small_codes_and_quantity = dict(zip(product_code, quantity))
        for key, value in small_codes_and_quantity.items():
            product = ET.Element('product')
            gtin = ET.SubElement(product, 'gtin')
            gtin.text = key
            quantity = ET.SubElement(product, 'quantity')
            quantity.text = value
            serialNumberType = ET.SubElement(product, 'serialNumberType')
            serialNumberType.text = 'OPERATOR'
            templateId = ET.SubElement(product, 'templateId')
            templateId.text = '1'
            products.append(product)
        tree = ET.ElementTree(root)
             
        filename = f'answer{counter}.xml'
        tree.write(os.path.join(filepath, filename), encoding="utf-8")
        counter += 1
    
    shutil.make_archive('answer', 'zip', filepath, filepath)
    print(f'{os.getcwd()}\\archives')
