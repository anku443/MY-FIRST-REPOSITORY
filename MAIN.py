import streamlit as st
from PREDICTION_HELPER import predict

# Set page configuration for a modern look
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling cards, fonts, and buttons
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem 1rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    div.block-container {
        padding-top: 2rem;
    }
    .card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title('🏥 Health Insurance Cost Predictor')
st.markdown("Estimate your expected health insurance premium instantly by providing your profile details below.")
st.markdown("---")

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Layout using structured containers with custom sections
with st.container():
    st.markdown("### 👤 Personal & Family Background")
    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
    with c2:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
    with c3:
        gender = st.selectbox('Gender', categorical_options['Gender'])

st.markdown("")

with st.container():
    st.markdown("### 💼 Financial & Risk Profile")
    c1, c2, c3 = st.columns(3)
    with c1:
        income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)
    with c2:
        genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
    with c3:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

st.markdown("")

with st.container():
    st.markdown("### 🌿 Lifestyle & Health Status")
    c1, c2, c3 = st.columns(3)
    with c1:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with c2:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
    with c3:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

st.markdown("")

with st.container():
    st.markdown("### 🛡️ Plan & Location Details")
    c1, c2, c3 = st.columns(3)
    with c1:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
    with c2:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with c3:
        region = st.selectbox('Region', categorical_options['Region'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

st.markdown("---")

# Center alignment for the prediction button and output
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    predict_clicked = st.button('✨ Calculate Insurance Cost')

if predict_clicked:
    with st.spinner('Analyzing your profile and calculating estimated cost...'):
        prediction = predict(input_dict)
    
    st.markdown("### 📊 Prediction Result")
    st.success(f"### Predicted Health Insurance Cost: ₹ {prediction:,.2f}" if isinstance(prediction, (int, float)) else f"### Predicted Health Insurance Cost: {prediction}")