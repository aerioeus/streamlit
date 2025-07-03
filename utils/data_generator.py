"""
Data generation utilities for the multipage app
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit as st
from config.settings import *

@st.cache_data
def generate_employee_data(size=SAMPLE_SIZE_EMPLOYEES):
    """Generate sample employee dataset"""
    return pd.DataFrame({
        'Name': [f'Employee {i}' for i in range(1, size + 1)],
        'Department': np.random.choice(DEPARTMENTS, size),
        'Salary': np.random.randint(40000, 120000, size),
        'Experience': np.random.randint(1, 20, size),
        'Performance': np.random.choice(['Excellent', 'Good', 'Average', 'Needs Improvement'], size)
    })

@st.cache_data
def generate_product_data(size=SAMPLE_SIZE_PRODUCTS):
    """Generate sample product dataset"""
    return pd.DataFrame({
        'Product': [f'Product {i}' for i in range(1, size + 1)],
        'Category': np.random.choice(PRODUCT_CATEGORIES, size),
        'Price': np.random.uniform(10, 500, size).round(2),
        'Stock': np.random.randint(0, 100, size),
        'Rating': np.random.uniform(1, 5, size).round(1)
    })

@st.cache_data
def generate_analytics_data(days=DATE_RANGE_DAYS):
    """Generate sample analytics time series data"""
    dates = pd.date_range(
        start=datetime.now() - timedelta(days=days),
        periods=days,
        freq='D'
    )
    
    return pd.DataFrame({
        'date': dates,
        'sales': np.random.normal(1000, 200, days).cumsum(),
        'visitors': np.random.randint(50, 200, days),
        'conversion_rate': np.random.uniform(0.02, 0.08, days)
    })