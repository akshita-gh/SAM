import pandas as pd
import datetime
import os

LOG_FOLDER = "attendance_logs"
LOG_FILE = os.path.join(LOG_FOLDER, "attendance.csv")


def mark_attendance(name):

    name = name.strip()

    if name == "":
        return False, "Name cannot be empty."

    os.makedirs(LOG_FOLDER, exist_ok=True)

    today = str(datetime.date.today())

    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    if os.path.exists(LOG_FILE):

        df = pd.read_csv(LOG_FILE)

        duplicate = df[
            (df["Name"] == name) &
            (df["Date"] == today)
        ]

        if not duplicate.empty:
            return False, f"{name} is already present today."

    new_data = pd.DataFrame({

        "Name": [name],

        "Date": [today],

        "Time": [current_time]

    })

    new_data.to_csv(

        LOG_FILE,

        mode="a",

        header=not os.path.exists(LOG_FILE),

        index=False

    )

    return True, "Attendance marked successfully."


def get_attendance_records():

    if os.path.exists(LOG_FILE):

        df = pd.read_csv(LOG_FILE)

        return df.values.tolist()

    return []


def view_attendance():

    if os.path.exists(LOG_FILE):

        df = pd.read_csv(LOG_FILE)

        print(df)

    else:

        print("No attendance records found.")