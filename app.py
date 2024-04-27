"This is a Testmodul"

import boto3
from botocore.exceptions import NoCredentialsError
import streamlit as st

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='your-region')

def main():
    st.sidebar.title('Navigation')
    if st.sidebar.button('Home'):
        st.session_state.page = 'Home'
    if st.sidebar.button('Page 1'):
        st.session_state.page = 'Page 1'
    if st.sidebar.button('Page 2'):
        st.session_state.page = 'Page 2'
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'
    
    if st.session_state.page == 'Home':
        display_home()
    elif st.session_state.page == 'Page 1':
        display_page1()
    elif st.session_state.page == 'Page 2':
        display_page2()

def display_home():
    st.title('Home Page')
    st.write('Welcome to the Home Page!')

def display_page1():
    st.title('Page 1')
    # Fetch data from DynamoDB
    try:
        table = dynamodb.Table('YourTableName')
        response = table.scan()  # or use query() based on your use case
        data = response['Items']
        if data:
            st.write(data)  # Display the data in a raw format or process as needed
        else:
            st.write("No data found in DynamoDB.")
    except NoCredentialsError:
        st.error("AWS credentials not found.")
    except Exception as e:
        st.error(f"Failed to fetch data from DynamoDB: {e}")

def display_page2():
    st.title('Page 2')
    st.write('Welcome to Page 2!')

if __name__ == "__main__":
    main()

