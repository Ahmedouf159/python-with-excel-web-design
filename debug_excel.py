import os
import pandas as pd

grades_path = r"i:\Ahmed\websites\python with excel\student.xlsx"
addresses_path = r"i:\Ahmed\websites\python with excel\add.xlsx"

print("🔎 Checking if files exist...")

if os.path.exists(grades_path):
    print(f"✔ Found student file: {grades_path}")
else:
    print(f"❌ File not found: {grades_path}")

if os.path.exists(addresses_path):
    print(f"✔ Found address file: {addresses_path}")
else:
    print(f"❌ File not found: {addresses_path}")

print("\n📄 Reading sheet names...")
try:
    print("Student file sheets:", pd.ExcelFile(grades_path).sheet_names)
    print("Address file sheets:", pd.ExcelFile(addresses_path).sheet_names)
except Exception as e:
    print("❌ Error while reading sheets:", e)

print("\n📥 Trying to read specific sheets...")
try:
    grades_df = pd.read_excel(grades_path, sheet_name="Grades")
    print("✔ Read 'Grades' sheet successfully.")
except Exception as e:
    print("❌ Failed to read 'Grades':", e)

try:
    addresses_df = pd.read_excel(addresses_path, sheet_name="Sheet1")
    print("✔ Read 'Sheet1' sheet successfully.")
except Exception as e:
    print("❌ Failed to read 'Sheet1':", e)
