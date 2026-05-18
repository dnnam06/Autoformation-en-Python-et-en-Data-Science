import pandas as pd
# ====== Prise de notes ======
# print(df.tail(n: int)) : print n datas from the bottom
# print(df.sample(n: int)) : print n datas randomly
# print(df.head(n: int)) : iprint n datas from the top

df = pd.read_csv("table_csv/table_revenu.csv", parse_dates=["date"])

# Small exercise : build a custom rounding function 
def round_number_2(n: float):
    str_n = str(n)
    detach = str_n.split('.')
    if float(detach[1]) >= 0.5:
        n = int(detach[0]) + 1
    else:
        n = int(detach[0])

    return n

def round_number_1(n: float):
    xy = str(n)
    index = xy.find('.')
    decimal = '0' + xy[index:]
    if float(decimal) >= 0.5:
        n = int(xy) + 1
    else:
        n = int(xy[:index]) 

    return n

# =========================================================
# INSERT COLUMN AT A SPECIFIC POSITION
# =========================================================

# Get the column index of 'price'
location = df.columns.get_loc('price')

# Insert a new column near the middle position
df.insert(
    loc=round_number_1(location / 2),
    column='sub_total',
    value=df['quantity'] * df['price']
)

# =========================================================
# SELECT ROWS WITH EVEN INDEXES
# =========================================================

df_pair = df[df.index % 2 == 0]

# =========================================================
# GROUP DATA BY DAY
# =========================================================

# Group by date and calculate total revenue
daily_revenue = (
    df.groupby(df["date"].dt.date)["sub_total"]
    .sum()
)

# print(daily_revenue)

# =========================================================
# FILTER DATA AFTER A SPECIFIC DATE
# =========================================================

after_date = df[df['date'] >= "2024-01-03"]

# =========================================================
# FILTER DATA BY TIME
# 
# METHOD 1:
# FILTER DATA USING DATETIME INDEX
# =========================================================

# Create a backup datetime column
df['date_copy'] = df['date']

# Convert date column into datetime index
df_date = df.set_index("date")

# Sort index (important for time filtering)
df_date = df_date.sort_index()

# Select rows between two dates
df1 = df_date["2024-01-02":"2024-01-04"]

# Keep only rows exactly at 10:00
df1 = df1.at_time('10:00')

# Select rows between 13:00 and 17:00
df2 = df_date.between_time('13:00', '17:00')

# Merge results
df_date2 = pd.merge(df1, df2, how='outer')

# Restore datetime index
df_date2 = df_date2.set_index('date_copy')

# Sort index again
df_date2 = df_date2.sort_index()

# Remove index name display (comment this if can't see the difference)
df_date2.index.name = None

# print(df_date2)

# =========================================================
# METHOD 2:
# FILTER DATA USING BOOLEAN CONDITIONS
# =========================================================

# Define datetime interval
start_ts = pd.Timestamp('2024-01-02 10:00:00')
end_ts = pd.Timestamp('2024-01-04 15:00:00')

# Filter rows inside datetime range
df_loc_ts = df[
    (df['date'] >= start_ts) &
    (df['date'] <= end_ts)
]

# Set datetime column as index
df_time = df_loc_ts.set_index('date')

# Keep only rows exactly at 12:30
df_time = df_time.at_time('12:30')

# Remove index name display
df_time.index.name = None

print(df_time)