import xlrd  # 引入xlrd模块
import json  # 引入json模块
import openpyxl


def convert():
    wb_obj = openpyxl.load_workbook('multilanguage.xlsx')  # 打开excel文件对象
    table = wb_obj.active
    table.delete_rows(1)
    en = {}
    zh = {}
    for r in table.iter_rows():  # 去除表头所有从第一行开始
        str = r[0].value
        en_str = r[1].value
        zh_str = r[2].value
        en[str] = en_str
        zh[str] = zh_str
    return en, zh


def main():
    en, zh = convert()
    # Writing JSON data
    with open('en.json', 'w') as f:
        json.dump(en, f)
    with open('zh-cn.json', 'w', encoding='utf-8') as f2:
        json.dump(zh, f2, ensure_ascii=False)
    with open('zh.json', 'w', encoding='utf-8') as f3:
        json.dump(zh, f3, ensure_ascii=False)
    print("convert to json success")


main()
