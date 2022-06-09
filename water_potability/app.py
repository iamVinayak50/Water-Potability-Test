import pandas as pd
import numpy as np
import pickle
import streamlit as st

from PIL import Image

# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)


def welcome():
    return 'welcome all'

st.markdown("![Alt Text](https://acegif.com/wp-content/gifs/water-43.gif)")
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.pexels.com/photos/4194850/pexels-photo-4194850.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity):
    prediction = classifier.predict([[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Water Potability")


    st.markdown('**Prediciting the Water Potability with following features that water is potable for drinking purpose or not. If water potability Output is 1 then water potable for drinking purpose whereas If Output is 0 then Water is Non- Potable.**') 
    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Water Quality ML App </h1>
    </div>
        """
    
    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    ph = st.slider("Ph",min_value=0.00,max_value=14.00)
    Hardness = st.number_input("Hardness", min_value=47.00,max_value=325.00)
    Solids = st.number_input("Solids", min_value=320.00,max_value=61230.00)
    Chloramines = st.number_input("Chloramines", min_value=0.30,max_value=13.20)
    Sulfate = st.number_input("Sulfate", min_value=129.00,max_value=480.00)
    Conductivity = st.number_input("Conductivity", min_value=181.00,max_value=755.00)
    Organic_carbon = st.number_input("Organic_carbon",min_value=2.00,max_value=30.00)
    Trihalomethanes = st.number_input("Trihalomethanes",min_value=0.00,max_value=124.00)
    Turbidity = st.number_input("Turbidity",min_value=1.00,max_value=7.00)
    result =""
    
 
    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity)
        if (result==0):
            st.write("Non-Potablity")
        else:
            st.write("Potabilty")
    st.success('The output is {}'.format(result))
  
    st.snow()
    
if __name__=='__main__':
    main()
