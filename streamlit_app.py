import streamlit as st
from pydantic import BaseModel
import streamlit_pydantic as sp

from ICD_code_converter import *

class ExampleModel(BaseModel):
    Enter_Your_Codes: str
    #some_boolean: bool

# Enter Functions Here

def main():
    """ICD Converter App"""
    st.title("ICD Code to SAS Converter")
    st.markdown("###### This application will transform ICD codes into a SAS readable format")
    data = sp.pydantic_form(key="my_form", model=ExampleModel)

    if data:
        userInput = data.Enter_Your_Codes
        cleaned = clean_codes(userInput)
        st.code(print_codes(cleaned))
    pass


main()
