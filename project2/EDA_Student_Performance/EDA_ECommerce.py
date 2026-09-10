# ============================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# E-Commerce Orders Dataset
# ============================================================
#
# Project:
# Exploratory Data Analysis
#
# Objective:
# Analyze E-Commerce Orders data to understand:
# - Data structure
# - Missing values
# - Duplicate records
# - Data types
# - Data validation
# - Descriptive statistics
# - Product performance
# - Order status
# - Payment methods
# - Referral sources
# - Coupon usage
# - Revenue trends
# - Correlations
# - Outliers
# - Key business observations
#
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import os

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 2. CONFIGURATION
# ============================================================

DATA_FILE = "dataset.csv"

OUTPUT_DIR = "output"

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Plot style
sns.set_theme(style="whitegrid")


# ============================================================
# DATASET COLUMNS
# ============================================================

EXPECTED_COLUMNS = [
    "OrderID",
    "Date",
    "CustomerID",
    "Product",
    "Quantity",
    "UnitPrice",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "TrackingNumber",
    "ItemsInCart",
    "CouponCode",
    "ReferralSource",
    "TotalPrice"
]


NUMERIC_COLUMNS = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]


# ============================================================
# 3. HEADER
# ============================================================

print("\n" + "=" * 70)
print("EXPLORATORY DATA ANALYSIS - E-COMMERCE ORDERS")
print("=" * 70)


# ============================================================
# 4. LOAD DATASET
# ============================================================

print("\n[1] Loading dataset...")

if not os.path.exists(DATA_FILE):

    print("\nERROR: Dataset file not found.")
    print(f"Expected file: {DATA_FILE}")

    print("\nMake sure your folder looks like:")
    print("EDA_Student_Performance/")
    print("    EDA_ECommerce.py")
    print("    dataset.csv")

    raise SystemExit


try:

    # First try TAB-separated format
    df = pd.read_csv(DATA_FILE, sep="\t")

    # If only one column is detected,
    # try normal comma-separated CSV
    if len(df.columns) == 1:

        df = pd.read_csv(DATA_FILE)

    print("Dataset loaded successfully.")

except Exception as error:

    print("\nERROR while loading dataset:")
    print(error)

    raise SystemExit


# ============================================================
# 5. CLEAN COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)


# ============================================================
# 6. DISPLAY COLUMN NAMES
# ============================================================

print("\n" + "=" * 70)
print("COLUMN NAMES")
print("=" * 70)

for number, column in enumerate(df.columns, start=1):

    print(f"{number}. {column}")


# ============================================================
# 7. FIRST FIVE RECORDS
# ============================================================

print("\n" + "=" * 70)
print("FIRST FIVE RECORDS")
print("=" * 70)

print(
    df.head().to_string(index=False)
)


# ============================================================
# 8. DATASET SHAPE
# ============================================================

print("\n" + "=" * 70)
print("DATASET SHAPE")
print("=" * 70)

rows, columns = df.shape

print(f"Number of Rows    : {rows}")
print(f"Number of Columns : {columns}")


# ============================================================
# 9. CHECK EXPECTED COLUMNS
# ============================================================

print("\n" + "=" * 70)
print("COLUMN VALIDATION")
print("=" * 70)

missing_columns = []

for column in EXPECTED_COLUMNS:

    if column in df.columns:

        print(f"OK      : {column}")

    else:

        print(f"MISSING : {column}")

        missing_columns.append(column)


if len(missing_columns) > 0:

    print("\nWARNING:")
    print("Some expected columns are missing.")

    print("\nMissing columns:")

    for column in missing_columns:

        print(f"- {column}")

    print("\nAvailable columns:")

    for column in df.columns:

        print(f"- {column}")

    raise SystemExit


# ============================================================
# 10. DATAFRAME INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("COLUMN INFORMATION")
print("=" * 70)

df.info()


# ============================================================
# 11. MISSING VALUES
# ============================================================

print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

missing_values = df.isnull().sum()

print(missing_values.to_string())

total_missing = missing_values.sum()

if total_missing == 0:

    print("\nNo missing values were found.")

else:

    print(
        f"\nTotal missing values: {total_missing}"
    )


# Save missing value report
missing_report = pd.DataFrame({
    "Column": missing_values.index,
    "MissingValues": missing_values.values
})

missing_report.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "missing_values.csv"
    ),
    index=False
)


# ============================================================
# 12. DUPLICATE RECORDS
# ============================================================

print("\n" + "=" * 70)
print("DUPLICATE RECORDS")
print("=" * 70)

duplicate_count = df.duplicated().sum()

print(
    f"Number of duplicate rows: {duplicate_count}"
)

if duplicate_count == 0:

    print("No duplicate records were found.")

else:

    print("Duplicate records were found.")


# ============================================================
# 13. DATA TYPES
# ============================================================

print("\n" + "=" * 70)
print("DATA TYPES")
print("=" * 70)

print(
    df.dtypes.to_string()
)


# ============================================================
# 14. CONVERT DATE COLUMN
# ============================================================

print("\n" + "=" * 70)
print("DATE CONVERSION")
print("=" * 70)

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

invalid_dates = df["Date"].isnull().sum()

print(
    f"Invalid date values: {invalid_dates}"
)


# ============================================================
# 15. CONVERT NUMERIC COLUMNS
# ============================================================

print("\n" + "=" * 70)
print("NUMERIC DATA CONVERSION")
print("=" * 70)

for column in NUMERIC_COLUMNS:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

    print(
        f"{column}: converted successfully"
    )


# ============================================================
# 16. CHECK NUMERIC MISSING VALUES
# ============================================================

print("\n" + "=" * 70)
print("NUMERIC COLUMN VALIDATION")
print("=" * 70)

for column in NUMERIC_COLUMNS:

    missing = df[column].isnull().sum()

    print(
        f"{column:<15}: {missing} missing values"
    )


# ============================================================
# 17. NEGATIVE VALUES CHECK
# ============================================================

print("\n" + "=" * 70)
print("NEGATIVE VALUES CHECK")
print("=" * 70)

for column in NUMERIC_COLUMNS:

    negative_values = (
        df[column] < 0
    ).sum()

    print(
        f"{column:<15}: "
        f"{negative_values} negative values"
    )


# ============================================================
# 18. QUANTITY VALIDATION
# ============================================================

print("\n" + "=" * 70)
print("QUANTITY VALIDATION")
print("=" * 70)

invalid_quantity = df[
    df["Quantity"] <= 0
]

print(
    f"Invalid quantity records: "
    f"{len(invalid_quantity)}"
)


# ============================================================
# 19. UNIT PRICE VALIDATION
# ============================================================

print("\n" + "=" * 70)
print("UNIT PRICE VALIDATION")
print("=" * 70)

invalid_price = df[
    df["UnitPrice"] <= 0
]

print(
    f"Invalid UnitPrice records: "
    f"{len(invalid_price)}"
)


# ============================================================
# 20. TOTAL PRICE VALIDATION
# ============================================================

print("\n" + "=" * 70)
print("TOTAL PRICE VALIDATION")
print("=" * 70)

# Calculate expected total
df["CalculatedTotal"] = (
    df["Quantity"] *
    df["UnitPrice"]
)

# Difference
df["PriceDifference"] = (
    df["TotalPrice"] -
    df["CalculatedTotal"]
)

incorrect_total = df[
    df["PriceDifference"].abs() > 0.01
]

print(
    f"Orders with incorrect TotalPrice: "
    f"{len(incorrect_total)}"
)


# ============================================================
# 21. DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 70)
print("DESCRIPTIVE STATISTICS")
print("=" * 70)

statistics = (
    df[NUMERIC_COLUMNS]
    .describe()
    .T
)

statistics["median"] = (
    df[NUMERIC_COLUMNS]
    .median()
)

statistics = statistics[
    [
        "count",
        "mean",
        "median",
        "std",
        "min",
        "25%",
        "50%",
        "75%",
        "max"
    ]
]

print(
    statistics.round(2)
)


# Save statistics
statistics.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "descriptive_statistics.csv"
    )
)


# ============================================================
# 22. MEAN
# ============================================================

print("\n" + "=" * 70)
print("MEAN")
print("=" * 70)

for column in NUMERIC_COLUMNS:

    value = df[column].mean()

    print(
        f"{column:<15}: {value:.2f}"
    )


# ============================================================
# 23. MEDIAN
# ============================================================

print("\n" + "=" * 70)
print("MEDIAN")
print("=" * 70)

for column in NUMERIC_COLUMNS:

    value = df[column].median()

    print(
        f"{column:<15}: {value:.2f}"
    )


# ============================================================
# 24. MINIMUM AND MAXIMUM
# ============================================================

print("\n" + "=" * 70)
print("MINIMUM AND MAXIMUM")
print("=" * 70)

for column in NUMERIC_COLUMNS:

    minimum = df[column].min()

    maximum = df[column].max()

    print(f"\n{column}")

    print(
        f"Minimum : {minimum:.2f}"
    )

    print(
        f"Maximum : {maximum:.2f}"
    )


# ============================================================
# 25. PRODUCT ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("PRODUCT ANALYSIS")
print("=" * 70)

product_orders = (
    df["Product"]
    .value_counts()
)

print(
    product_orders.to_string()
)


# ============================================================
# 26. PRODUCT QUANTITY
# ============================================================

print("\n" + "=" * 70)
print("QUANTITY SOLD BY PRODUCT")
print("=" * 70)

quantity_by_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print(
    quantity_by_product.to_string()
)


# Save product quantity
quantity_by_product.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "quantity_by_product.csv"
    )
)


# ============================================================
# 27. REVENUE BY PRODUCT
# ============================================================

print("\n" + "=" * 70)
print("REVENUE BY PRODUCT")
print("=" * 70)

revenue_by_product = (
    df.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print(
    revenue_by_product
    .round(2)
    .to_string()
)


# Save product revenue
revenue_by_product.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "revenue_by_product.csv"
    )
)


# ============================================================
# 28. ORDER STATUS ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("ORDER STATUS ANALYSIS")
print("=" * 70)

order_status = (
    df["OrderStatus"]
    .value_counts()
)

print(
    order_status.to_string()
)


# Save status
order_status.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "order_status_analysis.csv"
    )
)


# ============================================================
# 29. REVENUE BY ORDER STATUS
# ============================================================

print("\n" + "=" * 70)
print("REVENUE BY ORDER STATUS")
print("=" * 70)

status_revenue = (
    df.groupby("OrderStatus")["TotalPrice"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print(
    status_revenue
    .round(2)
    .to_string()
)


# ============================================================
# 30. PAYMENT METHOD ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("PAYMENT METHOD ANALYSIS")
print("=" * 70)

payment_counts = (
    df["PaymentMethod"]
    .value_counts()
)

print(
    payment_counts.to_string()
)


# Save payment analysis
payment_counts.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "payment_method_analysis.csv"
    )
)


# ============================================================
# 31. REVENUE BY PAYMENT METHOD
# ============================================================

print("\n" + "=" * 70)
print("REVENUE BY PAYMENT METHOD")
print("=" * 70)

payment_revenue = (
    df.groupby("PaymentMethod")["TotalPrice"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print(
    payment_revenue
    .round(2)
    .to_string()
)


# ============================================================
# 32. REFERRAL SOURCE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("REFERRAL SOURCE ANALYSIS")
print("=" * 70)

referral_counts = (
    df["ReferralSource"]
    .value_counts()
)

print(
    referral_counts.to_string()
)


# Save referral analysis
referral_counts.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "referral_source_analysis.csv"
    )
)


# ============================================================
# 33. REVENUE BY REFERRAL SOURCE
# ============================================================

print("\n" + "=" * 70)
print("REVENUE BY REFERRAL SOURCE")
print("=" * 70)

referral_revenue = (
    df.groupby("ReferralSource")["TotalPrice"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print(
    referral_revenue
    .round(2)
    .to_string()
)


# ============================================================
# 34. COUPON ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("COUPON CODE ANALYSIS")
print("=" * 70)

df["CouponCode"] = (
    df["CouponCode"]
    .fillna("No Coupon")
)

coupon_counts = (
    df["CouponCode"]
    .replace("", "No Coupon")
    .value_counts()
)

print(
    coupon_counts.to_string()
)


# Save coupon analysis
coupon_counts.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "coupon_analysis.csv"
    )
)


# ============================================================
# 35. CUSTOMER ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("CUSTOMER ANALYSIS")
print("=" * 70)

unique_customers = (
    df["CustomerID"]
    .nunique()
)

print(
    f"Unique Customers: "
    f"{unique_customers}"
)


customer_orders = (
    df.groupby("CustomerID")
    .size()
    .sort_values(
        ascending=False
    )
)

print("\nTop customers by number of orders:")

print(
    customer_orders.head(10)
    .to_string()
)


# ============================================================
# 36. KEY BUSINESS METRICS
# ============================================================

print("\n" + "=" * 70)
print("KEY BUSINESS METRICS")
print("=" * 70)

total_orders = len(df)

total_revenue = (
    df["TotalPrice"]
    .sum()
)

total_quantity = (
    df["Quantity"]
    .sum()
)

average_order_value = (
    df["TotalPrice"]
    .mean()
)

average_unit_price = (
    df["UnitPrice"]
    .mean()
)

print(
    f"Total Orders        : {total_orders:,}"
)

print(
    f"Total Revenue       : ${total_revenue:,.2f}"
)

print(
    f"Total Quantity Sold : {total_quantity:,}"
)

print(
    f"Average Order Value : ${average_order_value:,.2f}"
)

print(
    f"Average Unit Price  : ${average_unit_price:,.2f}"
)

print(
    f"Unique Customers    : {unique_customers:,}"
)


# ============================================================
# 37. TOP PRODUCT
# ============================================================

top_product = (
    revenue_by_product
    .idxmax()
)

top_product_revenue = (
    revenue_by_product
    .max()
)

print("\n" + "=" * 70)
print("TOP PRODUCT BY REVENUE")
print("=" * 70)

print(
    f"Product : {top_product}"
)

print(
    f"Revenue : ${top_product_revenue:,.2f}"
)


# ============================================================
# 38. TOP SELLING PRODUCT BY QUANTITY
# ============================================================

top_quantity_product = (
    quantity_by_product
    .idxmax()
)

top_quantity = (
    quantity_by_product
    .max()
)

print("\n" + "=" * 70)
print("TOP PRODUCT BY QUANTITY")
print("=" * 70)

print(
    f"Product  : {top_quantity_product}"
)

print(
    f"Quantity : {top_quantity}"
)


# ============================================================
# 39. TOP REFERRAL SOURCE
# ============================================================

top_referral = (
    referral_counts
    .idxmax()
)

top_referral_orders = (
    referral_counts
    .max()
)

print("\n" + "=" * 70)
print("TOP REFERRAL SOURCE")
print("=" * 70)

print(
    f"Source : {top_referral}"
)

print(
    f"Orders : {top_referral_orders}"
)


# ============================================================
# 40. DATE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("DATE ANALYSIS")
print("=" * 70)

minimum_date = df["Date"].min()

maximum_date = df["Date"].max()

print(
    f"First Order Date : {minimum_date.date()}"
)

print(
    f"Last Order Date  : {maximum_date.date()}"
)


# Create Year and Month
df["Year"] = (
    df["Date"]
    .dt.year
)

df["Month"] = (
    df["Date"]
    .dt.to_period("M")
    .astype(str)
)


# ============================================================
# 41. YEARLY REVENUE
# ============================================================

print("\n" + "=" * 70)
print("YEARLY REVENUE")
print("=" * 70)

yearly_revenue = (
    df.groupby("Year")["TotalPrice"]
    .sum()
)

print(
    yearly_revenue
    .round(2)
    .to_string()
)


# Save yearly revenue
yearly_revenue.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "yearly_revenue.csv"
    )
)


# ============================================================
# 42. MONTHLY REVENUE
# ============================================================

print("\n" + "=" * 70)
print("MONTHLY REVENUE")
print("=" * 70)

monthly_revenue = (
    df.groupby("Month")["TotalPrice"]
    .sum()
)

print(
    monthly_revenue
    .round(2)
    .to_string()
)


# Save monthly revenue
monthly_revenue.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "monthly_revenue.csv"
    )
)


# ============================================================
# 43. CORRELATION MATRIX
# ============================================================

print("\n" + "=" * 70)
print("CORRELATION MATRIX")
print("=" * 70)

correlation_matrix = (
    df[NUMERIC_COLUMNS]
    .corr()
)

print(
    correlation_matrix
    .round(2)
)


# Save correlation
correlation_matrix.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "correlation_matrix.csv"
    )
)


# ============================================================
# 44. OUTLIER DETECTION - IQR
# ============================================================

print("\n" + "=" * 70)
print("OUTLIER DETECTION - IQR METHOD")
print("=" * 70)


def detect_outliers(dataframe, column):

    Q1 = dataframe[column].quantile(0.25)

    Q3 = dataframe[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = (
        Q1 - 1.5 * IQR
    )

    upper_bound = (
        Q3 + 1.5 * IQR
    )

    outliers = dataframe[
        (dataframe[column] < lower_bound)
        |
        (dataframe[column] > upper_bound)
    ]

    return (
        Q1,
        Q3,
        IQR,
        lower_bound,
        upper_bound,
        outliers
    )


outlier_results = []


for column in NUMERIC_COLUMNS:

    (
        Q1,
        Q3,
        IQR,
        lower_bound,
        upper_bound,
        outliers
    ) = detect_outliers(
        df,
        column
    )

    print(f"\n{column}")

    print(
        f"Q1          : {Q1:.2f}"
    )

    print(
        f"Q3          : {Q3:.2f}"
    )

    print(
        f"IQR         : {IQR:.2f}"
    )

    print(
        f"Lower Bound : {lower_bound:.2f}"
    )

    print(
        f"Upper Bound : {upper_bound:.2f}"
    )

    print(
        f"Outliers    : {len(outliers)}"
    )

    outlier_results.append(
        {
            "Column": column,
            "Q1": Q1,
            "Q3": Q3,
            "IQR": IQR,
            "Lower_Bound": lower_bound,
            "Upper_Bound": upper_bound,
            "Number_of_Outliers": len(outliers)
        }
    )


outlier_df = pd.DataFrame(
    outlier_results
)

outlier_df.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "outlier_analysis.csv"
    ),
    index=False
)


# ============================================================
# 45. GRAPH 1 - REVENUE BY PRODUCT
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    x=revenue_by_product.index,
    y=revenue_by_product.values,
    hue=revenue_by_product.index,
    palette="viridis",
    legend=False
)

plt.title(
    "Revenue by Product",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Product")

plt.ylabel("Revenue ($)")

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "01_revenue_by_product.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 46. GRAPH 2 - ORDER STATUS
# ============================================================

plt.figure(
    figsize=(8, 6)
)

plt.pie(
    order_status.values,
    labels=order_status.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title(
    "Order Status Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "02_order_status.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 47. GRAPH 3 - PAYMENT METHOD
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    x=payment_revenue.index,
    y=payment_revenue.values,
    hue=payment_revenue.index,
    palette="Set2",
    legend=False
)

plt.title(
    "Revenue by Payment Method",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Payment Method")

plt.ylabel("Revenue ($)")

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "03_revenue_by_payment_method.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 48. GRAPH 4 - REFERRAL SOURCE
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    x=referral_counts.index,
    y=referral_counts.values,
    hue=referral_counts.index,
    palette="Set1",
    legend=False
)

plt.title(
    "Orders by Referral Source",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Referral Source")

plt.ylabel("Number of Orders")

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "04_orders_by_referral_source.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 49. GRAPH 5 - QUANTITY BY PRODUCT
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    x=quantity_by_product.index,
    y=quantity_by_product.values,
    hue=quantity_by_product.index,
    palette="coolwarm",
    legend=False
)

plt.title(
    "Quantity Sold by Product",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Product")

plt.ylabel("Quantity Sold")

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "05_quantity_by_product.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 50. GRAPH 6 - MONTHLY REVENUE
# ============================================================

plt.figure(
    figsize=(14, 6)
)

plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o",
    linewidth=2,
    color="royalblue"
)

plt.title(
    "Monthly Revenue Trend",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")

plt.ylabel("Revenue ($)")

plt.xticks(
    rotation=60
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "06_monthly_revenue.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 51. GRAPH 7 - YEARLY REVENUE
# ============================================================

plt.figure(
    figsize=(9, 6)
)

sns.barplot(
    x=yearly_revenue.index.astype(str),
    y=yearly_revenue.values,
    hue=yearly_revenue.index.astype(str),
    palette="Blues",
    legend=False
)

plt.title(
    "Yearly Revenue",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Year")

plt.ylabel("Revenue ($)")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "07_yearly_revenue.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 52. GRAPH 8 - UNIT PRICE DISTRIBUTION
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.histplot(
    df["UnitPrice"],
    bins=20,
    kde=True,
    color="purple"
)

plt.title(
    "Unit Price Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Unit Price")

plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "08_unit_price_distribution.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 53. GRAPH 9 - TOTAL PRICE DISTRIBUTION
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.histplot(
    df["TotalPrice"],
    bins=20,
    kde=True,
    color="green"
)

plt.title(
    "Total Order Price Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Total Price")

plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "09_total_price_distribution.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 54. GRAPH 10 - CORRELATION HEATMAP
# ============================================================

plt.figure(
    figsize=(9, 7)
)

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title(
    "Correlation Heatmap",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "10_correlation_heatmap.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 55. SAVE FINAL ANALYZED DATASET
# ============================================================

# Remove helper columns
final_df = df.drop(
    columns=[
        "CalculatedTotal",
        "PriceDifference",
        "Year",
        "Month"
    ],
    errors="ignore"
)

final_file = os.path.join(
    OUTPUT_DIR,
    "final_analyzed_dataset.csv"
)

final_df.to_csv(
    final_file,
    index=False
)

print("\n" + "=" * 70)
print("FINAL ANALYZED DATASET")
print("=" * 70)

print(
    f"Saved successfully: {final_file}"
)


# ============================================================
# 56. KEY OBSERVATIONS
# ============================================================

print("\n" + "=" * 70)
print("KEY OBSERVATIONS")
print("=" * 70)


highest_status = (
    order_status
    .idxmax()
)

highest_status_count = (
    order_status
    .max()
)


highest_payment = (
    payment_revenue
    .idxmax()
)


highest_year = (
    yearly_revenue
    .idxmax()
)


print(
    f"""
1. Total number of orders:
   {total_orders:,}

2. Total revenue:
   ${total_revenue:,.2f}

3. Total quantity sold:
   {total_quantity:,}

4. Average order value:
   ${average_order_value:,.2f}

5. Number of unique customers:
   {unique_customers:,}

6. Highest revenue product:
   {top_product}
   Revenue = ${top_product_revenue:,.2f}

7. Highest quantity product:
   {top_quantity_product}
   Quantity = {top_quantity}

8. Most common order status:
   {highest_status}
   Orders = {highest_status_count}

9. Payment method generating the highest revenue:
   {highest_payment}

10. Referral source with the most orders:
    {top_referral}

11. Highest revenue year:
    {highest_year}

12. Incorrect TotalPrice records:
    {len(incorrect_total)}

13. Duplicate records:
    {duplicate_count}

14. Missing values:
    {total_missing}
"""
)


# ============================================================
# 57. FINAL CONCLUSION
# ============================================================

print("\n" + "=" * 70)
print("FINAL CONCLUSION")
print("=" * 70)

print(
    """
The Exploratory Data Analysis of the E-Commerce Orders
dataset was completed successfully.

The analysis examined the structure and quality of the data,
including missing values, duplicate records, data types,
invalid values, numerical statistics and price validation.

Business analysis was also performed for products, quantities,
revenue, order status, payment methods, referral sources,
coupon usage and customers.

Several visualizations were generated to understand revenue
trends, product performance, order status distribution,
payment methods, referral sources, price distributions and
correlations between numerical variables.

The generated reports and visualizations can be found inside
the output folder.
"""
)


# ============================================================
# 58. PROJECT COMPLETED
# ============================================================

print("\n" + "=" * 70)
print("EDA PROJECT COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nOutput folder:")
print(
    os.path.abspath(OUTPUT_DIR)
)

print("\nGenerated analysis files are available in the output folder.")
print("=" * 70)
