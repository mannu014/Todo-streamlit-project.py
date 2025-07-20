import streamlit as st

from auth_db import csr, conn


st.title("Sign Up Here")

col1, col2 = st.columns(2)

#these are new changes

with col1:
    username = st.text_input("Enter Your Username...")

with col2 :
    full_name = st.text_input("Enter Your Full Name")

phone = st.number_input("Enter Your Phone Number", min_value= 0000000000)

email = st.text_input("Enter Your Email Address")

password = st.text_input("Enter Your passsword", type ="password")

conform_password = st.text_input("Confirm Password", type = "password")

btn = st.button("Sign Up")

if btn:
    if username == "" or full_name == "" or phone == "" or email == "" or password == ""  or conform_password == "" :
        st.error("Please Fill Up All Fields")
        st.snow()
    else:
        if password != conform_password:
            st.warning("Confirm Password do not match")
            st.snow()
        else:
            try:
                csr.execute(f"insert into signup_user(username, full_name, phone_number, email, passwordd) values('{username}', '{full_name}','{phone}','{email}','{password}')")
                conn.commit()

                st.success("Sign Up Successfully")
                st.balloons()

                st.markdown("[Go to login page](./login)")
            except Exception as e:
                st.error("please check username must be unique")
           


                               





