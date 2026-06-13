raw_terminal_logs = [
    "user:amna | status:success | attempts:1",
    "user:ali | status:failed | attempts:4",
    "user:amna | status:success | attempts:1",      # Duplicate! Skip it.
    "user:usman | status:failed | attempts:3",
    "user:aima | status:failed | attempts:CORRUPT", # Broken number! Handle safely.
    "user:zain | status:success | attempts:1"
]

unique_names = []
seen_names = set()
print("\n--- Phase 1: Terminal Line Audit ---")
for index, user in enumerate(raw_terminal_logs, start=1):
    current_name = user.split(" | ")[0].split(":")[1]
    if current_name not in seen_names:
        print(f"Line {index} : processing logs for {current_name}")
        unique_names.append(user)
        seen_names.add(current_name)
    else:
        print(f"line {index} : duplicate entry skipped for {current_name}")

print("\n--- Phase 2: System Processing Errors ---")


def parse_log(log_string):
    try:
        segments = log_string.split(" | ")
        username = segments[0].split(":")[1]
        status = segments[1].split(":")[1]
        attempts = int(segments[2].split(":")[1])
        return {
            "username": username,
            "status": status,
            "attempts": attempts,
        }
    except (ValueError, IndexError):
        actual_row = raw_terminal_logs.index(log_string) + 1
        username = log_string.split(" | ")[0].split(":")[1]
        print(f"[ERROR] Failed to read login attempts for user {username} on Row {actual_row}!")
        return None


def access_risk(attempts):
    return "High Risk" if attempts >= 3 else "Low Risk"


threat_board = []
for log in unique_names:
    parsed_data = parse_log(log)
    if parsed_data is not None:
        threat_board.append({
            "username": parsed_data["username"],
            "status": parsed_data["status"],
            "attempts": parsed_data["attempts"],
            "risk": access_risk(parsed_data["attempts"]),
        })

print("\n--- Phase 3: High Risk Threat Board ---")
import pprint
pprint.pprint(threat_board, sort_dicts=False)


