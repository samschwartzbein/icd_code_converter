import streamlit as st
import pydantic
from pydantic import BaseModel
print(pydantic.__version__)
import streamlit_pydantic as sp
from ICD_code_converter import *

class ExampleModel(BaseModel):
    Enter_Your_Codes: str

def main():
    """ICD Converter App"""
    st.title("Medical Code to SAS Converter")
    st.markdown("###### This application transforms medical codes (ICD9, ICD10, CPT, HSPS, GPI) into a SAS readable format")
    data = sp.pydantic_form(key="my_form", model=ExampleModel)

    if data:
        userInput = data.Enter_Your_Codes
        cleaned = clean_codes(userInput)
        final = print_codes(cleaned)
        st.code(final)
    pass

main()
