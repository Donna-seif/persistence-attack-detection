import json

with open("persistence.json", "r") as file:
    logs = json.load(file)

for log in logs:
    score = 0

    key = log.get("Key", "").lower()
    value = log.get("Value", "").lower()
    event_type = log.get("EventType", "").lower()
    command = log.get("Command", "").lower()

    # Registry Run key detection
    if "run" in key:
        score += 1

    if value == "evil.exe":
        score += 1

    # Scheduled task detection
    if event_type == "scheduledtask":
        score += 1

    if "evil.exe" in command:
        score += 1

    # Require at least 2 signals
    if score >= 2:
        print("🚨 Persistence detected:", log)
