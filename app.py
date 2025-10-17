import streamlit as st
import pickle
import json
import numpy as np

# Load model and columns
with open('banglore_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']

locations = data_columns[3:]

# 🎨 Page Config
st.set_page_config(page_title="🏡 Bangalore House Price Prediction", layout="centered")

# 🎨 Custom CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
        }
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1507089947368-19c1da9775ae?auto=format&fit=crop&w=1600&q=80");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            color: white;
        }
        .main-container {
            background-color: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 40px;
            max-width: 600px;
            margin: 60px auto;
            box-shadow: 0 0 25px rgba(0,0,0,0.5);
        }
        h1 {
            text-align: center;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 30px;
        }
        label {
            font-size: 16px;
            font-weight: 500;
            color: #f0f0f0 !important;
        }
        input {
            border-radius: 8px !important;
        }
        .stepper {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        .stepper button {
            background-color: #6C63FF;
            color: white;
            border: none;
            border-radius: 8px;
            width: 35px;
            height: 35px;
            font-size: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .stepper button:hover {
            background-color: #4e47d0;
        }
        /* Updated Predict Button */
        .predict-btn button {
            width: 100%;
            background-color: #1a1a1a; /* Dark professional color */
            color: #ffffff; /* White text */
            border: none;
            border-radius: 12px;
            padding: 12px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s ease, transform 0.2s ease;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        .predict-btn button:hover {
            background-color: #333333;
            transform: translateY(-2px);
            box-shadow: 0 7px 20px rgba(0,0,0,0.5);
        }
        /* Updated Price Box Text */
        .price-box {
            text-align: center;
            background-color: rgba(255,255,255,0.15);
            border-radius: 10px;
            padding: 12px;
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
            color: #000000; /* Dark black text */
        }
    </style>
""", unsafe_allow_html=True)

# 🏠 App Layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("<h1> Bangalore House Price Prediction</h1>", unsafe_allow_html=True)

# Inputs
area = st.number_input("Area (Square Feet)", min_value=300, max_value=10000, value=1000, step=50)

# Stepper for BHK
st.markdown("**BHK**")
col1, col2, col3 = st.columns([1, 2, 1])
if 'bhk' not in st.session_state:
    st.session_state.bhk = 3

with col1:
    if st.button("➖", key="bhk_minus") and st.session_state.bhk > 1:
        st.session_state.bhk -= 1
with col2:
    st.markdown(f"<div style='text-align:center;font-size:20px;font-weight:bold'>{st.session_state.bhk}</div>", unsafe_allow_html=True)
with col3:
    if st.button("➕", key="bhk_plus") and st.session_state.bhk < 10:
        st.session_state.bhk += 1

# Stepper for Bathrooms
st.markdown("**Bathrooms**")
col4, col5, col6 = st.columns([1, 2, 1])
if 'bath' not in st.session_state:
    st.session_state.bath = 2

with col4:
    if st.button("➖", key="bath_minus") and st.session_state.bath > 1:
        st.session_state.bath -= 1
with col5:
    st.markdown(f"<div style='text-align:center;font-size:20px;font-weight:bold'>{st.session_state.bath}</div>", unsafe_allow_html=True)
with col6:
    if st.button("➕", key="bath_plus") and st.session_state.bath < 10:
        st.session_state.bath += 1

location = st.selectbox("Location", sorted(locations))

# Prediction
st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
if st.button("  Predict Price"):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = area
    x[1] = st.session_state.bhk
    x[2] = st.session_state.bath
    if loc_index >= 0:
        x[loc_index] = 1

    prediction = round(model.predict([x])[0], 2)
    st.markdown(f'<div class="price-box"> Estimated Price: ₹ {prediction} Lakh</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)





