import pandas as pd
from models import db, Student
from datetime import datetime

def process_excel_files(grades_file_path, addresses_file_path):
    grades_df = pd.read_excel(grades_file_path, sheet_name="Grades")
    addresses_df = pd.read_excel(addresses_file_path, sheet_name="Sheet1")
    merged_df = pd.merge(grades_df, addresses_df, on='StudentName')

    for _, row in merged_df.iterrows():
        name = row['StudentName']
        math = row['Math']
        english = row['English']
        science = row['Science']
        address = row['Address']

        exists = Student.query.filter_by(name=name).first()
        if exists:
            print(f"🟡 Skipping existing student: {name}")
            continue

        line_code = generate_unique_line_code()
        student = Student(
            name=name,
            math=math,
            english=english,
            science=science,
            address=address,
            line_code=line_code,
            created_at=datetime.now()
        )
        db.session.add(student)

    db.session.commit()
    print("✅ All valid students added successfully.")

def generate_unique_line_code():
    base_year = datetime.now().year
    count = Student.query.count() + 1
    return f"{str(count).zfill(3)}-{base_year}"
