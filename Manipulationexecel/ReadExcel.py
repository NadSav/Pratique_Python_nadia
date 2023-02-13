import openpyxl

wk=openpyxl.load_workbook("C:\\Users\\inspiron\\Downloads\\data.xlsx")
print(type(wk))
sheets=wk.sheetnames
print(sheets)
# recuperer le nom de la feuille active
print(wk.active.title)
#option1 acceder aux donnes d,une feuillede wk
sh1=wk["noms"]
print(type(sh1))
d1=sh1["B1"].value
print(d1)
print(type(sh1["B3"]))
print(wk["noms"]["B3"].value)
#Exercice
wk["notes"]["A2"].value
print(wk["notes"]["A2"].value)
#option2
