
import streamlit as st

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
    # Orders of $50 or more get 10% off.
    if subtotal >= 50:
        return round(subtotal * 0.90, 2)
    else:
        return subtotal


def shipping_fee(subtotal):
    # Free delivery depends on the original subtotal.
    if subtotal >= 35:
        return 0.0
    else:
        return 5.99


st.title("Bright Bakery Interactive Order Calculator")
st.caption("A class practice app that calculates a quote.")

with st.sidebar:
    st.header("Order options")
    customer_name = st.text_input("Customer name or nickname")
    product = st.selectbox("Product", list(menu.keys()))
    quantity = st.number_input("Quantity", min_value=1, max_value=30, value=1, step=1)
    fulfillment = st.selectbox("Fulfillment", ["Pickup", "Delivery"])
    show_chart = st.checkbox("Show sample sales chart", value=True)

unit_price = menu[product]
subtotal = unit_price * quantity
discounted_subtotal = apply_discount(subtotal)
discount_amount = round(subtotal - discounted_subtotal, 2)

# Pickup does not need a delivery fee.
if fulfillment == "Pickup":
    delivery_fee = 0.0
else:
    delivery_fee = shipping_fee(subtotal)

total = round(discounted_subtotal + delivery_fee, 2)

# The quote stays outside the button so it updates with each selection.
st.subheader("Current quote")
col1, col2 = st.columns(2)

with col1:
    st.write(f"Product: {product}")
    st.write(f"Quantity: {quantity}")
    st.write(f"Unit price: ${unit_price:.2f}")
    st.write(f"Fulfillment: {fulfillment}")

with col2:
    st.write(f"Original subtotal: ${subtotal:.2f}")
    st.write(f"Discount: ${discount_amount:.2f}")
    st.write(f"Delivery fee: ${delivery_fee:.2f}")
    st.metric("Final total", f"${total:.2f}")

st.subheader("Bakery menu")
menu_data = {
    "Product": list(menu.keys()),
    "Price ($)": list(menu.values()),
}
st.dataframe(menu_data, hide_index=True)

if show_chart:
    st.subheader("Sample sales")
    st.caption("These are fictional sales for practice.")
    st.bar_chart(sample_sales, x="Product", y="Units sold", sort=False)

if st.button("Check quote"):
    clean_name = customer_name.strip()
    if clean_name == "":
        st.warning("Please enter your name or nickname.")
    else:
        st.success(f"Quote checked for {clean_name}. This is only a practice app. No order was saved or paid for.")
