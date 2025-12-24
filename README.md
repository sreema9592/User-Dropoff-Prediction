# User Drop-Off Prediction System

## 📌 Overview
This project is a Machine Learning–based system that predicts whether a user is likely to stop using an application (user drop-off) based on activity and engagement patterns.  
The system also suggests actionable strategies to improve user retention.

## 🎯 Problem Statement
Many applications lose users due to inactivity, low engagement, or poor feature usage.  
Identifying such users early helps businesses take preventive actions like notifications, offers, or feature guidance.

## 💡 Solution
This project analyzes user behavior data and predicts drop-off risk using a Logistic Regression model.  
Based on the prediction, the system recommends actions to re-engage users.

## 🧠 Machine Learning Details
- Algorithm: Logistic Regression
- Features used:
  - Days since last login
  - Average session time
  - Active days in last month
  - Features used
- Output:
  - Drop-Off Risk: HIGH / LOW
  - Suggested actions for retention

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- NumPy
- Tkinter (GUI)
- CSV dataset

## 📂 Project Structure
USER_DROPOFF_PROJECT/
│
├── main.py # Model training and prediction logic
├── tk_test.py # GUI-based prediction interface
├── users.csv # Sample user data
├── data/ # Dataset storage
├── build/ # Build files
├── dist/ # Executable files
└── README.md

## ▶️ How to Run the Project
1. Clone the repository
2. Install dependencies:

## 📊 Sample Output
- User ID: 999
- Drop-Off Risk: HIGH
- Reasons:
- Long inactivity
- Low engagement
- Poor usage frequency
- Suggested Actions:
- Send re-engagement notification
- Show feature tutorial
- Provide special offer or discount

## 🚀 Future Enhancements
- Real-time data integration
- Mobile app integration
- Automated push notifications
- Deep learning–based prediction
- Dashboard visualization

## 👩‍💻 Author
**Sreema M S**  
Machine Learning | Software Enthusiast
