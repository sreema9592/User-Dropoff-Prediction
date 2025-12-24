import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv(
    "C:/Users/Sreema MS/OneDrive/Desktop/USER DROPOFF PROJECT/users.csv"
)

# Features & target
X = data[
    ["days_since_last_login", "avg_session_time", "days_active_last_month", "features_used"]
]
y = data["drop_off"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# ---- New user (example) ----
new_user = {
    "user_id": 999,
    "days_since_last_login": 20,
    "avg_session_time": 3,
    "days_active_last_month": 2,
    "features_used": 1
}

user_values = [[
    new_user["days_since_last_login"],
    new_user["avg_session_time"],
    new_user["days_active_last_month"],
    new_user["features_used"]
]]

prediction = model.predict(user_values)[0]

print("User ID:", new_user["user_id"])

# ----- RESULT -----
if prediction == 1:
    print("⚠️ Drop-Off Risk: HIGH")

    # Reason analysis
    reasons = []
    if new_user["days_since_last_login"] > 15:
        reasons.append("Long inactivity")
    if new_user["avg_session_time"] < 5:
        reasons.append("Low engagement")
    if new_user["days_active_last_month"] < 5:
        reasons.append("Poor usage frequency")

    print("Reason(s):", ", ".join(reasons))

    # Action recommendation
    print("Suggested Action:")
    if "Long inactivity" in reasons:
        print("- Send re-engagement notification")
    if "Low engagement" in reasons:
        print("- Show feature tutorial")
    if "Poor usage frequency" in reasons:
        print("- Provide special offer / discount")

else:
    print("✅ User Status: ACTIVE")
    print("No action required")

def predict_dropoff(days, session, active, features):
    if days > 15 and active < 5:
        return "HIGH"
    else:
        return "LOW"
def send_notification(user_id):
    print(f"⚠️ Notification sent to User {user_id}")
    print("Offer / Reminder triggered")

def auto_action(user_id, days, session, active, features):
    risk = predict_dropoff(days, session, active, features)

    if risk == "HIGH":
        send_notification(user_id)
        return "Drop-Off Risk HIGH → Notification Sent"
    else:
        return "User Active → No Action Needed"


