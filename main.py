import streamlit as st
from PIL import Image

# Title Web Page
st.set_page_config (page_title= "Aksata", page_icon=":rose:", layout="wide"  )


#Header Section 
st.markdown("<h4 style='text-align: center; color: white;'> To Dear Calla, My Lovely Friend </h4>", unsafe_allow_html=True)

#Text Section
st.markdown("<h6 style='text-align: center; color: white;'> This Some Off Kinda Website That I Made For You</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: white;'> And This Is The Way That I Want To Tell You Something</h5>", unsafe_allow_html=True)
st.divider()

# A Looooong Text 
if st.button ('!'):

    # First Photo
    st.markdown ("<h6 style='text-align: center; color: white;'> after all the things we do together......</h5>", unsafe_allow_html=True)
    image = Image.open ('First Photo.jpeg')
    col1, col2, col3 = st.columns([4 ,4, 4])
    col2.image(image, caption=' The First Photo We Took',width=400,)

    # Second Photo
    st.markdown ("<h6 style='text-align: center; color: white;'> day by day had passed, month by month...</h5>", unsafe_allow_html=True)
    image = Image.open ('Project.jpeg')
    col1, col2, col3 = st.columns([4 ,4, 4])
    col2.image(image, caption='We Together In Project ',width=400,)

    # Third Photo
    st.markdown ("<h6 style='text-align: center; color: white;'> and until our both birthday....</h5>", unsafe_allow_html=True)
    image = Image.open ('Our Birthday.jpeg')
    col1, col2, col3 = st.columns([4 ,4, 4])
    col2.image(image, caption='Our Birthday',width=400,)


    # The Text
    st.markdown("<h6 style='text-align: center; color: white;'> i do like you cal, just wanted you to know.</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: white;'> im not asking you to be my girlfriend but if you want to.... would you? </h5>", unsafe_allow_html=True)

