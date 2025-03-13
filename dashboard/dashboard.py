import urllib

import matplotlib.image as mpimg
import matplotlib.ticker as mticker

import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
import streamlit as st

from func import DataAnalyzer, BrazilMapPlotter, get_base64_image

# Load Main Dataset
datetime_cols = ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date",
                 "order_estimated_delivery_date", "order_purchase_timestamp", "shipping_limit_date"]
main_df = pd.read_csv("./dashboard/main_data.csv")
main_df.sort_values(by="order_approved_at", inplace=True)
main_df.reset_index(inplace=True)

# Load Geolocation Dataset
geolocation = pd.read_csv('./dashboard/geolocation.csv')
data = geolocation.drop_duplicates(subset='customer_unique_id')

for col in datetime_cols:
    main_df[col] = pd.to_datetime(main_df[col])

min_date = main_df["order_approved_at"].min()
max_date = main_df["order_approved_at"].max()

# Sidebars
with st.sidebar:
    st.title("Menu")

    # Date Range
    start_date, end_date = st.date_input(
        label="Select Date Range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

# Main
main_df = main_df[(main_df["order_approved_at"] >= str(start_date)) &
                  (main_df["order_approved_at"] <= str(end_date))]

function = DataAnalyzer(main_df)
map_plot = BrazilMapPlotter(data, plt, mpimg, urllib, st)

sum_order_items_df = function.create_sum_order_items_df()
review_score, common_score = function.review_score_df()
state, most_common_state = function.create_bystate_df()
order_status, common_status = function.create_order_status()

image_base64 = get_base64_image("./dashboard/logo.jpg")
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{image_base64}' width='150' style='border-radius: 20%;'>
        <h1>E-Commerce Dashboard</h1>
        <h5>By Johanadi Santoso</h5>
    </div>
    <br>
    """,
    unsafe_allow_html=True
)

# Gross Revenue
st.subheader("Gross Revenue")

orders_filtered = main_df[main_df["order_purchase_timestamp"]
                          <= "2018-08-31"].copy()
orders_filtered["year_month"] = orders_filtered["order_purchase_timestamp"].dt.to_period(
    "M")
monthly_payments = orders_filtered.groupby("year_month")["payment_value"].sum()
months = monthly_payments.index.astype(str)
values = monthly_payments.values

fig, ax = plt.subplots(figsize=(13, 7))
ax.plot(months, values, marker='o', linestyle='-', color='b')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(
    lambda x, _: f'R${x:,.0f}'))  # Format mata uang BRL
ax.set_xticklabels(months, rotation=45)
ax.set_xlabel("Bulan", fontsize=12)
ax.set_ylabel("Total Pendapatan (BRL)", fontsize=12)
ax.set_title("Gross Revenue E-Commerce Hingga Agustus 2018", fontsize=14)
ax.grid(True, linestyle="--", alpha=0.7)
st.pyplot(fig)

with st.expander("Insight"):
    st.write("""
    - Terjadi peningkatan pendapatan yang signifikan sejak akhir 2016 hingga 2018, menunjukkan pertumbuhan bisnis e-commerce.
    - Puncak pendapatan terjadi pada akhir 2017, kemungkinan karena musim belanja akhir tahun.
    - Setelah Desember 2017, pendapatan mengalami beberapa penurunan tetapi tetap tinggi dibandingkan tahun sebelumnya.
    - Kesimpulan: E-commerce berkembang pesat dengan puncak pendapatan di musim liburan, menunjukkan peluang besar dalam strategi promosi berbasis musiman.
    """)
st.write("")

# Order Items
st.subheader("Order Items")
col1, col2 = st.columns(2)

with col1:
    total_items = sum_order_items_df["product_count"].sum()
    st.markdown(f"Total Items: **{total_items}**")

with col2:
    avg_items = sum_order_items_df["product_count"].mean()
    st.markdown(f"Average Items: **{avg_items}**")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(45, 25))

colors_high = ["#00C853", "#C0C0C0", "#C0C0C0", "#C0C0C0", "#C0C0C0"]
colors_low = ["#D32F2F", "#C0C0C0", "#C0C0C0", "#C0C0C0", "#C0C0C0"]

sns.barplot(x="product_category_name_english", y="product_count",
            data=sum_order_items_df.head(5), hue="product_category_name_english",
            palette=colors_high, ax=ax[0], legend=False)

ax[0].set_ylabel("Number of Sales", fontsize=45)
ax[0].set_xlabel(None)
ax[0].set_title("Produk dengan Penjualan Tertinggi", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30, rotation=45)

sns.barplot(x="product_category_name_english", y="product_count",
            data=sum_order_items_df.sort_values(
                by="product_count", ascending=True).head(5),
            hue="product_category_name_english", palette=colors_low, ax=ax[1], legend=False)

ax[1].set_ylabel("Number of Sales", fontsize=35)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Produk dengan Penjualan Terendah", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30, rotation=45)

st.pyplot(fig)

with st.expander("Insight"):
    st.write('- Produk dengan penjualan tertinggi adalah bed_bath_table, yang menunjukkan bahwa produk rumah tangga dan dekorasi memiliki permintaan tinggi di e-commerce. Sementara itu, produk dengan penjualan terendah adalah security_and_services.')
st.text("")

# Review Score
st.subheader("Review Score")
col1, col2 = st.columns(2)

with col1:
    avg_review_score = review_score.mean()
    st.markdown(f"Average Review Score: **{avg_review_score}**")

with col2:
    most_common_review_score = review_score.value_counts().index[0]
    st.markdown(f"Most Common Review Score: **{most_common_review_score}**")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=review_score.index,
            y=review_score.values,
            order=review_score.index,
            palette=["#00C853" if score ==
                     common_score else "#C0C0C0" for score in review_score.index]
            )

plt.title("Rating by customers for service", fontsize=15)
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(fontsize=12)
st.pyplot(fig)

with st.expander("Insight"):
    st.write('- Pelanggan sangat puas dengan layanan yang diberikan. Hal ini dibuktikan dengan dominasi rating **5**, yang memiliki jumlah ulasan terbanyak dibandingkan dengan rating lainnya.')
st.divider()

# Customer Demographic
st.subheader("Customer Demographic")
tab1, tab2 = st.tabs(["State", "Geolocation"])

with tab1:
    most_common_state = state.customer_state.value_counts().index[0]
    st.markdown(f"Most Common State: **{most_common_state}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=state.customer_state.value_counts().index,
                y=state.customer_count.values,
                data=state,
                palette=["#00C853" if score ==
                         most_common_state else "#C0C0C0" for score in state.customer_state.value_counts().index]
                )

    plt.title("Number customers from State", fontsize=15)
    plt.xlabel("State")
    plt.ylabel("Number of Customers")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

with tab2:
    map_plot.plot()

    with st.expander("Insight"):
        st.write('- Mayoritas pelanggan berasal dari negara bagian di wilayah tenggara dan selatan, menunjukkan bahwa pasar e-commerce lebih berkembang di daerah ini. Faktor-faktor seperti populasi yang lebih besar, infrastruktur logistik yang lebih baik, dan preferensi belanja online bisa menjadi alasan utama.')


st.caption("© 2025 Johanadi Santoso")
