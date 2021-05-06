from services.excel.get import SheetTable

test_sheet = SheetTable('sample.xlsx')
test_sheet_json = test_sheet.extract_data()
# print(test_sheet_json)


print(help(test_sheet))