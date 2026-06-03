import streamlit as st
def add_number(a:int,b:int):
    return a+b
st.title(" MY first CI/CD pipeline with github action")
st.write("This is a simple addition app to test the github action workflow")
x= st.number_input("Enter the first number")
y= st.number_input("Enter the second number")
if st.button("Add"):
    result = add_number(x,y)
    st.write("The result of addition is ",result)