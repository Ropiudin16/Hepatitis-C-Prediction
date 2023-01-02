import streamlit as st
import pandas as pd
from PIL import Image
import pickle

st.set_page_config(
    page_title='Hepatitis',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

# Title
st.title('Hepatitis C Prediction Dataset')
st.write('Hepatitis C adalah peradangan pada hati akibat infeksi virus hepatisis C. Jika berlangsung lama, hepatitis C dapat menyebabkan penyakit hati kronis, gagal hati, hingga kanker hati. Virus hepatitis C menular melalui darah. Hal ini bisa terjadi lewat transfusi darah atau penggunaan jarum suntik bersama. Oleh sebab itu, perlu dilakukan klasifikasi terhadap pasien yang ingin melakukan donor darah apakan mengidap penyakit hepatisis C berdasarkan darahnya')

# import image
image = Image.open('Image.jpg')
st.image(image)

# Step 1 - import saved model
model = pickle.load(open("M2P1_pred.pkl", "rb"))

st.write('Insert feature to predict')

# Step 2 - prepare input data for user

Age = st.number_input(label='Age (year)', min_value=19, max_value=77, value=47, step=1)
Sex = st.selectbox(label='Sex', options=['m', 'f'], key=1, help = 'm : male , f : female')
ALB = st.slider(label='Albumin Blood Test', min_value=14.90, max_value=82.20, value=41.00, step=0.1)
ALP = st.slider(label='Alkaline phosphatase', min_value=11.30, max_value=416.60, value=66.00, step=0.1)
ALT = st.slider(label='Alanine Transaminase', min_value=0.90, max_value=325.30, value=23.00, step=0.1)
AST = st.slider(label='Aspartat Transaminase', min_value=10.60, max_value=324.00, value=25.00, step=0.1)
BIL = st.slider(label='Bilirubin', min_value=0.80, max_value=254.00, value=7.00, step=0.1)
CHE = st.slider(label='Acetylcholinesterase', min_value=1.42, max_value=16.41, value=8.00, step=0.1)
CHOL = st.slider(label='Cholesterol', min_value=1.43, max_value=9.67, value=5.00, step=0.1)
CREA = st.slider(label='Creatinine', min_value=8.00, max_value=1079.10, value=77.00, step=0.1)
GGT = st.slider(label='Gamma-Glutamyl Transferase', min_value=4.50, max_value=650.90, value=23.00, step=0.1)
PROT = st.slider(label='Proteins', min_value=44.80, max_value=90.00, value=72.00, step=0.1)

# convert into dataframe
data = pd.DataFrame({'Age': [Age],
                'Sex': [Sex],
                'ALB': [ALB],
                'ALP':[ALP],
                'ALT': [ALT],
                'AST': [AST],
                'BIL': [BIL],
                'CHE': [CHE],
                'CHOL': [CHOL],
                'CREA': [CREA],
                'GGT': [GGT],
                'PROT': [PROT]
                })

st.write(data)

# model predict
Category = model.predict(data).tolist()[0]


# interpretation
st.write('Classification Result: ')

if Category == 0:
    st.text('Blood Donor')
else:
    st.text('Hepatitis C')