import numpy as np
import sklearn 
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

scalar = StandardScaler()

def Card_Detection(input_data):
    inp_data = np.asarray(input_data, dtype=float)
    inp_datas = inp_data.reshape(1,-1)
    prediction = loaded_model.predict(inp_datas)

    if (prediction == 0):
        return 'Legit'
    elif (prediction == 1):
        return 'Fraud Transaction'
    
def main():
    st.title('CREDIT CARD TRANSACTION DETECTION')
    left, right = st.columns([1,1])
    with left:
        V1 = st.text_input('V1')
        V5 = st.text_input('V5')
        V8 = st.text_input('V8')
        V14 = st.text_input('V14')
        V18 = st.text_input('V18')
    with right:
        V4 = st.text_input('V4')
        V6 = st.text_input('V6')
        V10 = st.text_input('V10')
        V15 = st.text_input('V15')
        V20 = st.text_input('V20')

    detection = ''

    if st.button('Check Result'):
        detection = Card_Detection([V1,V4,V5,V6,V8,V10,V14,V15,V18,V20])

    st.success(detection)

if __name__ == '__main__':
    main()

