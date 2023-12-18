# Import necessary libraries and modules
import streamlit as st
from dotenv import load_dotenv 
import json 
import json 
import os
from dotenv import load_dotenv
import openai
import logging
import os 
import cx_Oracle


table_metadata = """
    Table name: NETFLIX_DATA


"COLUMN_NAME"	"DATA_TYPE"	"NULLABLE"	"DATA_DEFAULT"
"SHOW_ID"	"VARCHAR2"	"Y"	""
"TYPE"	"VARCHAR2"	"Y"	""
"TITLE"	"VARCHAR2"	"Y"	""
"DIRECTOR"	"VARCHAR2"	"Y"	""
"CAST"	"VARCHAR2"	"Y"	""
"COUNTRY"	"VARCHAR2"	"Y"	""
"DATE_ADDED"	"VARCHAR2"	"Y"	""
"RELEASE_YEAR"	"NUMBER"	"Y"	""
"RATING"	"VARCHAR2"	"Y"	""
"DURATION"	"VARCHAR2"	"Y"	""
"LISTED_IN"	"VARCHAR2"	"Y"	""
"DESCRIPTION"	"VARCHAR2"	"Y"	""

"""



# Set the path to the Instant Client
os.environ["PATH"] = "C:\\Users\\Blake Hendricks\\Downloads\\instantclient-basic-windows.x64-21.12.0.0.0dbru\\instantclient_21_12" + ";" + os.environ["PATH"]
os.environ["ORACLE_HOME"] = "C:\\Users\\Blake Hendricks\\Downloads\\instantclient-basic-windows.x64-21.12.0.0.0dbru\\instantclient_21_12"


openai.api_key = "sk-"

# Load environment variables for Oracle database connection
load_dotenv()
oracle_username = os.getenv("ORACLE_USERNAME")
oracle_password = os.getenv("ORACLE_PASSWORD")
oracle_dsn = os.getenv("ORACLE_DSN")

# Oracle Database Connection Function
def create_db_connection():
    return cx_Oracle.connect(oracle_username, oracle_password, oracle_dsn)

# Function to execute SQL query on Oracle Database
def sql_query(target_query):
    conn = create_db_connection()
    cur = conn.cursor()
    
    # Execute a query
    cur.execute(target_query)

    answer = []
    # Fetch the result
    for row in cur:

        answer.append(row[0])

    # Close the cursor and the connection
    cur.close()
    conn.close()

    # Convert answer to string
    answer_text = '\n'.join(answer)
    return answer_text

# Function to run conversation with GPT
def run_conversation(query):
    # Prepare the context for GPT
    prompt = f"""
    Here is the context for how the tables are structured:

    {table_metadata}

    Now please convert the query below into working SQL and execute it:

    {query}
    """
    
    messages = [{"role": "user", "content": prompt}]
    functions = [
        {
            "name": "sql_query",
            "description": "Execute the given SQL query and return the results",
            "parameters": {
                "type": "object",
                "properties": {
                    "target_query": {
                        "type": "string",
                        "description": "The SQL query to execute",
                    }
                },
                "required": ["target_query"],
            },
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto"
    )
    response_message = response["choices"][0]["message"]



    # Process the function call if required
    if response_message.get("function_call"):
        available_functions = {"sql_query": sql_query}
        function_name = response_message["function_call"]["name"]
        function_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = function_to_call(target_query=function_args.get("target_query"))

        messages.append(response_message)
        messages.append({
            "role": "function",
            "name": function_name,
            "content": function_response,
        })
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )
        return second_response["choices"][0]["message"]["content"]


# Streamlit app
def main():
    st.set_page_config(page_title="Oracle Query Generator", page_icon=":bird:")
    st.header("Oracle Query Generator :bird:")
    
    user_query = st.text_input("Please enter your question about the Netflix Data Set", placeholder="Type your question here...")

    if st.button("Submit"):
        if user_query:
            try:
                st.write("Translating and executing your query...")
                result = run_conversation(user_query)
                st.success("Result:\n" + result)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please enter your question about the Netflix Data Set")

if __name__ == '__main__':
    main() 


