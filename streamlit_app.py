# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import math

# Set page configuration
st.set_page_config(
    page_title="Multi-Page Demo",
    page_icon="🚀",
    layout="wide"
)

# Define page functions
def home_page():
    st.title("energicos Metering Analysis")

    st.markdown("""
    ## About This App

    This is a quick energicos Metering Data Analysis App.
    Each page is completely independent and stateless.

    """)

    # Show some basic metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Pages", "4")

    with col2:
        st.metric("Navigation Method", "st.Page")

    with col3:
        st.metric("Session States", "0")

    with col4:
        st.metric("Complexity", "Low")

    st.info("👈 Use the sidebar to navigate between pages!")

def analytics_page():
    st.title(" Analytics Dashboard")

    st.markdown("This page demonstrates various data visualizations without maintaining any state.")

    # Generate fresh data each time (no state needed)
    @st.cache_data
    def generate_sample_data():
        dates = pd.date_range('2024-01-01', periods=100, freq='D')
        data = {
            'date': dates,
            'sales': np.random.normal(1000, 200, 100).cumsum(),
            'visitors': np.random.randint(50, 200, 100),
            'conversion_rate': np.random.uniform(0.02, 0.08, 100)
        }
        return pd.DataFrame(data)

    # Chart selection (fresh each time, no state persistence)
    chart_type = st.selectbox(
        "Select Chart Type:",
        ["Line Chart", "Bar Chart", "Scatter Plot", "Area Chart"]
    )

    data = generate_sample_data()

    if chart_type == "Line Chart":
        fig = px.line(data, x='date', y='sales', title='Sales Over Time')
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Bar Chart":
        # Create proper weekly aggregation
        data_with_week = data.copy()
        data_with_week['week'] = data_with_week['date'].dt.isocalendar().week
        data_with_week['year_week'] = data_with_week['date'].dt.strftime('%Y-W%U')
        weekly_data = data_with_week.groupby('year_week')['visitors'].sum().reset_index()

        fig = px.bar(weekly_data, x='year_week', y='visitors', title='Weekly Visitors')
        fig.update_xaxes(title='Week', tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Scatter Plot":
        fig = px.scatter(data, x='visitors', y='sales',
                        title='Sales vs Visitors Correlation')
        st.plotly_chart(fig, use_container_width=True)

    else:  # Area Chart
        fig = px.area(data, x='date', y='conversion_rate',
                     title='Conversion Rate Over Time')
        st.plotly_chart(fig, use_container_width=True)

    # Show summary statistics
    st.subheader("Summary Statistics")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Average Daily Sales", f"${data['sales'].mean():.2f}")
        st.metric("Total Visitors", f"{data['visitors'].sum():,}")

    with col2:
        st.metric("Average Conversion Rate", f"{data['conversion_rate'].mean():.2%}")
        st.metric("Peak Sales Day", f"${data['sales'].max():.2f}")

def data_page():
    st.title("Data Viewer")

    st.markdown("View and filter sample datasets. All filters reset when you navigate away.")

    # Data generation (fresh each time)
    @st.cache_data
    def load_sample_datasets():
        # Create sample employee data
        employees = pd.DataFrame({
            'Name': [f'Employee {i}' for i in range(1, 101)],
            'Department': np.random.choice(['IT', 'Sales', 'Marketing', 'HR', 'Finance'], 100),
            'Salary': np.random.randint(40000, 120000, 100),
            'Experience': np.random.randint(1, 20, 100),
            'Performance': np.random.choice(['Excellent', 'Good', 'Average', 'Needs Improvement'], 100)
        })

        # Create sample product data
        products = pd.DataFrame({
            'Product': [f'Product {i}' for i in range(1, 51)],
            'Category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home'], 50),
            'Price': np.random.uniform(10, 500, 50).round(2),
            'Stock': np.random.randint(0, 100, 50),
            'Rating': np.random.uniform(1, 5, 50).round(1)
        })

        return employees, products

    employees_df, products_df = load_sample_datasets()

    # Dataset selection
    dataset = st.selectbox("Choose Dataset:", ["Employees", "Products"])

    if dataset == "Employees":
        st.subheader("Employee Data")

        # Simple filters (no state persistence)
        col1, col2 = st.columns(2)
        with col1:
            dept_filter = st.multiselect(
                "Filter by Department:",
                employees_df['Department'].unique(),
                default=employees_df['Department'].unique()
            )
        with col2:
            min_salary = st.number_input("Minimum Salary:",
                                       min_value=0,
                                       max_value=200000,
                                       value=40000)

        # Apply filters
        filtered_df = employees_df[
            (employees_df['Department'].isin(dept_filter)) &
            (employees_df['Salary'] >= min_salary)
        ]

        st.dataframe(filtered_df, use_container_width=True)
        st.write(f"Showing {len(filtered_df)} out of {len(employees_df)} employees")

    else:  # Products
        st.subheader("Product Data")

        # Simple filters
        col1, col2 = st.columns(2)
        with col1:
            category_filter = st.multiselect(
                "Filter by Category:",
                products_df['Category'].unique(),
                default=products_df['Category'].unique()
            )
        with col2:
            max_price = st.slider("Maximum Price:",
                                min_value=0,
                                max_value=500,
                                value=500)

        # Apply filters
        filtered_df = products_df[
            (products_df['Category'].isin(category_filter)) &
            (products_df['Price'] <= max_price)
        ]

        st.dataframe(filtered_df, use_container_width=True)
        st.write(f"Showing {len(filtered_df)} out of {len(products_df)} products")

def calculator_page():
    st.title("🧮 Simple Calculator")

    st.markdown("Perform basic mathematical operations. No history is saved between visits.")

    # Calculator type selection
    calc_type = st.radio("Calculator Type:", ["Basic", "Scientific"])

    if calc_type == "Basic":
        st.subheader("Basic Calculator")

        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("First Number:", value=0.0)
        with col2:
            num2 = st.number_input("Second Number:", value=0.0)

        operation = st.selectbox("Operation:", ["+", "-", "×", "÷"])

        if st.button("Calculate"):
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "×":
                result = num1 * num2
            elif operation == "÷":
                if num2 != 0:
                    result = num1 / num2
                else:
                    st.error("Cannot divide by zero!")
                    result = None

            if result is not None: # type: ignore
                st.success(f"Result: {num1} {operation} {num2} = {result}") # type: ignore

    else:  # Scientific
        st.subheader("Scientific Calculator")

        number = st.number_input("Enter Number:", value=0.0)

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Square Root"):
                if number >= 0:
                    result = math.sqrt(number)
                    st.success(f"√{number} = {result}")
                else:
                    st.error("Cannot calculate square root of negative number!")

            if st.button("Square"):
                result = number ** 2
                st.success(f"{number}² = {result}")

        with col2:
            if st.button("Sine"):
                result = math.sin(math.radians(number))
                st.success(f"sin({number}°) = {result:.6f}")

            if st.button("Cosine"):
                result = math.cos(math.radians(number))
                st.success(f"cos({number}°) = {result:.6f}")

        with col3:
            if st.button("Natural Log"):
                if number > 0:
                    result = math.log(number)
                    st.success(f"ln({number}) = {result:.6f}")
                else:
                    st.error("Cannot calculate log of non-positive number!")

            if st.button("Exponential"):
                result = math.exp(number)
                st.success(f"e^{number} = {result:.6f}")

    st.markdown("---")
    st.info("💡 Tip: All calculations are performed fresh each time. No history is maintained.")

# Define pages using functions instead of files
home_page_obj = st.Page(home_page, title="Home", icon="🏠")
analytics_page_obj = st.Page(analytics_page, title="Analytics", icon="📊")
data_page_obj = st.Page(data_page, title="Data View", icon="📋")
calculator_page_obj = st.Page(calculator_page, title="Calculator", icon="🧮")

# Create navigation
pg = st.navigation([
    home_page_obj,
    analytics_page_obj,
    data_page_obj,
    calculator_page_obj
])

# Run the selected page
pg.run()