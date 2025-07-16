import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def celsius_to_kelvin(c): return c + 273.15
def kelvin_to_celsius(k): return k - 273.15
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32

# Conversion logic
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "C":
        if to_unit == "F":
            return celsius_to_fahrenheit(value)
        elif to_unit == "K":
            return celsius_to_kelvin(value)
    elif from_unit == "F":
        if to_unit == "C":
            return fahrenheit_to_celsius(value)
        elif to_unit == "K":
            return fahrenheit_to_kelvin(value)
    elif from_unit == "K":
        if to_unit == "C":
            return kelvin_to_celsius(value)
        elif to_unit == "F":
            return kelvin_to_fahrenheit(value)
    else:
        raise ValueError("Invalid unit")

# Streamlit app setup
st.set_page_config(page_title="Temperature Converter", page_icon="🌡️")
st.title("🌡️ Temperature Converter")

st.markdown("Convert temperatures between **Celsius (C)**, **Fahrenheit (F)**, and **Kelvin (K)**.")

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Input fields
temp_value = st.number_input("🌡️ Enter temperature value:", value=0.0, step=0.1)
from_unit = st.selectbox(" Convert from:", ["C", "F", "K"])
to_unit = st.selectbox(" Convert to:", ["C", "F", "K"])

# Convert button
if st.button("Convert"):
    try:
        result = convert_temperature(temp_value, from_unit, to_unit)
        output = f"{temp_value}°{from_unit} = {result:.2f}°{to_unit}"
        st.success(output)
        st.session_state.history.append(output)
    except Exception as e:
        st.error(f"Error: {e}")

# Show conversion history
st.markdown("### 📜 Conversion History")
if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.write("•", item)
    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.experimental_rerun()
else:
    st.info("No conversions yet.")

#run using: python -m streamlit run temperature_converter_gui.py
