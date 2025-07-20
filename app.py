import streamlit as st
from auth_db import csr, conn
import pandas as pd



st.header("My Todo App")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.authenticated:
    st.subheader(f"Add Todo ({st.session_state.username})")

    todo_tittle = st.text_input("Enter Todo Title")

    desc = st.text_area("Breaf about Todo :")

    adddin = st.button("Add Todo")

    if adddin:
        if todo_tittle == "" or desc =="":
            st.warning("Please fill up all fields")
        else:
            csr.execute(f"insert into mytodos(todo_added_by,todo_title, todo_desc) values ('{st.session_state.username}','{todo_tittle}','{desc}')")
            conn.commit()

            st.success("Todo Added Succesfully..!")
            st.balloons()

    st.subheader("My All Todos")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.subheader("Todo ID")
    with col2:
        st.subheader("Todo tittle")
    with col3:
        st.subheader("Discription")
    with col4:
        st.subheader("Delete Todos")
    
    

    csr.execute(f"select * from mytodos where todo_added_by ='{st.session_state.username}';")

    all_todos = csr.fetchall()

    for id, added, title, dec, done in all_todos:
        todo_id, til, desc, dlt = st.columns(4)

        with todo_id:
            checked = st.checkbox("Done", key = {id}, value = bool(done))

            if checked != bool(done):
                csr.execute(f"update mytodos set todo_done = {checked} where todo_id = {id}")
        with til:
            st.write(f"{title}")
        with desc:
            st.write(f"{dec}")
        with dlt:
            x = st.button(" ❌ Delete", key = f"{id}")

            if x:
                csr.execute(f"delete from mytodos where todo_id = '{id}';")
                conn.commit()
                st.snow()
                st.rerun()

        st.write("--------------------------------------------------")


    



else:
    st.warning("Please login first..")

    st.markdown("[Go to Login Page](./login)")
