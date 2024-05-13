# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Example Streamlit App :balloon:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)


import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"))

st.write("You selected:", option)


if ingredients_list:
    
    ingredients_string = ''
    for fruit_chosen in ingredients_list;
      ingredients_string +=fruit_chosen
    st.write(ingredients_string)


my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

st.write(my_insert_stmt)

   if ingredients_string:
        session.sql(my_insert_stmt).collect()
	st.success('Your Smoothie is ordered!', icon="✅")
