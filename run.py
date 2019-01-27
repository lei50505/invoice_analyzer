#! /usr/bin/env python
# -*- coding: utf-8 -*-

#pylint:disable=too-many-locals,too-many-statements

"""doc"""

import os
import datetime
import traceback
from aip import AipOcr
from book import Book

def get_file_content(file_path):
    """doc"""
    with open(file_path, "rb") as file_oper:
        return file_oper.read()

def main():
    """doc"""

    secret_in = input("Input a Secret: ")

    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year

    secret = "%d" % (day * 20 + month * 11 + year)

    if secret_in != secret:
        print("Secret Error")
        return

    app_id = "11305089"
    api_key = "eZdMGCO8tIiOvXy0Nl2Po4Qw"
    secret_key = "pP2yPQWFYioW4zKdqvHANyIHzHpn8Ify"

    client = AipOcr(app_id, api_key, secret_key)

    book = Book("out.xlsx")
    book.create()
    sheet = book.get_active_sheet()
    sheet.get_cell(1, 1).set_val("发票代码")
    sheet.get_cell(1, 2).set_val("发票号码")
    sheet.get_cell(1, 3).set_val("开票日期")
    sheet.get_cell(1, 4).set_val("合计金额")
    sheet.get_cell(1, 5).set_val("合计税额")
    sheet.get_cell(1, 6).set_val("价税合计(小写)")
    sheet.get_cell(1, 7).set_val("价税合计(大写)")
    sheet.get_cell(1, 8).set_val("销售方名称")
    sheet.get_cell(1, 9).set_val("销售方纳税人识别号")
    sheet.get_cell(1, 10).set_val("购方名称")
    sheet.get_cell(1, 11).set_val("购方纳税人识别号")
    sheet.get_cell(1, 12).set_val("货物名称")
    sheet.get_cell(1, 13).set_val("规格型号")
    sheet.get_cell(1, 14).set_val("单位")
    sheet.get_cell(1, 15).set_val("数量")
    sheet.get_cell(1, 16).set_val("单价")
    sheet.get_cell(1, 17).set_val("金额")
    sheet.get_cell(1, 18).set_val("税率")
    sheet.get_cell(1, 19).set_val("税额")

    row_index = 2

    for (dir_path, _, file_names) in os.walk("in"):
        for file_name in file_names:
            file_path = dir_path + os.sep + file_name

            print(file_path)
            image = get_file_content(file_path)
            invoice_data = client.vatInvoice(image)

            if invoice_data.get("error_msg") is not None:
                print(invoice_data.get("error_msg"))
                continue
            print(invoice_data)
            # 发票代码
            invoice_code = invoice_data["words_result"]["InvoiceCode"]
            # 发票号码
            invoice_num = invoice_data["words_result"]["InvoiceNum"]
            # 开票日期
            invoice_date = invoice_data["words_result"]["InvoiceDate"]
            # 合计金额
            total_amount = invoice_data["words_result"]["TotalAmount"]
            # 合计税额
            total_tax = invoice_data["words_result"]["TotalTax"]
            # 价税合计(小写)
            amount_in_figuers = invoice_data["words_result"]["AmountInFiguers"]
            # 价税合计(大写)
            amount_in_words = invoice_data["words_result"]["AmountInWords"]
            # 销售方名称
            seller_name = invoice_data["words_result"]["SellerName"]
            # 销售方纳税人识别号
            seller_register_num = invoice_data["words_result"]["SellerRegisterNum"]
            # 购方名称
            purchaser_name = invoice_data["words_result"]["PurchaserName"]
            # 购方纳税人识别号
            purchaser_register_num = invoice_data["words_result"]["PurchaserRegisterNum"]

            print("发票代码: ", invoice_code)
            print("发票号码: ", invoice_num)
            print("开票日期: ", invoice_date)
            print("合计金额: ", total_amount)
            print("合计税额: ", total_tax)
            print("价税合计(小写): ", amount_in_figuers)
            print("价税合计(大写): ", amount_in_words)
            print("销售方名称: ", seller_name)
            print("销售方纳税人识别号: ", seller_register_num)
            print("购方名称: ", purchaser_name)
            print("购方纳税人识别号: ", purchaser_register_num)

            # 货物名称
            commodity_name_word = invoice_data["words_result"]["CommodityName"][0]["word"]
            # 规格型号
            commodity_type_word = invoice_data["words_result"]["CommodityType"][0]["word"]
            # 单位
            commodity_unit_word = invoice_data["words_result"]["CommodityUnit"][0]["word"]
            # 数量
            commodity_num_word = invoice_data["words_result"]["CommodityNum"][0]["word"]
            # 单价
            commodity_price_word = invoice_data["words_result"]["CommodityPrice"][0]["word"]
            # 金额
            commodity_amount_word = invoice_data["words_result"]["CommodityAmount"][0]["word"]
            # 税率
            commodity_tax_rate_word = invoice_data["words_result"]["CommodityTaxRate"][0]["word"]
            # 税额
            commodity_tax_word = invoice_data["words_result"]["CommodityTax"][0]["word"]

            print("货物名称: ", commodity_name_word)
            print("规格型号: ", commodity_type_word)
            print("单位: ", commodity_unit_word)
            print("数量: ", commodity_num_word)
            print("单价: ", commodity_price_word)
            print("金额: ", commodity_amount_word)
            print("税率: ", commodity_tax_rate_word)
            print("税额: ", commodity_tax_word)



            sheet.get_cell(row_index, 1).set_val(invoice_code)
            sheet.get_cell(row_index, 2).set_val(invoice_num)
            sheet.get_cell(row_index, 3).set_val(invoice_date)
            sheet.get_cell(row_index, 4).set_val(total_amount)
            sheet.get_cell(row_index, 5).set_val(total_tax)
            sheet.get_cell(row_index, 6).set_val(amount_in_figuers)
            sheet.get_cell(row_index, 7).set_val(amount_in_words)
            sheet.get_cell(row_index, 8).set_val(seller_name)
            sheet.get_cell(row_index, 9).set_val(seller_register_num)
            sheet.get_cell(row_index, 10).set_val(purchaser_name)
            sheet.get_cell(row_index, 11).set_val(purchaser_register_num)
            sheet.get_cell(row_index, 12).set_val(commodity_name_word)
            sheet.get_cell(row_index, 13).set_val(commodity_type_word)
            sheet.get_cell(row_index, 14).set_val(commodity_unit_word)
            sheet.get_cell(row_index, 15).set_val(commodity_num_word)
            sheet.get_cell(row_index, 16).set_val(commodity_price_word)
            sheet.get_cell(row_index, 17).set_val(commodity_amount_word)
            sheet.get_cell(row_index, 18).set_val(commodity_tax_rate_word)
            sheet.get_cell(row_index, 19).set_val(commodity_tax_word)
            row_index += 1

    book.save()
    book.close()
    print("Success")

if __name__ == '__main__':
    try:
        main()
    except BaseException:
        print(traceback.format_exc())
    input("Press Enter to Continue:")
