import pandas as pd

# ==========================================
# SMART DATA CLEANER
# ==========================================

print("======================================")
print("       SMART DATA CLEANER")
print("======================================")

# ------------------------------------------
# STEP 1: Load Raw Dataset
# ------------------------------------------

# Dataset is TAB-separated
df = pd.read_csv("raw_data.csv", sep="\t")

print("\nOriginal Dataset:")
print(df)

print("\nOriginal Number of Rows:", len(df))
print("Original Number of Columns:", len(df.columns))


# ------------------------------------------
# STEP 2: Identify Missing Values
# ------------------------------------------

print("\n======================================")
print("MISSING VALUES")
print("======================================")

print(df.isnull().sum())


# ------------------------------------------
# STEP 3: Find Duplicate Records
# ------------------------------------------

print("\n======================================")
print("DUPLICATE RECORDS")
print("======================================")

duplicates = df.duplicated().sum()

print("Number of duplicate records:", duplicates)


# ------------------------------------------
# STEP 4: Clean Text Columns
# ------------------------------------------

text_columns = [
    "OrderID",
    "CustomerID",
    "Product",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "TrackingNumber",
    "CouponCode",
    "ReferralSource"
]

for col in text_columns:
    df[col] = df[col].astype("string").str.strip()


# ------------------------------------------
# STEP 5: Standardize Product Names
# ------------------------------------------

df["Product"] = df["Product"].str.title()


# ------------------------------------------
# STEP 6: Standardize Payment Method
# ------------------------------------------

df["PaymentMethod"] = df["PaymentMethod"].str.title()


# ------------------------------------------
# STEP 7: Standardize Order Status
# ------------------------------------------

df["OrderStatus"] = df["OrderStatus"].str.title()


# ------------------------------------------
# STEP 8: Clean Date
# ------------------------------------------

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

# Convert date to YYYY-MM-DD
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# Keep missing dates blank
df["Date"] = df["Date"].fillna("")


# ------------------------------------------
# STEP 9: Clean Numeric Columns
# ------------------------------------------

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )


# ------------------------------------------
# STEP 10: Handle Missing Numeric Values
# ------------------------------------------

for col in numeric_columns:

    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(
            df[col].median()
        )


# ------------------------------------------
# STEP 11: Remove Invalid Values
# ------------------------------------------

# Quantity should not be negative or zero
df.loc[
    df["Quantity"] <= 0,
    "Quantity"
] = pd.NA

# Refill invalid quantities with median
df["Quantity"] = df["Quantity"].fillna(
    df["Quantity"].median()
)

# Unit price should not be negative
df.loc[
    df["UnitPrice"] < 0,
    "UnitPrice"
] = pd.NA

df["UnitPrice"] = df["UnitPrice"].fillna(
    df["UnitPrice"].median()
)

# Items in cart should not be negative
df.loc[
    df["ItemsInCart"] < 0,
    "ItemsInCart"
] = pd.NA

df["ItemsInCart"] = df["ItemsInCart"].fillna(
    df["ItemsInCart"].median()
)

# Total price should not be negative
df.loc[
    df["TotalPrice"] < 0,
    "TotalPrice"
] = pd.NA

df["TotalPrice"] = df["TotalPrice"].fillna(
    df["TotalPrice"].median()
)


# ------------------------------------------
# STEP 12: Handle Missing Text Values
# ------------------------------------------

df["ShippingAddress"] = df["ShippingAddress"].fillna(
    "Not Provided"
)

df["PaymentMethod"] = df["PaymentMethod"].fillna(
    "Not Provided"
)

df["OrderStatus"] = df["OrderStatus"].fillna(
    "Unknown"
)

df["TrackingNumber"] = df["TrackingNumber"].fillna(
    "Not Available"
)

df["CouponCode"] = df["CouponCode"].fillna(
    "No Coupon"
)

df["ReferralSource"] = df["ReferralSource"].fillna(
    "Unknown"
)


# ------------------------------------------
# STEP 13: Remove Duplicate Records
# ------------------------------------------

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

removed = before_duplicates - after_duplicates

print("\nDuplicates Removed:", removed)


# ------------------------------------------
# STEP 14: Round Numeric Values
# ------------------------------------------

df["Quantity"] = df["Quantity"].round().astype("Int64")

df["ItemsInCart"] = (
    df["ItemsInCart"]
    .round()
    .astype("Int64")
)

df["UnitPrice"] = df["UnitPrice"].round(2)

df["TotalPrice"] = df["TotalPrice"].round(2)


# ------------------------------------------
# STEP 15: Final Dataset Information
# ------------------------------------------

print("\n======================================")
print("CLEANED DATASET")
print("======================================")

print(df)

print("\nCleaned Number of Rows:", len(df))
print("Cleaned Number of Columns:", len(df.columns))


# ------------------------------------------
# STEP 16: Check Remaining Missing Values
# ------------------------------------------

print("\n======================================")
print("REMAINING MISSING VALUES")
print("======================================")

print(df.isnull().sum())


# ------------------------------------------
# STEP 17: Save Cleaned Dataset
# ------------------------------------------

df.to_csv(
    "cleaned_data.csv",
    index=False
)

print("\n======================================")
print("SUCCESS")
print("======================================")

print("Cleaned dataset saved as:")
print("cleaned_data.csv")
