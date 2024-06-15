import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:\\Users\\Divyansh Bose\\PycharmProjects\\FaceRecognitionRealTimeDatabase\\.venv\\serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-748d0-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "254698":
            {
                "name": "Gaurank Joshi",
                "major": "CS    ",
                "starting_year": 2020,
                "total_attendance": 8,
                "standing": "G",
                "year": 4,
                "last_attendance_time": "2024-04-03 15:46:21"
            },
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "364876":
        {
            "name": "Kuldeepak Singh",
            "major": "CS",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-05-31 10:25:45"
        },
    "788654":
            {
                "name": "Dev Bharadwaj",
                "major": "CS",
                "starting_year": 2020,
                "total_attendance": 9,
                "standing": "G",
                "year": 4,
                "last_attendance_time": "2024-03-14 12:16:8"
            },
    "852741":
        {
            "name": "Divyansh Bose",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 10,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-06-01 12:45:25"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2021,
            "total_attendance": 5,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-07-18 09:15:41"
        },


}

for key, value in data.items():
    ref.child(key).set(value)