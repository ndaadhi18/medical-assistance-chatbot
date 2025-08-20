import streamlit as st
from utils.api import upload_pdfs_api

def render_uploader():
    st.header("Upload Medical documents (.PDFs)")
    uploaded_files=st.file_uploader("Upload multiple PDFs",type="pdf",accept_multiple_files=True)
    if st.button("Upload DB") and uploaded_files:
        response=upload_pdfs_api(uploaded_files)
        if response.status_code==200:
            st.success("Uploaded successfully")
        else:
            st.error(f"Error:{response.text}")