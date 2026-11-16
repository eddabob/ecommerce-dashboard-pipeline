import streamlit as st
import duckdb
import plotly.express as px

st.set_page_config(page_title='E-Commerce Executive Dashboard', layout='wide')
st.title('E-Commerce Revenue & Delivery Performance')

con = duckdb.connect("ecommerce.duckdb", read_only=True)
df = con.execute("SELECT * FROM main.fct_orders WHERE order_status ='delivered'").df()

col1, col2, col3 = st.columns(3)
total_revenue = df['total_revenue'].sum()
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
total_orders = len(df)
col2.metric("Total Delivered Orders", f"{total_orders:,.0f}")
late_pct = (df['days_late'] >0).mean()*100
col3.metric("Late Delivery Rate", f"{late_pct:,.1f}%")

monthly = df.groupby("order_month", as_index=False)['total_revenue'].sum().sort_values("order_month")
fig = px.line(monthly, 
              x="order_month",
              y="total_revenue",
              title = "Monthly Revenue Trend")
st.plotly_chart(fig, use_container_width = True)

