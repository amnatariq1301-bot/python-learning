student_records = [
    {"name": "Amna", "score": 85},
    {"name": "Zain", "score": 35},  
    {"name": "Ali", "score": 72},
    {"name": "Usman", "score": 90},
    {"name": "Aima", "score": 38}   
]

print("\n processing the student records")

for index, student in enumerate(student_records, start=1):
    name = student["name"]
    print(f"Row {index} : Processing {name}")

result = lambda x : x*1.10
print("\n--- Cleaned & Curved Passing Board ---")
for student in student_records:
    if student["score"] < 40:
        print(f" {student['name']} has score {student['score']} so he is not upto the passing criteria")
    else:
        
        final_res = round(result(student['score']))
        print(f" name: {student['name']} , curved score: {final_res}")
        