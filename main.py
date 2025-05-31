import streamlit as st
import helper
 
st.set_page_config(page_title="Shoe Recommender", page_icon="👟")
st.title("👟 Occasion-Based Shoe Recommender")
 
# Sidebar for occasion
occasion = st.sidebar.selectbox("Pick an Occasion", [
    "Wedding", "Workout", "Casual Outing", "Office", "Party", "Beach Day"
])
 
if occasion:
    response = helper.suggest_shoes(occasion)
    st.subheader("Shoe Brand Name")
    st.success(response['brand'].strip())
 
    st.subheader("Recommended Shoes")
    shoes = [s.strip() for s in response["shoes"].split(",") if s.strip()]
    for shoe in shoes:
        st.markdown(f"- {shoe}")
 