from Chefboost.outputs.rules import rules
import pandas as pd
import openpyxl as xl
import os

PATH = 'Chefboost/tests/dataset/golftest.xlsx'
COLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U',
        'V', 'W']


def get_object(d_f):
    result = d_f[:-1]
    return result


def get_answer(input_obj):
    result = rules.findDecision(input_obj)
    return result


def fill_answer(d_f):
    work_book = xl.load_workbook(PATH)
    work_sheet = work_book["Sheet1"]
    rows = df.shape[0]
    cols = df.shape[1]
    for i in range(rows):
        list_item = get_object(d_f.values[i])
        work_sheet[COLS[cols - 1] + str(i + 2)] = get_answer(list_item)
    work_book.save(PATH)


if __name__ == '__main__':
    df = pd.read_excel(PATH)
    print(df)
    fill_answer(df)
    os.startfile("F:\\Python\\Chefboost\\tests\\dataset\\golftest.xlsx")
