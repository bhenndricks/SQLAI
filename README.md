# SQLAI

# Oracle Query Generator Documentation

## Introduction

Oracle Query Generator is a Streamlit-based application designed to facilitate natural language querying on the Netflix dataset. It utilizes advanced natural language processing techniques to translate user queries into SQL, executes them on an Oracle database, and presents the results in a user-friendly manner.

## Overview

The application combines the power of OpenAI's GPT-3.5 model and Oracle database technology to provide an innovative solution for querying databases using natural language. It is particularly useful for users who may not be familiar with SQL but need to extract information from a database.

## Key Features

- **Natural Language Query Processing**: Leverages GPT-3.5 to interpret and translate natural language queries.
- **Oracle Database Integration**: Seamlessly executes the generated SQL queries on an Oracle database.
- **Streamlit Web Interface**: Offers an interactive platform for query input and result visualization.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Streamlit
- cx_Oracle
- Access to an Oracle Database
- OpenAI API Key

### Installation Instructions

1. **Clone the repository**:
   
   Clone the Oracle Query Generator repository to your local machine.

2. **Install Dependencies**:

   Use pip to install the necessary Python packages:

   ```bash
   pip install streamlit cx_Oracle openai python-dotenv
    ```

### Environment Setup:

1. Create a .env file in the root directory of the project and populate it with your Oracle credentials and OpenAI API key:


```
ORACLE_USERNAME=your_oracle_username
ORACLE_PASSWORD=your_oracle_password
ORACLE_DSN=your_oracle_dsn
OPENAI_API_KEY=your_openai_api_key
```

### Running the Application
1. Activate your Python environment.

2. Start the Streamlit application:

```
streamlit run app.py

```
A local URL will be generated, which can be accessed through a web browser.

### How to Use

1. Input Query:

Enter your natural language query regarding the Netflix dataset in the provided text input area.

2. Submit Query:

Click the "Submit" button to process your query.

3. View Results:

The application will display the translated SQL query and its execution results.

Contribution
Contributions are welcomed to enhance the functionality and efficiency of the Oracle Query Generator. Please adhere to the standard workflow of forking, cloning, creating feature branches, committing changes, and submitting pull requests.

## License
This project is released under the MIT License. More details can be found in the LICENSE file.

## Acknowledgments
This project makes use of Oracle Database technologies.
It integrates OpenAI's GPT-3.5 model for NLP capabilities.
The Streamlit community for providing an excellent platform for building interactive web applications.