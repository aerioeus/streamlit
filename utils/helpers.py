"""
Helper functions for the multipage app
"""
import streamlit as st

def create_metric_cards(metrics_data):
    """Create a row of metric cards"""
    if not metrics_data:
        return

    cols = st.columns(len(metrics_data))

    for i, (label, value, delta) in enumerate(metrics_data):
        with cols[i]:
            st.metric(label, value, delta)

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

def format_percentage(value):
    """Format number as percentage"""
    return f"{value:.2%}"

def show_dataframe_info(df, title="Dataset Info"):
    """Display information about a dataframe"""
    st.subheader(title)

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Rows:** {len(df)}")
        st.write(f"**Columns:** {len(df.columns)}")

    with col2:
        st.write(f"**Memory Usage:** {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
        st.write(f"**Data Types:** {df.dtypes.value_counts().to_dict()}")