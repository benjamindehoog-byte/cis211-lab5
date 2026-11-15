# CIS 211 Lab 5 - Bright Bakery Interactive Order Calculator
# Complete the TODO sections using the Lab 5 instructions.
# Add at least THREE explanatory comments of your own.

import streamlit as st

# Supplied data: keep these products, prices and sample counts unchanged.
menu = {
    "cupcake": 3.75,
    "cookie": 2.00,
    "muffin": 2.75,
    "scone": 3.25,
    "brownie": 3.00,
}

sample_sales = {
    "Product": ["cupcake", "cookie", "muffin", "scone", "brownie"],
    "Units sold": [18, 30, 12, 10, 15],
}


def apply_discount(subtotal):
     """Return the remaining item subtotal after any eligible discount."""
    if subtotal >=50:
        return round(subtotal * 0.9, 2)
    else:
        return subtotal

def shipping_fee(subtotal):
      """Return the Delivery fee, using the ORIGINAL item subtotal."""
    if subtotal >= 35:
        return 0.0
    else:
        return 5.99
  
st.title("Bright Bakery Interactive Order Calculator")
st.caption("A class practice app that calculates a quote.")
st.info("Starter file loaded. Complete the TODO sections before submitting.")

# TODO 3 - Step 5: Put the required controls in a sidebar.
# Collect customer_name, product, quantity, fulfillment and show_chart.
# Keep quantity an integer from 1 through 30.
with st.sidebar:
    st.header("Order Options")
    customer_name = st.text_input("Customer Name")
    product = st.selectbox("Product", list(menu.keys()))
    quantity = st.number_input(
        "Quantity", 
        min_value=1,
        max_value=30,
        value=1,
        step=1
    )
    fulfillment = st.radio("Fulfillment", ["Pickup", "Delivery"])
    show_chart = st.checkbox("Show sample sales chart", value=True)


# TODO 4 - Step 6: Calculate unit_price, subtotal and discounted_subtotal.
# Call your functions. Calculate discount_amount, delivery_fee and total.
# Pickup costs 0; Delivery uses shipping_fee(subtotal).

unit_price = menu[product]
subtotal = unit_price * quantity
discounted_subtotal = apply_discount(subtotal)
discount_amount = subtotal - discounted_subtotal
if fulfillment == "Pickup":
    delivery_fee = o.o
else:
    delivery_fee = shipping_fee(subtotal)
total = discounted_subtotal + delivery_fee

# TODO 5 - Step 7: Show the quote in two columns with dollars to 2 decimals.
# Include product, quantity, unit price, fulfillment, subtotal, discount,
# delivery fee and final total. Keep this outside the button block.


# TODO 6 - Step 8: Build and display the menu table from the menu dictionary.
# Add a clearly labeled fictional sample-sales chart controlled by show_chart.


# TODO 7 - Step 9: Add a Check quote button.
# Warn if customer_name is blank or spaces only. Otherwise show a check message.
# Do not claim that an order was saved, submitted or paid for.


# TODO 8: Test, add your own comments and remove the starter info message.
# Do not upload your submission report or screenshots to this public repository.
