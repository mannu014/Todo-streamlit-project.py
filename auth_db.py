import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "manu",
    database = "streamlit_project"
)

csr = conn.cursor()