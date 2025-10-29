import streamlit as st

# --- Streamlit Calculator App ---
st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations below.")

# --- User inputs ---
num1 = st.number_input("Enter first number", value=0.0)
operation = st.selectbox("Select operation", ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)"])
num2 = st.number_input("Enter second number", value=0.0)

# --- Perform operation ---
result = None
if st.button("Calculate"):
    if operation == "Add (+)":
        result = num1 + num2
    elif operation == "Subtract (-)":
        result = num1 - num2
    elif operation == "Multiply (×)":
        result = num1 * num2
    elif operation == "Divide (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("❌ Cannot divide by zero!")

# --- Display result ---
if result is not None:
    st.success(f"✅ Result: {result}")

st.caption("Built with ❤️ using Streamlit")
