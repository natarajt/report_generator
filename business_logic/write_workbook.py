from openpyxl import Workbook
def wirteToWorkbook(workbookName,cursor):
    print ("writing in to workbook " + workbookName)
    wb = Workbook()
    ws = wb.active
    ws.title = "Salary Report"
    ws.append([row[0] for row in cursor.description])
    results = cursor.fetchall()
    for row in results:
        ws.append(row)
    wb.save(workbookName)
    return