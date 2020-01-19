import xml.etree.ElementTree as ET


def xml_builder(order_dict):
    # gtin_list = ['04670033580052', '04670033580113', '04670033580013', '04670033580055']
    elem = {"xmlns": "urn:oms.order", "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", "xsi:schemaLocation": "urn:oms.order order-v5.0.xsd"}

    root = ET.Element("order", elem)
    shoes = ET.SubElement(root, 'shoes')
    productGroupe = ET.SubElement(shoes, 'productGroupe')
    productGroupe.text = 'shoes'
    contactPerson = ET.SubElement(shoes, 'contactPerson')
    contactPerson.text = 'Алексей'
    releaseMethodType = ET.SubElement(shoes, 'releaseMethodType')
    releaseMethodType.text = 'REMAINS'
    createMethodType = ET.SubElement(shoes, 'createMethodType')
    createMethodType.text = 'SELF_MADE'
    contractNumber = ET.SubElement(shoes, 'contractNumber')
    contractNumber.text = '55909'
    contractDate = ET.SubElement(shoes, 'contractDate')
    contractDate.text = '2019-11-04'
    products = ET.SubElement(shoes, 'products')

    print(order_dict)
    print(type(order_dict))

    for key, value in order_dict.items():
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
