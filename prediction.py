import streamlit as st
import pickle
import pandas as pd

# Load the trained model from the pickle file
with open('rdf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define a dictionary to map numeric predictions to labels
outcome_labels = {0: 'Died', 1: 'Euthanized', 2: 'Lived'}

# Create a Streamlit app
st.title('Health Outcome Prediction for Horses')

# Define input fields
surgery = st.number_input('Surgery (1 for Yes, 0 for No)', min_value=0, max_value=1)
pulse = st.number_input('Pulse', min_value=0.0)
respiratory_rate = st.number_input('Respiratory Rate', min_value=0.0)
capillary_refill_time = st.number_input('Capillary Refill Time (Seconds)', min_value=0, max_value=10)
nasogastric_reflux_ph = st.number_input('Nasogastric Reflux pH', min_value=0.0)
packed_cell_volume = st.number_input('Packed Cell Volume', min_value=0.0)
total_protein = st.number_input('Total Protein', min_value=0.0)

# Input field for Abdomo Appearance
abdomo_appearance_options = {'Serosanguious': 1, 'Cloudy': 2, 'Other': 3}
abdomo_appearance = st.selectbox('Abdomo Appearance', options=list(abdomo_appearance_options.keys()))

abdomo_protein = st.number_input('Abdomo Protein', min_value=0.0)
surgical_lesion = st.number_input('Surgical Lesion (1 for Yes, 0 for No)', min_value=0, max_value=1)
lesion_2 = st.number_input('Lesion 2', min_value=0)
lesion_3 = st.number_input('Lesion 3', min_value=0)

# Map selected option to numeric value
abdomo_appearance_value = abdomo_appearance_options[abdomo_appearance]

# Make prediction
input_data = pd.DataFrame({
    'surgery': surgery,
    'pulse': pulse,
    'respiratory_rate': respiratory_rate,
    'capillary_refill_time': capillary_refill_time,
    'nasogastric_reflux_ph': nasogastric_reflux_ph,
    'packed_cell_volume': packed_cell_volume,
    'total_protein': total_protein,
    'abdomo_appearance': abdomo_appearance_value,
    'abdomo_protein': abdomo_protein,
    'surgical_lesion': surgical_lesion,
    'lesion_2': lesion_2,
    'lesion_3': lesion_3
}, index=[0])

if st.button('Predict'):
    prediction = model.predict(input_data)
    predicted_label = outcome_labels[prediction[0]] 
    st.write('Predicted Health Outcome:', predicted_label)
