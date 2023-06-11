import streamlit as st
import pandas as pd
import emoji

def load_data():
    manufacturers = pd.DataFrame({
        'Name': ['Gar Labs', 'Lily\'s', 'Beauty Private Label', 'Federal Packaging', 'Twincraft', 
                 'Coughlin Companies', 'Sinoscan', 'KKT', 'Goodkind Co'],
        'MOQ': [5000, 10000, 3000, 5000, 15000, 5000, 10000, 5000, 10000],
        'Time': [14, 16, 12, 15, 20, 14, 16, 15, 17],
        'Price_per_unit': [2.00, 5.50, 4.50, 5.00, 2.50, 4.50, 3.50, 5.00, 3.00],
        'Email': ['tom@garlabs.com', 'hello@moesgroup.org', 'Sales@bqgmanufacturing.com', 'info@federalpackage.com', 
                  'jackson.berman@twincraft.com', 'info@contactcoghlin.com', 'info@sinoscan.com', 'krupa@kktconsultants.com', 
                  'info@nutracapusa.com']
    })
    return manufacturers

def home_page():
    st.title(emoji.emojize('Welcome to CPG Brand - Manufacturer Matching App :factory:'))
    st.write('This app helps CPG brands find the perfect contract manufacturer.')
    if st.button('Let\'s go!'):
        st.session_state.page += 1

def input_company_info():
    st.title(emoji.emojize('Enter Your Company Information :memo:'))
    # added placeholders
    company_name = st.text_input('Company Name', 'Enter Company Name')
    product_type = st.text_input('Product Type', 'Enter Product Type')
    segment = st.text_input('Segment', 'Enter Segment')
    annual_units = st.number_input('Annual Units', 0)
    website_url = st.text_input('Website URL', 'http://')
    revenue_last_year = st.number_input('Revenue in the last 12 months ($)', 0)
    price_per_unit = st.number_input('Price Per Unit ($)', 0)
    projected_revenue = st.number_input('Projected Revenue for the next 12 months ($)', 0)
    ideal_monthly_units = st.number_input('Ideal Monthly Units', 0)
    differentiation = st.text_input('Company Differentiation', 'What sets your company apart?')
    monthly_revenue = st.number_input('Average Monthly Revenue ($)', 0)
    monthly_expense = st.number_input('Average Monthly Expense ($)', 0)
    if st.button('Submit'):
        st.success(emoji.emojize('Company Info Saved Successfully! :white_check_mark:'))
        st.session_state.page += 1

def choose_criteria():
    st.title(emoji.emojize('Choose Your Main Criteria for Manufacturer Selection :mag:'))
    criteria = st.selectbox('Choose your main criteria', ['MOQ', 'Time', 'Price_per_unit'])
    st.session_state.criteria = criteria
    if st.button('Let\'s see the matches!'):
        st.session_state.page += 1

def best_match():
    st.title('Your Best Manufacturer Matches')
    manufacturers = load_data()
    criteria = st.session_state.criteria  # Get the selected criteria from the session state
    # Sort the manufacturers based on the selected criteria
    sorted_manufacturers = manufacturers.sort_values(by=criteria, ascending=True)

    # Fetch top 3 manufacturers
    for i in range(3):
        manufacturer = sorted_manufacturers.iloc[i]
        st.subheader(f'{i+1}. {manufacturer["Name"]}')
        st.write(f"This manufacturer is one of the top choices based on the {criteria} criteria. "
                  f"It has {manufacturer[criteria]} {criteria}. You can contact them at {manufacturer['Email']}.")

    st.write('These manufacturers have been chosen based on the lowest values of your selected criteria, '
             'which could translate into lower production costs and faster delivery times for your CPG brand.')

    if st.button('Next'):
        st.session_state.page += 1

def manufacturers_list():
    st.title('Manufacturers List')
    manufacturers = load_data()
    st.write(manufacturers)
    if st.button('Back to Home'):
        st.session_state.page = 0

PAGES = [home_page, input_company_info, choose_criteria, best_match, manufacturers_list]

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 0
    PAGES[st.session_state.page]()

if __name__ == "__main__":
    main()







