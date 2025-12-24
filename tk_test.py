from main import auto_action
import tkinter as tk

# Create window
root = tk.Tk()
root.title("User Drop-Off Prediction")
root.geometry("400x350")

# Title
title = tk.Label(root, text="User Drop-Off Prediction", font=("Arial", 14))
title.pack(pady=10)

# Labels & Entry boxes
tk.Label(root, text="Days since last login").pack()
entry_last_login = tk.Entry(root)
entry_last_login.pack()

tk.Label(root, text="Average session time").pack()
entry_session = tk.Entry(root)
entry_session.pack()

tk.Label(root, text="Active days last month").pack()
entry_active_days = tk.Entry(root)
entry_active_days.pack()

import tkinter as tk
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ---------------- LOAD & TRAIN MODEL ----------------
data = pd.read_csv(
    "C:/Users/Sreema MS/OneDrive/Desktop/USER DROPOFF PROJECT/users.csv"
)

X = data[
    ["days_since_last_login", "avg_session_time", "days_active_last_month", "features_used"]
]
y = data["drop_off"]

model = LogisticRegression()
model.fit(X, y)

# ---------------- UI ----------------
root = tk.Tk()
root.title("User Drop-Off Prediction")
root.geometry("420x420")

tk.Label(root, text="User Drop-Off Prediction", font=("Arial", 14, "bold")).pack(pady=10)

# Input fields
tk.Label(root, text="Days since last login").pack()
entry_last_login = tk.Entry(root)
entry_last_login.pack()

tk.Label(root, text="Average session time").pack()
entry_session = tk.Entry(root)
entry_session.pack()

tk.Label(root, text="Active days last month").pack()
entry_active_days = tk.Entry(root)
entry_active_days.pack()

tk.Label(root, text="Features used").pack()
entry_features = tk.Entry(root)
entry_features.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=15)

# ---------------- PREDICT FUNCTION ----------------
def predict():
    try:
        values = [[
            int(entry_last_login.get()),
            int(entry_session.get()),
            int(entry_active_days.get()),
            int(entry_features.get())
        ]]

        prediction = model.predict(values)[0]

        if prediction == 1:
            result_label.config(
                text="⚠️ Drop-Off Risk HIGH\nAction: Send offer / notification",
                fg="red"
            )
        else:
            result_label.config(
                text="✅ User ACTIVE\nNo action required",
                fg="green"
            )

    except:
        result_label.config(
            text="❌ Please enter valid numbers",
            fg="black"
        )

# Predict button
def on_predict():
    user_id = entry_user_id.get()
    days = int(entry_days.get())
    session = int(entry_session.get())
    active = int(entry_active.get())
    features = int(entry_features.get())

    result = auto_action(user_id, days, session, active, features)

    result_label.config(text=result)


root.mainloop()
result_label = Label(root, text="")
result_label.pack()


