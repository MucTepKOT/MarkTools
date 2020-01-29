# import os
# from openpyxl import load_workbook

# def parse_xlsx(filepath):
#     wb = load_workbook(filepath)
#     ws = wb['Данные']
#     all_gtin = ws['B']
#     all_gtin_list = []
#     all_quantity = ws['S']
#     all_quantity_list = []
#     for row in all_gtin[6:-1]:
#         all_gtin_list.append(row.value)
#     for row in all_quantity[6:-1]:
#         all_quantity_list.append(row.value)
#     return dict(zip(all_gtin_list, all_quantity_list))


# UPLOAD_FOLDER = f'{os.getcwd()}\\uploads'
# filename = 'uploaded_xlsx.xlsx'
# a = parse_xlsx(os.path.join(UPLOAD_FOLDER, filename))

# print(a)

def f(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

a = [1,2,3,4,45,5,6,8,8,98,0,9,234,3256,45,656,786,78,789,78,345,345,54,54,435,54,213,423,534,545,6,454,34,654,6]
b = ['a','b','s','d','sd','sd','as','asd','df','sdf','asd','bgf','gbf','fgb','df','fb','fb','fb','grt','hm','kk','hn','dfg','er','wer','ewr','vf','df','dfv','dfv']


c = f(a,10)
d = f(b,10)

print(c)
print()
print(d)
print()
for gtin, quant in zip(c,d):
    print(dict(zip(gtin, quant)))
