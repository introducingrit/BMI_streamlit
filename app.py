import streamlit as st
st.title("BMI Calculator ")
st.info("Enetr your weight and height to calculate your BMI")
weight=st.number_input("Weight (kg)", min_value=1.0)
height=st.number_input("Height (m)", min_value=0.1)
if st.button("Calculate BMI"):
    bmi=weight/(height**2)
    st.success(f"Your BMI is: {bmi:.2f}")
    if bmi<18.5:
        st.warning("You are underweight.")
    elif bmi<25:
        st.success("You have a normal weight.")
        st.balloons()
    elif bmi<30:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")

st.badge("BMI calculated successfully!")