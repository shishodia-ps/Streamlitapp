import pandas as pd
import streamlit as st
import openpyxl

st.title("Forensic Audit")

myselectbox=st.sidebar.selectbox('Select team',['Audit','Data Analytics','Forensic','Compliance'])
st.markdown('Before we get started with the analysis, lets have a quick look at the raw data :sunglasses:')

name=st.text_input('Please enter your name:')


if name:
    st.write(f'Hello {name}') 
    st.divider()
    st.write("Please Enter your data")
    uploaded_file=st.file_uploader('Upload a file:',type=['.txt','.csv','.xlsx'])
    if uploaded_file:
        if uploaded_file.type=='text/plain':
            from io import StringIO
            stringio=StringIO(uploaded_file.getvalue().decode('utf-8'))
            string_data=stringio.read()
            st.write(string_data)
        elif uploaded_file.type=='text/csv':
            import pandas as pd
            df=pd.read_csv(uploaded_file)
            st.write(df)
        else:
            import pandas as pd
            df=pd.read_excel(uploaded_file)
            st.write(df)
    if uploaded_file:
        st.write("what do you want to do with this data"+':smile:'*3)