import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('Pasien_liver.sav', 'rb'))

st.title('prediksi penyakit liver')

col1, col2, col3 = st.columns(3)

with col1:
    Age = st.number_input('Umur')
with col2:
    Total_Bilirubin = st.number_input('Jumlah Bilirubin')
with col3:
    Direct_Bilirubin = st.number_input('Bilirubin Yang Tidak Terkonjungsi')
with col1:
    Alkaline_Phosphotase = st.number_input('Jumlah Kadar ALP')
with col2:
    Alamine_Aminotransferase = st.number_input('Jumlah Enzim Dalam Darah')
with col3:
    Aspartate_Aminotransferase = st.number_input('Jumlah AST')
with col1:
    Total_Protiens = st.number_input('Jumlah Protein')
with col2:
    Albumin = st.number_input('Jumlah Protein Pada Darah')
with col3:
    Albumin_and_Globulin_Ratio = st.number_input('Rasio Albumin dan Globulin ')

liver_diagnosis =''

if st.button('Prediksi Pebyakit Liver'):
    liver_prediction = model.predict([[Age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
    
    if (liver_prediction[0]==1):
        liver_diagnosis = 'Pasien Tidak Terkena Penyakit Liver'
    else:
        liver_diagnosis = 'Pasien Terkena Penyakit Liver'
st.success(liver_diagnosis)
    
