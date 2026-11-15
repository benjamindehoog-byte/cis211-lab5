# CIS 211 Lab 5 - Bright Bakery Interactive Order Calculator
# Completed the TODO sections.
# Added several comments to the code.

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
    if subtotal >=50:
        return round(subtotal * 0.9, 2)
    else:
        return subtotal

def shipping_fee(subtotal):
    if subtotal >= 35:
        return 0.0
    else:
        return 5.99
  
st.title("Bright Bakery Interactive Order Calculator")
st.caption("A class practice app that calculates a quote.")

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


# Call your functions. Calculate discount_amount, delivery_fee and total.
# Pickup costs 0; Delivery uses shipping_fee(subtotal).
# The selected product is used as a key in the menu dictionary to find its unit price.

unit_price = menu[product]
subtotal = unit_price * quantity
discounted_subtotal = apply_discount(subtotal)
discount_amount = subtotal - discounted_subtotal
# Delivery price is based on the original subtotal, before any discount is applied.
if fulfillment == "Pickup":
    delivery_fee = 0.0
else:
    delivery_fee = shipping_fee(subtotal)
total = discounted_subtotal + delivery_fee

# Include product, quantity, unit price, fulfillment, subtotal, discount,
# delivery fee and final total. Keep this outside the button block.
st.header("Your Order Quote")
left, right = st.columns(2)
with left:
    st.subheader("Order Details")
    st.write(f"Product: {product}")
    st.write(f"Quantity: {quantity}")
    st.write(f"Unit Price: ${unit_price:.2f}")
    st.write(f"Fulfillment: {fulfillment}")
with right:
    st.subheader("Order Summary")
    st.write(f"Subtotal: ${subtotal:.2f}")
    st.write(f"Discount Amount: ${discount_amount:.2f}")
    st.write(f"Delivery Fee: ${delivery_fee:.2f}")
    st.write(f"Final Total: ${total:.2f}")

# Add a clearly labeled fictional sample-sales chart controlled by show_chart.
st.header("Bakery Menu")

# I didn't like how the menu was showing, so I created a formatted menu. 
formatted_menu = {
    product: f"${price:.2f}"
    for product, price in menu.items()
}

# Again, didn't like how the table was showing, so added headers for easier viewing. 
st.table({
    "Product": list(formatted_menu.keys()),
    "Price": list(formatted_menu.values())
})
st.header("Fictional Sample Sales")
if show_chart:
    st.bar_chart(sample_sales, x="Product", y="Units sold")

# Warn if customer_name is blank or spaces only. Otherwise show a check message.
# Do not claim that an order was saved, submitted or paid for.
# Strip removes extra spaces, so a blank name won't pass the validation check.
if st.button("Check Quote"):
    if not customer_name.strip():
        st.warning("Please enter your name before checking the quote.")
    else:
        st.success("Quote checked successfully. This is only an estimate; no order has been placed.")

# Tested!
# Not uploading my submission report or screenshots to this public repository.
