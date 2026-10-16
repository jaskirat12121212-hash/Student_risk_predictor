import streamlit as st
import requests

st.title("Student risk predictor")

name=st.text_input("Enter your name")
marks_maths=st.number_input("Enter maths marks",min_value=0.0,max_value=100.0)
marks_science=st.number_input("Enter science marks",min_value=0.0,max_value=100.0)
marks_eng=st.number_input("Enter english marks",min_value=0.0,max_value=100.0)
attendance=st.number_input("Enter your attendance")

if st.button("Calculate risk"):
    if not name.strip():
        st.error("Please enter your name")
    else:
     data={
        "name":name,
        "attendance_percent":attendance,
        "marks_maths":marks_maths,
        "marks_science":marks_science,
        "marks_eng":marks_eng,
        "average":(marks_maths+marks_eng+marks_science)/3,
        }
    try:
        response=requests.post("http://127.0.0.1:8000/predict",json=data,timeout=10)
        response.raise_for_status()
        result=response.json()
        st.success("Analysis completed")
        st.metric("Average marks",result["avg_marks"])
        st.subheader(f"Risk level:{result['risk']}")
    except requests.RequestException as e :
        st.error(f"Backend error:{e}")

    

