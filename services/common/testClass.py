class myClass:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def myClassFunc(self):
        return self.val1 + self.val2

class1 = myClass(1000, 798)
print(class1.myClassFunc())

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename="hello_world.xlsx")