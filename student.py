from fastapi import FastAPI,Depends
from pydantic import BaseModel,Field

app=FastAPI()

class Student(BaseModel):
    name:str
    attendance_percent:float=Field(ge=0,le=100)
    marks_science :float=Field(ge=0,le=100)
    marks_maths :float=Field(ge=0,le=100)
    marks_eng :float=Field(ge=0,le=100)

@app.get('/')
def info():
    return{"This is analyser for the result "}
@app.post("/predict")
def predict(student:Student):
    avg_marks=(student.marks_science+student.marks_maths+student.marks_eng)/3
    risk=(student.attendance_percent<75 or  avg_marks<40)
    return {"student":student.name,
            "attendance":student.attendance_percent,
            "avg_marks":avg_marks,
            "risk":"high" if risk else "low",
            "message":"Needs to work harder " if risk else "passed"}

