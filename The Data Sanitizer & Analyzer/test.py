raw_data = [
    {"name" : "amna", "score" : 80},
    {"name" : "ali", "score" : 95},
    {"name" : "usman", "score" : 25},
    {"name" : "amna", "score" : 80},
    {"name" : "aima", "score" : "97"},
    {"name" : "asif", "score" : "N\A"},
]

unique_names = []
seen_names = []
high_performers = []
regular_performers = []
total_score_sum = 0
valid_user_count = 0

print("\n DATA CLEANING LOGS")

for user in raw_data:
    if user["name"] not in seen_names:
        unique_names.append(user)
        seen_names.append(user["name"])
    else:
        print(f"duplicate skipped : {user['name']}")


for user in unique_names:
    try:

        actual_score = int(user["score"])
        print(f"Successfully processed {user['name']} with score {actual_score}")
        total_score_sum += actual_score
        valid_user_count += 1
        if actual_score >= 80:
            high_performers.append(user["name"])
        else:
            regular_performers.append(user["name"])

    except ValueError:
        print(f"Could not process {user['name']} due to invalid {user['score']}")

print("\n FINAL ANALYTICS REPORT")
print(f"Total valid users: {valid_user_count}")
if valid_user_count > 0:
    average_score = total_score_sum / valid_user_count
    print(f"Average Score {average_score}")
else:
    print("Average System Score: 0.0 (No valid data points found)")

print(f"\nHigh Performers (>= 80): {high_performers}")
print(f"Regular Performers (< 80): {regular_performers}")


