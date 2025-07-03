# Multipage Streamlit App

A demonstration of building multipage Streamlit applications without session states using the modern `st.Page` and `st.navigation` approach.

## Features

- 🏠 Home page with app overview
- 📊 Analytics dashboard with interactive charts
- 📋 Data viewer with filtering capabilities
- 🧮 Calculator with basic and scientific functions

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd multipage-streamlit-app
   ```


2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

## Project Structure

* `streamlit_app.py` - Main entrypoint and navigation setup
* `pages/` - Individual page implementations
* `utils/` - Helper functions and data generators
* `config/` - Application configuration
* `assets/` - Static files and sample data

## Architecture

This app demonstrates:

* Stateless page design
* Modern Streamlit navigation
* Clean separation of concerns
* Reusable utility functions
* Performance optimization with caching

Install dependencies:
bashpip install -r requirements.txt

Run the application:
bashstreamlit run streamlit_app.py


Project Structure

streamlit_app.py - Main entrypoint and navigation setup
pages/ - Individual page implementations
utils/ - Helper functions and data generators
config/ - Application configuration
assets/ - Static files and sample data

Architecture
This app demonstrates:

Stateless page design
Modern Streamlit navigation
Clean separation of concerns
Reusable utility functions
Performance optimization with caching


#### `requirements.txt`
```txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.15.0