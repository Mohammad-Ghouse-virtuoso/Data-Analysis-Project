import streamlit as st
import os
import textwrap
import google.generativeai as genai
import mysql.connector
st.markdown("""
<style>
.css-1rs6os.edgvbvh3
{
    visibilty:hidden;
}         
.css-1lsmgbg.egzxvld0
{
    visibility:hidden; 
}
</style>
            
""",unsafe_allow_html=True)
# Configure GenAI Key (replace with your actual API key)
genai.configure(api_key="") #add your key here

#connect with workbench:
def connect_to_database():
    return mysql.connector.connect(
        user="root", 
        password="johndoe", 
        host="localhost",  
        database="spidata",
        auth_plugin="mysql_native_password"
    )
def dis(sql_query):
    conn = connect_to_database()
    cursor = conn.cursor()
    result = cursor.execute(sql_query)  # Use cursor.execute() for query execution
    result = cursor.fetchall()
    if isinstance(result, list) and result:
        # Display the result in table format
        columns = [desc[0] for desc in cursor.description]
        st.table([columns] + result)
    elif isinstance(result, str):
        # Display non-SELECT query execution message
        st.write(result)
    else:
        st.warning("No records found.")

    conn.close()


# Function to get response using GenAI's Gemini model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to execute SQL query using the database connection (not shown in this example)

prompt = ["""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name spidata and consists of the following table- spi
    The structure of each table is as follows:
    Columns:
spi_rank int 
country text 
spi_score double 
basic_human_needs double 
wellbeing double 
opportunity double 
basic_nutri_med_care double 
water_sanitation double 
shelter double 
personal_safety double 
access_basic_knowledge double 
access_info_comm double 
health_wellness double 
env_quality double 
personal_rights double 
personal_freedom_choice double 
inclusiveness double 
access_adv_edu double    
          
          For example,
    - what are the top five countries based on ranking
      The SQL command will be something like this: SELECT country,spi_rank FROM spi where spi_rank<6;

    - List five countries having the lowest spi score
      The SQL command will be something like this: SELECT country FROM spi ORDER BY spi_score ASC LIMIT 5;
          
    - top one and bottom one country based on spi rank
      The SQL command will be something like this: SELECT country, spi_rank FROM spi ORDER BY spi_rank ASC LIMIT 1 UNION SELECT country, spi_rank FROM spi ORDER BY spi_rank DESC LIMIT 1;
    
    - Find the top 5 countries with the highest wellbeing score
      The SQL command will be something like this: SELECT country, wellbeing FROM spi ORDER BY wellbeing DESC LIMIT 5;

          
    Remember, the SQL code should not have ``` in the beginning or end, and the output should not contain the word 'sql'.
    generate only sql query...

          """]
st.header("Generative analysis..!")
st.title('''
Examples: 
         1.Find average opportunity score
    2.Find the top 5 countries with the highest wellbeing score
''')
question = st.text_input("Enter an English question: ")
if question:
    result = get_gemini_response(question, prompt)
    st.success(f"Generated SQL Query: {result}")
    dis(f"{result}")
