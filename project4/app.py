import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO

st.set_page_config(
    page_title="Data Visualization Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown("""
<style>

    .main {
        background-color: #f5f9fc;
    }

    .dashboard-title {
        background: linear-gradient(90deg, #315a72, #6b8e62);
        padding: 25px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }

    .dashboard-title h1 {
        margin: 0;
        font-size: 36px;
    }

    .dashboard-title p {
        margin-top: 8px;
        font-size: 17px;
    }

    .section-title {
        color: #315a72;
        font-weight: bold;
        font-size: 24px;
        margin-top: 20px;
    }

    [data-testid="stMetric"] {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #6b8e62;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

</style>
""", unsafe_allow_html=True)


DATA = """
OrderID,Date,CustomerID,Product,Quantity,UnitPrice,ShippingAddress,PaymentMethod,OrderStatus,TrackingNumber,ItemsInCart,CouponCode,ReferralSource,TotalPrice
ORD200000,2023-01-04,C72649,Monitor,5,570.62,928 Main St,Debit Card,Shipped,TRK37947903,7,SAVE10,Instagram,2853.10
ORD200001,2024-08-23,C75739,Phone,2,151.35,823 Main St,Online,Shipped,TRK91186779,3,SAVE10,Referral,302.70
ORD200002,2024-02-27,C81728,Tablet,5,550.68,512 Main St,Credit Card,Cancelled,TRK42903982,8,FREESHIP,Email,2753.40
ORD200003,2023-10-15,C33540,Chair,1,273.19,275 Main St,Debit Card,Returned,TRK62788070,5,SAVE10,Facebook,273.19
ORD200004,2025-05-08,C81840,Printer,4,626.01,668 Main St,Online,Delivered,TRK29241424,8,SAVE10,Email,2504.04
ORD200005,2023-10-23,C37249,Phone,2,245.86,934 Main St,Credit Card,Shipped,TRK72976927,4,SAVE10,Instagram,491.72
ORD200006,2025-06-17,C83492,Laptop,1,664.42,986 Main St,Gift Card,Returned,TRK96417362,6,SAVE10,Facebook,664.42
ORD200007,2023-05-12,C41460,Monitor,5,149.55,706 Main St,Cash,Shipped,TRK78809193,9,FREESHIP,Facebook,747.75
ORD200008,2025-04-02,C26817,Phone,2,134.28,904 Main St,Gift Card,Cancelled,TRK61042692,2,,Email,268.56
ORD200009,2023-11-21,C31946,Desk,4,509.38,102 Main St,Credit Card,Shipped,TRK33478363,6,SAVE10,Google,2037.52
ORD200010,2023-12-29,C43443,Tablet,5,625.97,333 Main St,Credit Card,Returned,TRK98859248,9,WINTER15,Instagram,3129.85
ORD200011,2024-02-17,C93861,Monitor,3,49.14,831 Main St,Online,Returned,TRK48234646,7,SAVE10,Email,147.42
ORD200012,2024-10-15,C38785,Monitor,2,180.50,179 Main St,Debit Card,Pending,TRK20419991,6,FREESHIP,Referral,361.00
ORD200013,2023-08-30,C88348,Laptop,3,201.49,903 Main St,Credit Card,Returned,TRK81913874,4,FREESHIP,Facebook,604.47
ORD200014,2023-03-27,C98474,Tablet,2,393.33,980 Main St,Debit Card,Pending,TRK79186539,3,SAVE10,Instagram,786.66
ORD200015,2023-07-17,C39416,Printer,1,473.96,942 Main St,Cash,Delivered,TRK54930938,3,,Google,473.96
ORD200016,2023-01-24,C28976,Printer,2,533.81,914 Main St,Credit Card,Pending,TRK13194259,3,FREESHIP,Email,1067.62
ORD200017,2024-03-02,C60672,Tablet,1,423.40,382 Main St,Debit Card,Shipped,TRK11972116,3,,Referral,423.40
ORD200018,2025-03-26,C84329,Desk,1,431.44,891 Main St,Gift Card,Pending,TRK65191045,3,SAVE10,Facebook,431.44
ORD200019,2023-01-23,C14552,Monitor,5,224.00,273 Main St,Cash,Returned,TRK59101365,9,SAVE10,Google,1120.00
ORD200020,2023-05-08,C54829,Chair,5,62.51,587 Main St,Cash,Pending,TRK16718651,9,WINTER15,Instagram,312.55
ORD200021,2024-11-17,C99023,Monitor,4,342.95,569 Main St,Cash,Delivered,TRK52646983,6,,Google,1371.80
ORD200022,2023-01-29,C34416,Monitor,2,49.62,633 Main St,Online,Pending,TRK75937350,2,SAVE10,Google,99.24
ORD200023,2025-04-09,C42372,Phone,4,273.25,755 Main St,Debit Card,Cancelled,TRK36168083,5,FREESHIP,Referral,1093.00
ORD200024,2024-10-30,C17470,Laptop,2,230.95,956 Main St,Online,Delivered,TRK28775057,3,WINTER15,Referral,461.90
ORD200025,2024-07-24,C42577,Monitor,1,399.98,709 Main St,Debit Card,Delivered,TRK69423327,3,WINTER15,Email,399.98
ORD200026,2024-03-06,C21944,Laptop,5,59.55,296 Main St,Online,Delivered,TRK80276812,6,,Referral,297.75
ORD200027,2024-02-22,C97593,Printer,1,472.74,881 Main St,Online,Shipped,TRK89117573,6,WINTER15,Google,472.74
ORD200028,2023-11-21,C59823,Phone,4,160.07,568 Main St,Online,Pending,TRK65895539,5,,Email,640.28
ORD200029,2024-09-20,C33260,Desk,3,423.53,930 Main St,Credit Card,Delivered,TRK59744090,6,SAVE10,Referral,1270.59
ORD200030,2025-03-22,C44267,Monitor,2,426.70,895 Main St,Online,Pending,TRK54751444,5,SAVE10,Referral,853.40
ORD200031,2023-06-30,C26445,Chair,3,500.08,996 Main St,Debit Card,Returned,TRK31229981,6,,Facebook,1500.24
ORD200032,2023-05-01,C12388,Tablet,5,536.72,830 Main St,Cash,Delivered,TRK99261395,10,,Email,2683.60
ORD200033,2023-06-05,C52184,Chair,1,162.77,912 Main St,Online,Cancelled,TRK73312471,4,WINTER15,Facebook,162.77
ORD200034,2023-01-07,C67195,Chair,4,576.52,926 Main St,Credit Card,Pending,TRK55467915,5,WINTER15,Facebook,2306.08
ORD200035,2024-12-07,C50304,Monitor,2,465.15,128 Main St,Online,Shipped,TRK46850888,2,SAVE10,Facebook,930.30
ORD200036,2025-05-08,C59337,Laptop,2,534.43,465 Main St,Debit Card,Pending,TRK50961250,5,,Facebook,1068.86
ORD200037,2024-10-14,C10054,Laptop,2,76.74,409 Main St,Cash,Returned,TRK94005261,7,SAVE10,Instagram,153.48
ORD200038,2024-12-19,C15924,Laptop,1,245.89,549 Main St,Debit Card,Delivered,TRK14835975,3,SAVE10,Google,245.89
ORD200039,2025-02-27,C96664,Printer,3,256.46,666 Main St,Credit Card,Delivered,TRK85508960,4,SAVE10,Referral,769.38
ORD200040,2023-08-20,C84766,Desk,2,344.02,267 Main St,Online,Delivered,TRK78967923,4,FREESHIP,Instagram,688.04
ORD200041,2023-12-05,C20212,Monitor,3,611.45,657 Main St,Gift Card,Pending,TRK69733327,4,FREESHIP,Instagram,1834.35
ORD200042,2024-05-06,C28712,Printer,2,151.66,980 Main St,Cash,Cancelled,TRK40772558,6,,Instagram,303.32
ORD200043,2023-12-14,C60572,Chair,3,499.21,871 Main St,Online,Cancelled,TRK20351666,8,,Instagram,1497.63
ORD200044,2025-04-21,C73225,Phone,2,550.18,996 Main St,Gift Card,Returned,TRK73848522,3,FREESHIP,Referral,1100.36
ORD200045,2024-02-10,C17388,Chair,1,317.25,157 Main St,Debit Card,Returned,TRK47077395,1,SAVE10,Facebook,317.25
ORD200046,2024-06-26,C43212,Monitor,4,550.14,223 Main St,Debit Card,Pending,TRK25100762,4,FREESHIP,Instagram,2200.56
ORD200047,2023-07-19,C38134,Desk,2,209.94,323 Main St,Credit Card,Returned,TRK42450754,3,FREESHIP,Email,419.88
ORD200048,2023-08-26,C12408,Monitor,2,80.77,464 Main St,Debit Card,Shipped,TRK38938858,4,,Google,161.54
"""


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(StringIO(DATA))

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year

df["Month"] = df["Date"].dt.to_period("M").astype(str)

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

df["TotalPrice"] = pd.to_numeric(df["TotalPrice"])

df["Quantity"] = pd.to_numeric(df["Quantity"])

df["UnitPrice"] = pd.to_numeric(df["UnitPrice"])



st.sidebar.title("🎛️ Dashboard Filters")

st.sidebar.markdown("### Select Filters")

selected_years = st.sidebar.multiselect(
    "📅 Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

selected_products = st.sidebar.multiselect(
    "🛍️ Product",
    sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

selected_status = st.sidebar.multiselect(
    "📦 Order Status",
    sorted(df["OrderStatus"].unique()),
    default=sorted(df["OrderStatus"].unique())
)

selected_payment = st.sidebar.multiselect(
    "💳 Payment Method",
    sorted(df["PaymentMethod"].unique()),
    default=sorted(df["PaymentMethod"].unique())
)




filtered_df = df[
    (df["Year"].isin(selected_years))
    & (df["Product"].isin(selected_products))
    & (df["OrderStatus"].isin(selected_status))
    & (df["PaymentMethod"].isin(selected_payment))
].copy()


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="dashboard-title">

<h1>📊 Data Visualization Dashboard</h1>

<p>
E-Commerce Sales Analysis & Business Insights
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    "### 🎯 Goal: Create visual representations of data to communicate insights clearly."
)




if filtered_df.empty:

    st.warning("⚠️ No data available for the selected filters.")

    st.stop()




total_orders = len(filtered_df)

total_revenue = filtered_df["TotalPrice"].sum()

total_quantity = filtered_df["Quantity"].sum()

average_order_value = filtered_df["TotalPrice"].mean()

unique_customers = filtered_df["CustomerID"].nunique()



st.markdown('<p class="section-title">📌 Key Performance Indicators</p>',
            unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "🛒 Total Orders",
    f"{total_orders:,}"
)

col2.metric(
    "💰 Total Revenue",
    f"${total_revenue:,.2f}"
)

col3.metric(
    "📦 Quantity Sold",
    f"{total_quantity:,}"
)

col4.metric(
    "💵 Average Order Value",
    f"${average_order_value:,.2f}"
)

col5.metric(
    "👥 Customers",
    f"{unique_customers:,}"
)




st.markdown('<p class="section-title">📊 Product Performance</p>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    product_sales = (
        filtered_df
        .groupby("Product", as_index=False)["TotalPrice"]
        .sum()
        .sort_values("TotalPrice", ascending=False)
    )

    fig_product = px.bar(
        product_sales,
        x="Product",
        y="TotalPrice",
        color="Product",
        title="Revenue by Product",
        labels={
            "TotalPrice": "Revenue ($)",
            "Product": "Product"
        },
        text_auto=".2s"
    )

    fig_product.update_layout(
        template="plotly_white",
        showlegend=False
    )

    st.plotly_chart(
        fig_product,
        use_container_width=True
    )




with col2:

    product_quantity = (
        filtered_df
        .groupby("Product", as_index=False)["Quantity"]
        .sum()
        .sort_values("Quantity", ascending=False)
    )

    fig_quantity = px.bar(
        product_quantity,
        x="Product",
        y="Quantity",
        color="Product",
        title="Quantity Sold by Product",
        labels={
            "Quantity": "Quantity Sold",
            "Product": "Product"
        },
        text_auto=True
    )

    fig_quantity.update_layout(
        template="plotly_white",
        showlegend=False
    )

    st.plotly_chart(
        fig_quantity,
        use_container_width=True
    )




st.markdown('<p class="section-title">📈 Sales Trend</p>',
            unsafe_allow_html=True)

monthly_sales = (
    filtered_df
    .groupby("Month", as_index=False)["TotalPrice"]
    .sum()
)

fig_monthly = px.line(
    monthly_sales,
    x="Month",
    y="TotalPrice",
    markers=True,
    title="Monthly Revenue Trend",
    labels={
        "Month": "Month",
        "TotalPrice": "Revenue ($)"
    }
)

fig_monthly.update_traces(
    line=dict(
        color="#315A72",
        width=3
    )
)

fig_monthly.update_layout(
    template="plotly_white",
    hovermode="x unified"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)




st.markdown('<p class="section-title">📦 Order Status Analysis</p>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    status_data = (
        filtered_df["OrderStatus"]
        .value_counts()
        .reset_index()
    )

    status_data.columns = [
        "OrderStatus",
        "Orders"
    ]

    fig_status = px.pie(
        status_data,
        names="OrderStatus",
        values="Orders",
        hole=0.45,
        title="Order Status Distribution"
    )

    fig_status.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_status.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(
        fig_status,
        use_container_width=True
    )



with col2:

    payment_data = (
        filtered_df
        .groupby("PaymentMethod", as_index=False)["TotalPrice"]
        .sum()
        .sort_values("TotalPrice", ascending=False)
    )

    fig_payment = px.bar(
        payment_data,
        x="PaymentMethod",
        y="TotalPrice",
        color="PaymentMethod",
        title="Revenue by Payment Method",
        labels={
            "TotalPrice": "Revenue ($)",
            "PaymentMethod": "Payment Method"
        },
        text_auto=".2s"
    )

    fig_payment.update_layout(
        template="plotly_white",
        showlegend=False
    )

    st.plotly_chart(
        fig_payment,
        use_container_width=True
    )



st.markdown('<p class="section-title">📣 Marketing & Referral Analysis</p>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    referral_data = (
        filtered_df["ReferralSource"]
        .value_counts()
        .reset_index()
    )

    referral_data.columns = [
        "ReferralSource",
        "Orders"
    ]

    fig_referral = px.bar(
        referral_data,
        x="ReferralSource",
        y="Orders",
        color="ReferralSource",
        title="Orders by Referral Source",
        text_auto=True
    )

    fig_referral.update_layout(
        template="plotly_white",
        showlegend=False
    )

    st.plotly_chart(
        fig_referral,
        use_container_width=True
    )




with col2:

    yearly_data = (
        filtered_df
        .groupby("Year", as_index=False)["TotalPrice"]
        .sum()
    )

    fig_year = px.bar(
        yearly_data,
        x="Year",
        y="TotalPrice",
        color="Year",
        title="Revenue by Year",
        labels={
            "TotalPrice": "Revenue ($)",
            "Year": "Year"
        },
        text_auto=".2s"
    )

    fig_year.update_layout(
        template="plotly_white",
        showlegend=False
    )

    st.plotly_chart(
        fig_year,
        use_container_width=True
    )



st.markdown('<p class="section-title">💡 Key Insights</p>',
            unsafe_allow_html=True)

product_revenue = (
    filtered_df
    .groupby("Product")["TotalPrice"]
    .sum()
)

top_product = product_revenue.idxmax()

top_product_revenue = product_revenue.max()


status_counts = filtered_df["OrderStatus"].value_counts()

common_status = status_counts.idxmax()

common_status_count = status_counts.max()


payment_revenue = (
    filtered_df
    .groupby("PaymentMethod")["TotalPrice"]
    .sum()
)

top_payment = payment_revenue.idxmax()

top_payment_revenue = payment_revenue.max()


referral_counts = filtered_df["ReferralSource"].value_counts()

top_referral = referral_counts.idxmax()

top_referral_orders = referral_counts.max()


col1, col2 = st.columns(2)

with col1:

    st.success(
        f"🏆 **Top Product:** {top_product} "
        f"generated **${top_product_revenue:,.2f}** revenue."
    )

    st.info(
        f"📦 **Most Common Order Status:** {common_status} "
        f"with **{common_status_count} orders**."
    )


with col2:

    st.success(
        f"💳 **Top Payment Method:** {top_payment} "
        f"generated **${top_payment_revenue:,.2f}** revenue."
    )

    st.info(
        f"📣 **Top Referral Source:** {top_referral} "
        f"generated **{top_referral_orders} orders**."
    )




st.markdown('<p class="section-title">📋 Order Data</p>',
            unsafe_allow_html=True)

display_columns = [
    "OrderID",
    "Date",
    "CustomerID",
    "Product",
    "Quantity",
    "UnitPrice",
    "PaymentMethod",
    "OrderStatus",
    "ItemsInCart",
    "CouponCode",
    "ReferralSource",
    "TotalPrice"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)



csv_data = filtered_df[display_columns].to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv_data,
    file_name="filtered_orders.csv",
    mime="text/csv"
)



st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#6B8E62;">
        <b>Data Visualization Project</b><br>
        Visualizations • Charts • Storytelling with Data
    </div>
    """,
    unsafe_allow_html=True
)
