import xml.etree.ElementTree as ET


def xml_builder(order_dict):
    # gtin_list = ['04670033580052', '04670033580113', '04670033580013', '04670033580055']
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

    codes_and_quantity = dict(zip(order_dict['product_code'], order_dict['quantity']))

    for key, value in codes_and_quantity.items():
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
    tree.write('answer.xml', encoding="utf-8")
