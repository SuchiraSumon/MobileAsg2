class HobbyModel:
    students = [
        {
            "id": 1,
            "name": "Nur Ezurin Farisha",
            "hobbies": ["Coding", "Software Development"],
            "image": "ezu.png",
            "details": "Passionate about coding and creating innovative software solutions. Excels in programming languages like Python & Java. Enjoys participating in hackathons and contributing to open-source projects."
        },
        {
            "id": 2,
            "name": "Thivya Sri Sivakumar",
            "hobbies": ["Painting", "Artworks"],
            "image": "thivya.png",
            "details": "Expresses creativity through painting and creating mesmerizing artworks. Participates in art exhibitions and collaborates on multimedia projects."
        },
        {
            "id": 3,
            "name": "Suchira A/P Sumon",
            "hobbies": ["Music", "Playing Instruments"],
            "image": "chira.png",
            "details": "Deep passion for music and skilled in playing various instruments. Expertise in guitar and keyboard. Actively involved in the university music club."
        },
        
    ]

    @classmethod
    def get_students(cls):
        return cls.students

    @classmethod
    def get_student(cls, student_id):
        return next((student for student in cls.students if student["id"] == student_id), None)