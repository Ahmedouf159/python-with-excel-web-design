import pandas as pd

grades_file_path = r"i:\Ahmed\websites\python with excel\student.xlsx"
addresses_file_path = r"i:\Ahmed\websites\python with excel\add.xlsx"


print("Checking student.xlsx ...")
try:
    grades_sheets = pd.ExcelFile(grades_file_path).sheet_names
    print("✔ Sheets in student.xlsx:", grades_sheets)
except Exception as e:
    print("❌ Error reading student.xlsx:", e)

print("Checking ad.xlsx ...")
try:
    addresses_sheets = pd.ExcelFile(addresses_file_path).sheet_names
    print("✔ Sheets in ad.xlsx:", addresses_sheets)
except Exception as e:
    print("❌ Error reading ad.xlsx:", e)
